from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import init_db, get_db
from functools import wraps
import os
import math

# Import distances
from distance import distances  # distances[state1][state2] = km

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret-change-me")

# ---- App startup (ensure DB ready) ----
with app.app_context():
    init_db()

# ---- Helpers ----
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in first.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

def get_distance(source, destination):
    if source in distances and destination in distances[source]:
        return distances[source][destination]
    elif destination in distances and source in distances[destination]:
        return distances[destination][source]
    else:
        return 800  # default distance if not found

# ---- Routes: Auth ----
@app.route("/")
def home():
    return redirect(url_for("plan_trip") if session.get("user_id") else url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            flash("Username and password are required.", "danger")
            return render_template("login.html", page_class="login-page")
        with get_db() as db:
            row = db.execute("SELECT id, password FROM users WHERE username = ?", (username,)).fetchone()
        if row and check_password_hash(row[1], password):
            session.clear()
            session["user_id"] = row[0]
            session["username"] = username
            flash("Logged in successfully!", "success")
            return redirect(url_for("plan_trip"))
        flash("Invalid credentials.", "danger")
    return render_template("login.html", page_class="login-page")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")
        if not username or not password:
            flash("All fields are required.", "danger")
            return render_template("signup.html", page_class="signup-page")
        if password != confirm:
            flash("Passwords do not match.", "danger")
            return render_template("signup.html", page_class="signup-page")
        pw_hash = generate_password_hash(password)
        try:
            with get_db() as db:
                db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, pw_hash))
                db.commit()
            flash("Signup successful. Please log in.", "success")
            return redirect(url_for("login"))
        except Exception:
            flash("Username already exists.", "warning")
    return render_template("signup.html", page_class="signup-page")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.", "info")
    return redirect(url_for("login"))

# ---- Trip Planning ----
@app.route("/trip", methods=["GET", "POST"])
@login_required
def plan_trip():
    if request.method == "POST":
        source = request.form.get("source", "").strip()
        destination = request.form.get("destination", "").strip()
        start_date = request.form.get("start_date", "").strip()
        end_date = request.form.get("end_date", "").strip()
        persons = int(request.form.get("persons", 1))
        days = int(request.form.get("days", 1))

        if not source or not destination or not start_date or not end_date:
            flash("Please fill all fields.", "danger")
            return render_template("trip.html", page_class="trip-page")

        distance = get_distance(source, destination)

        with get_db() as db:
            cur = db.execute(
                """
                INSERT INTO trips (user_id, source, destination, persons, days, start_date, end_date, distance)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (session["user_id"], source, destination, persons, days, start_date, end_date, distance)
            )
            db.commit()
            trip_id = cur.lastrowid

        session["last_trip_id"] = trip_id
        return redirect(url_for("budget"))

    return render_template("trip.html", page_class="trip-page")

# ---- Budget Logic ----
def estimate_budget(persons: int, days: int, distance: int):
    transport = distance * 5 * persons   # reduced cost per km for India travel
    local_transport = 200 * days * persons
    rooms = max(1, math.ceil(persons / 2))
    hotel = 1800 * rooms * days
    food = 500 * days * persons
    total = transport + local_transport + hotel + food
    return {
        "transport": transport,
        "local_transport": local_transport,
        "hotel": hotel,
        "food": food,
        "total": total,
        "rooms": rooms,
    }

def suggest_hotels(destination: str):
    return [
        {"name": f"{destination} Central Inn", "area": "City Center", "approx": 2000},
        {"name": f"{destination} Cozy Stay", "area": "Near Railway Station", "approx": 1800},
        {"name": f"{destination} Green View", "area": "Quiet Neighborhood", "approx": 2200},
    ]

def transport_options(source: str, destination: str):
    return [
        {"mode": "Train", "notes": "Economical, overnight options available."},
        {"mode": "Bus", "notes": "Sleeper/AC buses between major cities."},
        {"mode": "Flight", "notes": "Fastest for long routes."},
        {"mode": "Cab/Taxi", "notes": "Convenient for local sightseeing."},
        {"mode": "Metro/Local", "notes": "Available in metro cities."},
    ]

@app.route("/budget")
@login_required
def budget():
    trip_id = session.get("last_trip_id")
    if not trip_id:
        flash("Plan a trip first.", "warning")
        return redirect(url_for("plan_trip"))

    with get_db() as db:
        row = db.execute(
            "SELECT source, destination, persons, days, start_date, end_date, distance FROM trips WHERE id = ? AND user_id = ?",
            (trip_id, session["user_id"])
        ).fetchone()

    if not row:
        flash("Trip not found.", "danger")
        return redirect(url_for("plan_trip"))

    source, destination, persons, days, start_date, end_date, distance = row
    est = estimate_budget(persons, days, distance)
    hotels = suggest_hotels(destination)
    transports = transport_options(source, destination)

    return render_template(
        "budget.html",
        page_class="budget-page",
        trip={
            "source": source,
            "destination": destination,
            "persons": persons,
            "days": days,
            "start_date": start_date,
            "end_date": end_date,
            "distance": distance,
        },
        est=est,
        hotels=hotels,
        transports=transports,
    )

# ---- Trips History ----
@app.route("/my_trips")
@login_required
def my_trips():
    with get_db() as db:
        rows = db.execute(
            "SELECT id, source, destination, persons, days, start_date, end_date FROM trips WHERE user_id = ? ORDER BY start_date DESC",
            (session["user_id"],)
        ).fetchall()

    trips = [
        {
            "id": r[0],
            "source": r[1],
            "destination": r[2],
            "persons": r[3],
            "days": r[4],
            "start_date": r[5],
            "end_date": r[6],
        }
        for r in rows
    ]
    return render_template("my_trips.html", trips=trips, page_class="trip-page")

@app.route("/trip/<int:trip_id>")
@login_required
def view_trip(trip_id):
    with get_db() as db:
        trip = db.execute(
            "SELECT source, destination, persons, days, start_date, end_date, distance FROM trips WHERE id = ? AND user_id = ?",
            (trip_id, session["user_id"])
        ).fetchone()

    if not trip:
        flash("Trip not found.", "danger")
        return redirect(url_for("my_trips"))

    est = estimate_budget(trip[2], trip[3], trip[6])
    hotels = suggest_hotels(trip[1])
    transports = transport_options(trip[0], trip[1])

    return render_template(
        "budget.html",
        page_class="trip-page",
        trip={
            "source": trip[0],
            "destination": trip[1],
            "persons": trip[2],
            "days": trip[3],
            "start_date": trip[4],
            "end_date": trip[5],
            "distance": trip[6],
        },
        est=est,
        hotels=hotels,
        transports=transports,
    )

@app.route("/clear_trips", methods=["POST"])
@login_required
def clear_trips():
    with get_db() as db:
        db.execute("DELETE FROM trips WHERE user_id = ?", (session["user_id"],))
        db.commit()
    flash("All previous trips cleared.", "success")
    return redirect(url_for("my_trips"))

# ---- Run App ----
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
