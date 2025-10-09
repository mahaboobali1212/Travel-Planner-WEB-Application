# distance.py

# Approximate road distances between Indian states/UTs in kilometers
# The distances are symmetric: distance[A][B] = distance[B][A]

distances = {
    "Andhra Pradesh": {
        "Arunachal Pradesh": 3500, "Assam": 3000, "Bihar": 1500, "Chhattisgarh": 700,
        "Goa": 900, "Gujarat": 1800, "Haryana": 2000, "Himachal Pradesh": 2200,
        "Jharkhand": 1000, "Karnataka": 500, "Kerala": 800, "Madhya Pradesh": 1200,
        "Maharashtra": 1000, "Manipur": 3200, "Meghalaya": 3000, "Mizoram": 3400,
        "Nagaland": 3100, "Odisha": 600, "Punjab": 2100, "Rajasthan": 2000, "Sikkim": 2900,
        "Tamil Nadu": 450, "Telangana": 350, "Tripura": 3300, "Uttar Pradesh": 1800,
        "Uttarakhand": 2200, "West Bengal": 1200, "Andaman and Nicobar Islands": 2300,
        "Chandigarh": 2100, "Dadra and Nagar Haveli and Daman and Diu": 1900, "Delhi": 2000,
        "Jammu and Kashmir": 2500, "Ladakh": 3000, "Lakshadweep": 900, "Puducherry": 400
    },

    "Arunachal Pradesh": {
        "Andhra Pradesh": 3500, "Assam": 500, "Bihar": 2200, "Chhattisgarh": 3200,
        "Goa": 4200, "Gujarat": 4500, "Haryana": 3800, "Himachal Pradesh": 3600,
        "Jharkhand": 2400, "Karnataka": 4700, "Kerala": 5200, "Madhya Pradesh": 3400,
        "Maharashtra": 4300, "Manipur": 1500, "Meghalaya": 800, "Mizoram": 1700,
        "Nagaland": 700, "Odisha": 2800, "Punjab": 3700, "Rajasthan": 4000, "Sikkim": 1000,
        "Tamil Nadu": 5000, "Telangana": 3700, "Tripura": 1600, "Uttar Pradesh": 3200,
        "Uttarakhand": 3500, "West Bengal": 1400, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 3700, "Dadra and Nagar Haveli and Daman and Diu": 4700, "Delhi": 3600,
        "Jammu and Kashmir": 3700, "Ladakh": 3900, "Lakshadweep": 5200, "Puducherry": 4900
    },

    "Assam": {
        "Andhra Pradesh": 3000, "Arunachal Pradesh": 500, "Bihar": 1800, "Chhattisgarh": 2800,
        "Goa": 4200, "Gujarat": 4500, "Haryana": 3600, "Himachal Pradesh": 3500,
        "Jharkhand": 1500, "Karnataka": 4200, "Kerala": 4700, "Madhya Pradesh": 3000,
        "Maharashtra": 3800, "Manipur": 1200, "Meghalaya": 350, "Mizoram": 800,
        "Nagaland": 500, "Odisha": 2300, "Punjab": 3500, "Rajasthan": 4000, "Sikkim": 900,
        "Tamil Nadu": 4500, "Telangana": 3500, "Tripura": 1000, "Uttar Pradesh": 2800,
        "Uttarakhand": 3200, "West Bengal": 600, "Andaman and Nicobar Islands": 4300,
        "Chandigarh": 3600, "Dadra and Nagar Haveli and Daman and Diu": 4600, "Delhi": 3500,
        "Jammu and Kashmir": 3600, "Ladakh": 3800, "Lakshadweep": 4700, "Puducherry": 4200
    },

    "Bihar": {
        "Andhra Pradesh": 1500, "Arunachal Pradesh": 2200, "Assam": 1800, "Chhattisgarh": 1200,
        "Goa": 2100, "Gujarat": 1800, "Haryana": 1200, "Himachal Pradesh": 1400,
        "Jharkhand": 400, "Karnataka": 2200, "Kerala": 2800, "Madhya Pradesh": 1000,
        "Maharashtra": 1800, "Manipur": 1800, "Meghalaya": 1500, "Mizoram": 2000,
        "Nagaland": 1800, "Odisha": 900, "Punjab": 1400, "Rajasthan": 1600, "Sikkim": 1500,
        "Tamil Nadu": 2700, "Telangana": 2000, "Tripura": 1900, "Uttar Pradesh": 600,
        "Uttarakhand": 1100, "West Bengal": 800, "Andaman and Nicobar Islands": 2500,
        "Chandigarh": 1400, "Dadra and Nagar Haveli and Daman and Diu": 2000, "Delhi": 1200,
        "Jammu and Kashmir": 1600, "Ladakh": 2200, "Lakshadweep": 2800, "Puducherry": 2200
    },

    "Chhattisgarh": {
    "Goa": 1100, "Gujarat": 1500, "Haryana": 1800, "Himachal Pradesh": 2000, "Jharkhand": 900,
    "Karnataka": 1200, "Kerala": 1700, "Madhya Pradesh": 700, "Maharashtra": 1000, "Manipur": 2200,
    "Meghalaya": 2100, "Mizoram": 2300, "Nagaland": 2200, "Odisha": 600, "Punjab": 1800,
    "Rajasthan": 1500, "Sikkim": 2100, "Tamil Nadu": 1800, "Telangana": 1000, "Tripura": 2300,
    "Uttar Pradesh": 1300, "Uttarakhand": 1800, "West Bengal": 1000, "Andaman and Nicobar Islands": 2500,
    "Chandigarh": 1800, "Dadra and Nagar Haveli and Daman and Diu": 1300, "Delhi": 1800,
    "Jammu and Kashmir": 2200, "Ladakh": 2600, "Lakshadweep": 1700, "Puducherry": 1300
    },

    "Goa": {
    "Gujarat": 700, "Haryana": 2200, "Himachal Pradesh": 2400, "Jharkhand": 2100,
    "Karnataka": 400, "Kerala": 600, "Madhya Pradesh": 1200, "Maharashtra": 450,
    "Manipur": 3200, "Meghalaya": 3000, "Mizoram": 3300, "Nagaland": 3100, "Odisha": 1800,
    "Punjab": 2200, "Rajasthan": 1900, "Sikkim": 3000, "Tamil Nadu": 900, "Telangana": 1000,
    "Tripura": 3100, "Uttar Pradesh": 1900, "Uttarakhand": 2200, "West Bengal": 2300,
    "Andaman and Nicobar Islands": 2200, "Chandigarh": 2200, "Dadra and Nagar Haveli and Daman and Diu": 500,
    "Delhi": 2100, "Jammu and Kashmir": 2500, "Ladakh": 3000, "Lakshadweep": 600, "Puducherry": 850
},

"Gujarat": {
    "Haryana": 1200, "Himachal Pradesh": 1400, "Jharkhand": 1800, "Karnataka": 1500,
    "Kerala": 2000, "Madhya Pradesh": 900, "Maharashtra": 700, "Manipur": 4000,
    "Meghalaya": 3600, "Mizoram": 4000, "Nagaland": 3800, "Odisha": 1600, "Punjab": 800,
    "Rajasthan": 400, "Sikkim": 3700, "Tamil Nadu": 2200, "Telangana": 1500, "Tripura": 3800,
    "Uttar Pradesh": 1200, "Uttarakhand": 1400, "West Bengal": 2300, "Andaman and Nicobar Islands": 3200,
    "Chandigarh": 900, "Dadra and Nagar Haveli and Daman and Diu": 200, "Delhi": 1200,
    "Jammu and Kashmir": 1600, "Ladakh": 2200, "Lakshadweep": 2000, "Puducherry": 2200
},
 "Haryana": {
        "Andhra Pradesh": 2000, "Arunachal Pradesh": 3800, "Assam": 3600, "Bihar": 1200,
        "Chhattisgarh": 1500, "Goa": 2200, "Gujarat": 1300, "Himachal Pradesh": 400,
        "Jharkhand": 1100, "Karnataka": 2300, "Kerala": 2800, "Madhya Pradesh": 900,
        "Maharashtra": 1800, "Manipur": 3200, "Meghalaya": 3200, "Mizoram": 3500,
        "Nagaland": 3400, "Odisha": 1700, "Punjab": 200, "Rajasthan": 400, "Sikkim": 2600,
        "Tamil Nadu": 3000, "Telangana": 2200, "Tripura": 3400, "Uttar Pradesh": 300,
        "Uttarakhand": 350, "West Bengal": 1800, "Andaman and Nicobar Islands": 4000,
        "Chandigarh": 250, "Dadra and Nagar Haveli and Daman and Diu": 2300, "Delhi": 200,
        "Jammu and Kashmir": 900, "Ladakh": 1200, "Lakshadweep": 3100, "Puducherry": 2800
    },

    "Himachal Pradesh": {
        "Andhra Pradesh": 2200, "Arunachal Pradesh": 3600, "Assam": 3500, "Bihar": 1400,
        "Chhattisgarh": 2000, "Goa": 2600, "Gujarat": 2000, "Haryana": 400,
        "Jharkhand": 1500, "Karnataka": 2700, "Kerala": 3200, "Madhya Pradesh": 1300,
        "Maharashtra": 2200, "Manipur": 3600, "Meghalaya": 3400, "Mizoram": 3800,
        "Nagaland": 3700, "Odisha": 2000, "Punjab": 300, "Rajasthan": 800, "Sikkim": 1000,
        "Tamil Nadu": 3500, "Telangana": 2400, "Tripura": 3600, "Uttar Pradesh": 900,
        "Uttarakhand": 200, "West Bengal": 2200, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 300, "Dadra and Nagar Haveli and Daman and Diu": 2800, "Delhi": 500,
        "Jammu and Kashmir": 600, "Ladakh": 1000, "Lakshadweep": 3400, "Puducherry": 3100
    },

    "Jharkhand": {
        "Andhra Pradesh": 1000, "Arunachal Pradesh": 2400, "Assam": 1500, "Bihar": 400,
        "Chhattisgarh": 800, "Goa": 2200, "Gujarat": 1800, "Haryana": 1100,
        "Himachal Pradesh": 1500, "Karnataka": 1800, "Kerala": 2400, "Madhya Pradesh": 1000,
        "Maharashtra": 1600, "Manipur": 2200, "Meghalaya": 1600, "Mizoram": 2100,
        "Nagaland": 2000, "Odisha": 600, "Punjab": 1400, "Rajasthan": 1600, "Sikkim": 1600,
        "Tamil Nadu": 2500, "Telangana": 1200, "Tripura": 2100, "Uttar Pradesh": 700,
        "Uttarakhand": 1200, "West Bengal": 500, "Andaman and Nicobar Islands": 2700,
        "Chandigarh": 1500, "Dadra and Nagar Haveli and Daman and Diu": 2000, "Delhi": 1200,
        "Jammu and Kashmir": 1600, "Ladakh": 2200, "Lakshadweep": 2800, "Puducherry": 2000
    },

    "Karnataka": {
        "Andhra Pradesh": 500, "Arunachal Pradesh": 4700, "Assam": 4200, "Bihar": 2200,
        "Chhattisgarh": 1000, "Goa": 400, "Gujarat": 1400, "Haryana": 2300,
        "Himachal Pradesh": 2700, "Jharkhand": 1800, "Kerala": 600, "Madhya Pradesh": 1200,
        "Maharashtra": 1000, "Manipur": 3800, "Meghalaya": 4000, "Mizoram": 4200,
        "Nagaland": 4100, "Odisha": 1500, "Punjab": 2500, "Rajasthan": 1800, "Sikkim": 3900,
        "Tamil Nadu": 350, "Telangana": 500, "Tripura": 4100, "Uttar Pradesh": 2000,
        "Uttarakhand": 2700, "West Bengal": 2000, "Andaman and Nicobar Islands": 2700,
        "Chandigarh": 2500, "Dadra and Nagar Haveli and Daman and Diu": 1500, "Delhi": 2300,
        "Jammu and Kashmir": 2700, "Ladakh": 3200, "Lakshadweep": 650, "Puducherry": 300
    },

    "Kerala": {
        "Andhra Pradesh": 800, "Arunachal Pradesh": 5200, "Assam": 4700, "Bihar": 2800,
        "Chhattisgarh": 1400, "Goa": 900, "Gujarat": 1800, "Haryana": 2800,
        "Himachal Pradesh": 3200, "Jharkhand": 2400, "Karnataka": 600, "Madhya Pradesh": 1500,
        "Maharashtra": 1200, "Manipur": 4300, "Meghalaya": 4600, "Mizoram": 4800,
        "Nagaland": 4700, "Odisha": 2000, "Punjab": 3000, "Rajasthan": 2100, "Sikkim": 4400,
        "Tamil Nadu": 450, "Telangana": 800, "Tripura": 4700, "Uttar Pradesh": 2500,
        "Uttarakhand": 3200, "West Bengal": 2500, "Andaman and Nicobar Islands": 3000,
        "Chandigarh": 3000, "Dadra and Nagar Haveli and Daman and Diu": 1800, "Delhi": 2800,
        "Jammu and Kashmir": 3200, "Ladakh": 3700, "Lakshadweep": 700, "Puducherry": 500
    },
    "Madhya Pradesh": {
        "Andhra Pradesh": 1200, "Arunachal Pradesh": 3400, "Assam": 3000, "Bihar": 900,
        "Chhattisgarh": 600, "Goa": 1400, "Gujarat": 900, "Haryana": 900,
        "Himachal Pradesh": 1300, "Jharkhand": 1000, "Karnataka": 1200, "Kerala": 1500,
        "Maharashtra": 700, "Manipur": 3500, "Meghalaya": 3200, "Mizoram": 3800,
        "Nagaland": 3700, "Odisha": 1200, "Punjab": 1100, "Rajasthan": 800, "Sikkim": 2600,
        "Tamil Nadu": 1600, "Telangana": 1000, "Tripura": 3600, "Uttar Pradesh": 700,
        "Uttarakhand": 900, "West Bengal": 1500, "Andaman and Nicobar Islands": 2800,
        "Chandigarh": 1300, "Dadra and Nagar Haveli and Daman and Diu": 1300, "Delhi": 900,
        "Jammu and Kashmir": 1500, "Ladakh": 2000, "Lakshadweep": 1600, "Puducherry": 1400
    },

    "Maharashtra": {
        "Andhra Pradesh": 900, "Arunachal Pradesh": 4300, "Assam": 4000, "Bihar": 1600,
        "Chhattisgarh": 1000, "Goa": 450, "Gujarat": 600, "Haryana": 1800,
        "Himachal Pradesh": 2200, "Jharkhand": 1600, "Karnataka": 1000, "Kerala": 1200,
        "Madhya Pradesh": 700, "Manipur": 4200, "Meghalaya": 4000, "Mizoram": 4600,
        "Nagaland": 4500, "Odisha": 1400, "Punjab": 2000, "Rajasthan": 1200, "Sikkim": 3900,
        "Tamil Nadu": 1300, "Telangana": 900, "Tripura": 4200, "Uttar Pradesh": 1300,
        "Uttarakhand": 2200, "West Bengal": 1800, "Andaman and Nicobar Islands": 2500,
        "Chandigarh": 2200, "Dadra and Nagar Haveli and Daman and Diu": 450, "Delhi": 1800,
        "Jammu and Kashmir": 2200, "Ladakh": 2700, "Lakshadweep": 1200, "Puducherry": 1200
    },

    "Manipur": {
        "Andhra Pradesh": 3500, "Arunachal Pradesh": 1500, "Assam": 500, "Bihar": 2200,
        "Chhattisgarh": 3200, "Goa": 4200, "Gujarat": 4500, "Haryana": 3200,
        "Himachal Pradesh": 3600, "Jharkhand": 2200, "Karnataka": 3800, "Kerala": 4300,
        "Madhya Pradesh": 3500, "Maharashtra": 4200, "Meghalaya": 800, "Mizoram": 700,
        "Nagaland": 900, "Odisha": 2800, "Punjab": 3700, "Rajasthan": 4000, "Sikkim": 1200,
        "Tamil Nadu": 5000, "Telangana": 3700, "Tripura": 600, "Uttar Pradesh": 3200,
        "Uttarakhand": 3500, "West Bengal": 1400, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 3700, "Dadra and Nagar Haveli and Daman and Diu": 4700, "Delhi": 3600,
        "Jammu and Kashmir": 3700, "Ladakh": 3900, "Lakshadweep": 5200, "Puducherry": 4900
    },

    "Meghalaya": {
        "Andhra Pradesh": 3200, "Arunachal Pradesh": 800, "Assam": 300, "Bihar": 1800,
        "Chhattisgarh": 2600, "Goa": 4000, "Gujarat": 4200, "Haryana": 3200,
        "Himachal Pradesh": 3400, "Jharkhand": 1600, "Karnataka": 4000, "Kerala": 4600,
        "Madhya Pradesh": 3200, "Maharashtra": 4000, "Manipur": 800, "Mizoram": 900,
        "Nagaland": 1000, "Odisha": 2200, "Punjab": 3200, "Rajasthan": 3600, "Sikkim": 1000,
        "Tamil Nadu": 4800, "Telangana": 3600, "Tripura": 1000, "Uttar Pradesh": 2800,
        "Uttarakhand": 3400, "West Bengal": 800, "Andaman and Nicobar Islands": 4000,
        "Chandigarh": 3400, "Dadra and Nagar Haveli and Daman and Diu": 4700, "Delhi": 3200,
        "Jammu and Kashmir": 3400, "Ladakh": 3600, "Lakshadweep": 4800, "Puducherry": 4500
    },

    "Mizoram": {
        "Andhra Pradesh": 3700, "Arunachal Pradesh": 1700, "Assam": 1600, "Bihar": 2100,
        "Chhattisgarh": 3200, "Goa": 4700, "Gujarat": 5000, "Haryana": 3500,
        "Himachal Pradesh": 3800, "Jharkhand": 2100, "Karnataka": 4200, "Kerala": 4800,
        "Madhya Pradesh": 3800, "Maharashtra": 4600, "Manipur": 700, "Meghalaya": 900,
        "Nagaland": 800, "Odisha": 2600, "Punjab": 3800, "Rajasthan": 4200, "Sikkim": 1200,
        "Tamil Nadu": 5000, "Telangana": 4000, "Tripura": 900, "Uttar Pradesh": 3200,
        "Uttarakhand": 3800, "West Bengal": 1400, "Andaman and Nicobar Islands": 4500,
        "Chandigarh": 3800, "Dadra and Nagar Haveli and Daman and Diu": 5000, "Delhi": 3800,
        "Jammu and Kashmir": 4000, "Ladakh": 4200, "Lakshadweep": 5200, "Puducherry": 5000
    },

    "Nagaland": {
        "Andhra Pradesh": 3600, "Arunachal Pradesh": 700, "Assam": 400, "Bihar": 2000,
        "Chhattisgarh": 3000, "Goa": 4000, "Gujarat": 4300, "Haryana": 3400,
        "Himachal Pradesh": 3700, "Jharkhand": 2000, "Karnataka": 4100, "Kerala": 4700,
        "Madhya Pradesh": 3700, "Maharashtra": 4500, "Manipur": 900, "Meghalaya": 1000,
        "Mizoram": 800, "Odisha": 2400, "Punjab": 3700, "Rajasthan": 4000, "Sikkim": 1200,
        "Tamil Nadu": 4800, "Telangana": 3800, "Tripura": 800, "Uttar Pradesh": 3200,
        "Uttarakhand": 3700, "West Bengal": 1200, "Andaman and Nicobar Islands": 4500,
        "Chandigarh": 3700, "Dadra and Nagar Haveli and Daman and Diu": 4700, "Delhi": 3600,
        "Jammu and Kashmir": 3800, "Ladakh": 4000, "Lakshadweep": 5200, "Puducherry": 4900
    },
    "Odisha": {
        "Andhra Pradesh": 800, "Arunachal Pradesh": 2800, "Assam": 1800, "Bihar": 1000,
        "Chhattisgarh": 600, "Goa": 2000, "Gujarat": 1800, "Haryana": 2200,
        "Himachal Pradesh": 2400, "Jharkhand": 500, "Karnataka": 1500, "Kerala": 2200,
        "Madhya Pradesh": 1200, "Maharashtra": 1400, "Manipur": 2800, "Meghalaya": 2200,
        "Mizoram": 2600, "Nagaland": 2400, "Punjab": 2200, "Rajasthan": 1800, "Sikkim": 1600,
        "Tamil Nadu": 1800, "Telangana": 900, "Tripura": 2600, "Uttar Pradesh": 1200,
        "Uttarakhand": 1500, "West Bengal": 800, "Andaman and Nicobar Islands": 3000,
        "Chandigarh": 2200, "Dadra and Nagar Haveli and Daman and Diu": 1800, "Delhi": 2000,
        "Jammu and Kashmir": 2400, "Ladakh": 2800, "Lakshadweep": 2200, "Puducherry": 1600
    },

    "Punjab": {
        "Andhra Pradesh": 1800, "Arunachal Pradesh": 3800, "Assam": 3200, "Bihar": 1800,
        "Chhattisgarh": 1400, "Goa": 2600, "Gujarat": 1500, "Haryana": 200,
        "Himachal Pradesh": 300, "Jharkhand": 1600, "Karnataka": 2600, "Kerala": 3000,
        "Madhya Pradesh": 1100, "Maharashtra": 2000, "Manipur": 3700, "Meghalaya": 3200,
        "Mizoram": 3800, "Nagaland": 3700, "Odisha": 2200, "Rajasthan": 600, "Sikkim": 1800,
        "Tamil Nadu": 3000, "Telangana": 2100, "Tripura": 3700, "Uttar Pradesh": 700,
        "Uttarakhand": 400, "West Bengal": 2000, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 200, "Dadra and Nagar Haveli and Daman and Diu": 2600, "Delhi": 400,
        "Jammu and Kashmir": 700, "Ladakh": 1200, "Lakshadweep": 3000, "Puducherry": 2600
    },

    "Rajasthan": {
        "Andhra Pradesh": 1200, "Arunachal Pradesh": 4000, "Assam": 3600, "Bihar": 2200,
        "Chhattisgarh": 1400, "Goa": 2000, "Gujarat": 900, "Haryana": 600,
        "Himachal Pradesh": 800, "Jharkhand": 1800, "Karnataka": 2200, "Kerala": 2800,
        "Madhya Pradesh": 800, "Maharashtra": 1200, "Manipur": 4000, "Meghalaya": 3600,
        "Mizoram": 4200, "Nagaland": 4000, "Odisha": 1800, "Punjab": 600, "Sikkim": 2200,
        "Tamil Nadu": 3000, "Telangana": 1800, "Tripura": 4000, "Uttar Pradesh": 900,
        "Uttarakhand": 800, "West Bengal": 2200, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 800, "Dadra and Nagar Haveli and Daman and Diu": 1200, "Delhi": 900,
        "Jammu and Kashmir": 1200, "Ladakh": 1500, "Lakshadweep": 2800, "Puducherry": 2200
    },

    "Sikkim": {
        "Andhra Pradesh": 2800, "Arunachal Pradesh": 1000, "Assam": 600, "Bihar": 1000,
        "Chhattisgarh": 1600, "Goa": 3600, "Gujarat": 3800, "Haryana": 1800,
        "Himachal Pradesh": 1600, "Jharkhand": 1400, "Karnataka": 4000, "Kerala": 4500,
        "Madhya Pradesh": 2600, "Maharashtra": 3900, "Manipur": 1200, "Meghalaya": 1000,
        "Mizoram": 1200, "Nagaland": 1200, "Odisha": 1600, "Punjab": 1800, "Rajasthan": 2200,
        "Tamil Nadu": 4200, "Telangana": 2800, "Tripura": 1200, "Uttar Pradesh": 1400,
        "Uttarakhand": 1600, "West Bengal": 800, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 1600, "Dadra and Nagar Haveli and Daman and Diu": 4000, "Delhi": 1600,
        "Jammu and Kashmir": 2000, "Ladakh": 1800, "Lakshadweep": 4800, "Puducherry": 4000
    },

    "Tamil Nadu": {
        "Andhra Pradesh": 700, "Arunachal Pradesh": 5000, "Assam": 4800, "Bihar": 3600,
        "Chhattisgarh": 2800, "Goa": 1600, "Gujarat": 3000, "Haryana": 3000,
        "Himachal Pradesh": 3500, "Jharkhand": 2400, "Karnataka": 700, "Kerala": 700,
        "Madhya Pradesh": 1600, "Maharashtra": 1300, "Manipur": 5000, "Meghalaya": 4800,
        "Mizoram": 5000, "Nagaland": 4800, "Odisha": 1800, "Punjab": 3000, "Rajasthan": 3000,
        "Sikkim": 4200, "Telangana": 1200, "Tripura": 5000, "Uttar Pradesh": 3200,
        "Uttarakhand": 3500, "West Bengal": 2400, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 3500, "Dadra and Nagar Haveli and Daman and Diu": 3000, "Delhi": 3200,
        "Jammu and Kashmir": 3500, "Ladakh": 3800, "Lakshadweep": 700, "Puducherry": 200
    },

    "Telangana": {
        "Andhra Pradesh": 200, "Arunachal Pradesh": 3700, "Assam": 3400, "Bihar": 2600,
        "Chhattisgarh": 900, "Goa": 1300, "Gujarat": 2000, "Haryana": 2600,
        "Himachal Pradesh": 3000, "Jharkhand": 1800, "Karnataka": 500, "Kerala": 900,
        "Madhya Pradesh": 1000, "Maharashtra": 900, "Manipur": 3700, "Meghalaya": 3600,
        "Mizoram": 4000, "Nagaland": 3800, "Odisha": 900, "Punjab": 2100, "Rajasthan": 1800,
        "Sikkim": 2800, "Tamil Nadu": 1200, "Tripura": 3700, "Uttar Pradesh": 1400,
        "Uttarakhand": 2000, "West Bengal": 1200, "Andaman and Nicobar Islands": 4000,
        "Chandigarh": 2600, "Dadra and Nagar Haveli and Daman and Diu": 2000, "Delhi": 2600,
        "Jammu and Kashmir": 3000, "Ladakh": 3300, "Lakshadweep": 900, "Puducherry": 1200
    },

    "Tripura": {
        "Andhra Pradesh": 3600, "Arunachal Pradesh": 1600, "Assam": 700, "Bihar": 2000,
        "Chhattisgarh": 3000, "Goa": 4200, "Gujarat": 4500, "Haryana": 3200,
        "Himachal Pradesh": 3600, "Jharkhand": 2000, "Karnataka": 3800, "Kerala": 4300,
        "Madhya Pradesh": 3500, "Maharashtra": 4200, "Manipur": 600, "Meghalaya": 1000,
        "Mizoram": 900, "Nagaland": 800, "Odisha": 2600, "Punjab": 3700, "Rajasthan": 4000,
        "Sikkim": 1200, "Tamil Nadu": 5000, "Telangana": 3700, "Uttar Pradesh": 3200,
        "Uttarakhand": 3600, "West Bengal": 1400 
    },
    "West Bengal": {
        "Andhra Pradesh": 1600, "Arunachal Pradesh": 1400, "Assam": 800, "Bihar": 600,
        "Chhattisgarh": 1400, "Goa": 3200, "Gujarat": 2800, "Haryana": 2000,
        "Himachal Pradesh": 2200, "Jharkhand": 600, "Karnataka": 2600, "Kerala": 3200,
        "Madhya Pradesh": 1800, "Maharashtra": 2600, "Manipur": 1600, "Meghalaya": 1000,
        "Mizoram": 1400, "Nagaland": 1400, "Odisha": 800, "Punjab": 2000, "Rajasthan": 2200,
        "Sikkim": 800, "Tamil Nadu": 2400, "Telangana": 1200, "Tripura": 1400, "Uttar Pradesh": 1200,
        "Uttarakhand": 1400, "Andaman and Nicobar Islands": 3500, "Chandigarh": 2200,
        "Dadra and Nagar Haveli and Daman and Diu": 3000, "Delhi": 2000, "Jammu and Kashmir": 2400,
        "Ladakh": 2800, "Lakshadweep": 3200, "Puducherry": 2400
    },

    "Andaman and Nicobar Islands": {
        "Andhra Pradesh": 1200, "Arunachal Pradesh": 4200, "Assam": 3600, "Bihar": 3200,
        "Chhattisgarh": 3000, "Goa": 4000, "Gujarat": 4800, "Haryana": 4200,
        "Himachal Pradesh": 4400, "Jharkhand": 3000, "Karnataka": 3800, "Kerala": 4000,
        "Madhya Pradesh": 3800, "Maharashtra": 4000, "Manipur": 4200, "Meghalaya": 4200,
        "Mizoram": 4200, "Nagaland": 4200, "Odisha": 3000, "Punjab": 4200, "Rajasthan": 4200,
        "Sikkim": 4200, "Tamil Nadu": 4200, "Telangana": 4000, "Tripura": 4000, "Uttar Pradesh": 4200,
        "Uttarakhand": 4200, "West Bengal": 3500, "Chandigarh": 4200, "Dadra and Nagar Haveli and Daman and Diu": 4800,
        "Delhi": 4200, "Jammu and Kashmir": 4500, "Ladakh": 4700, "Lakshadweep": 1200, "Puducherry": 4200
    },

    "Chandigarh": {
        "Andhra Pradesh": 1800, "Arunachal Pradesh": 3700, "Assam": 3200, "Bihar": 2000,
        "Chhattisgarh": 1400, "Goa": 2600, "Gujarat": 1500, "Haryana": 200,
        "Himachal Pradesh": 300, "Jharkhand": 1600, "Karnataka": 2600, "Kerala": 3000,
        "Madhya Pradesh": 1100, "Maharashtra": 2000, "Manipur": 3700, "Meghalaya": 3200,
        "Mizoram": 3800, "Nagaland": 3700, "Odisha": 2200, "Punjab": 200, "Rajasthan": 800,
        "Sikkim": 1600, "Tamil Nadu": 3500, "Telangana": 2600, "Tripura": 3700, "Uttar Pradesh": 700,
        "Uttarakhand": 400, "West Bengal": 2200, "Andaman and Nicobar Islands": 4200,
        "Dadra and Nagar Haveli and Daman and Diu": 2600, "Delhi": 400, "Jammu and Kashmir": 700,
        "Ladakh": 1200, "Lakshadweep": 3000, "Puducherry": 2600
    },

    "Dadra and Nagar Haveli and Daman and Diu": {
        "Andhra Pradesh": 1200, "Arunachal Pradesh": 4700, "Assam": 4200, "Bihar": 3200,
        "Chhattisgarh": 1600, "Goa": 200, "Gujarat": 200, "Haryana": 2600,
        "Himachal Pradesh": 2800, "Jharkhand": 2600, "Karnataka": 1200, "Kerala": 1600,
        "Madhya Pradesh": 1400, "Maharashtra": 200, "Manipur": 4700, "Meghalaya": 4200,
        "Mizoram": 4700, "Nagaland": 4500, "Odisha": 1800, "Punjab": 2600, "Rajasthan": 1200,
        "Sikkim": 4000, "Tamil Nadu": 3000, "Telangana": 2000, "Tripura": 4700, "Uttar Pradesh": 2600,
        "Uttarakhand": 2800, "West Bengal": 3000, "Andaman and Nicobar Islands": 4800,
        "Chandigarh": 2600, "Delhi": 2600, "Jammu and Kashmir": 3000, "Ladakh": 3300,
        "Lakshadweep": 1600, "Puducherry": 3000
    },

    "Delhi": {
        "Andhra Pradesh": 1800, "Arunachal Pradesh": 3600, "Assam": 3200, "Bihar": 1200,
        "Chhattisgarh": 1400, "Goa": 2600, "Gujarat": 1200, "Haryana": 200,
        "Himachal Pradesh": 400, "Jharkhand": 1600, "Karnataka": 2600, "Kerala": 3000,
        "Madhya Pradesh": 1100, "Maharashtra": 2000, "Manipur": 3600, "Meghalaya": 3200,
        "Mizoram": 4200, "Nagaland": 3800, "Odisha": 1800, "Punjab": 400, "Rajasthan": 800,
        "Sikkim": 1600, "Tamil Nadu": 3500, "Telangana": 2600, "Tripura": 3600, "Uttar Pradesh": 600,
        "Uttarakhand": 400, "West Bengal": 2000, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 400, "Dadra and Nagar Haveli and Daman and Diu": 2600,
        "Jammu and Kashmir": 700, "Ladakh": 1200, "Lakshadweep": 3000, "Puducherry": 2600
    },

    "Jammu and Kashmir": {
        "Andhra Pradesh": 2500, "Arunachal Pradesh": 3700, "Assam": 3600, "Bihar": 2600,
        "Chhattisgarh": 2400, "Goa": 3000, "Gujarat": 2800, "Haryana": 700,
        "Himachal Pradesh": 500, "Jharkhand": 2400, "Karnataka": 3200, "Kerala": 3600,
        "Madhya Pradesh": 2000, "Maharashtra": 2800, "Manipur": 3700, "Meghalaya": 3600,
        "Mizoram": 4000, "Nagaland": 3700, "Odisha": 2800, "Punjab": 700, "Rajasthan": 1200,
        "Sikkim": 1800, "Tamil Nadu": 4000, "Telangana": 3000, "Tripura": 3700, "Uttar Pradesh": 1200,
        "Uttarakhand": 700, "West Bengal": 2400, "Andaman and Nicobar Islands": 4500,
        "Chandigarh": 700, "Dadra and Nagar Haveli and Daman and Diu": 3000,
        "Delhi": 700, "Ladakh": 600, "Lakshadweep": 3600, "Puducherry": 3000
    },

    "Ladakh": {
        "Andhra Pradesh": 3000, "Arunachal Pradesh": 3900, "Assam": 4000, "Bihar": 3200,
        "Chhattisgarh": 2800, "Goa": 3600, "Gujarat": 3300, "Haryana": 1200,
        "Himachal Pradesh": 800, "Jharkhand": 3000, "Karnataka": 3600, "Kerala": 4000,
        "Madhya Pradesh": 2400, "Maharashtra": 3200, "Manipur": 3900, "Meghalaya": 3800,
        "Mizoram": 4000, "Nagaland": 3900, "Odisha": 3200, "Punjab": 1200, "Rajasthan": 1600,
        "Sikkim": 2000, "Tamil Nadu": 4200, "Telangana": 3400, "Tripura": 3900, "Uttar Pradesh": 1600,
        "Uttarakhand": 1200, "West Bengal": 2800, "Andaman and Nicobar Islands": 4700,
        "Chandigarh": 1200, "Dadra and Nagar Haveli and Daman and Diu": 3300,
        "Delhi": 1200, "Jammu and Kashmir": 600, "Lakshadweep": 4000, "Puducherry": 3400
    },

    "Lakshadweep": {
        "Andhra Pradesh": 1200, "Arunachal Pradesh": 5200, "Assam": 5000, "Bihar": 4800,
        "Chhattisgarh": 4000, "Goa": 1400, "Gujarat": 1600, "Haryana": 3000,
        "Himachal Pradesh": 3200, "Jharkhand": 4200, "Karnataka": 800, "Kerala": 600,
        "Madhya Pradesh": 3200, "Maharashtra": 1400, "Manipur": 5200, "Meghalaya": 5000,
        "Mizoram": 5200, "Nagaland": 5000, "Odisha": 4000, "Punjab": 3000, "Rajasthan": 3200,
        "Sikkim": 4700, "Tamil Nadu": 600, "Telangana": 1800, "Tripura": 5000, "Uttar Pradesh": 3200,
        "Uttarakhand": 3200, "West Bengal": 3200, "Andaman and Nicobar Islands": 1200,
        "Chandigarh": 3000, "Dadra and Nagar Haveli and Daman and Diu": 1600,
        "Delhi": 3000, "Jammu and Kashmir": 3600, "Ladakh": 4000, "Puducherry": 600
    },

    "Puducherry": {
        "Andhra Pradesh": 500, "Arunachal Pradesh": 4900, "Assam": 4700, "Bihar": 4500,
        "Chhattisgarh": 3200, "Goa": 3000, "Gujarat": 2800, "Haryana": 2600,
        "Himachal Pradesh": 3000, "Jharkhand": 3000, "Karnataka": 1400, "Kerala": 1200,
        "Madhya Pradesh": 2800, "Maharashtra": 2000, "Manipur": 4900, "Meghalaya": 4700,
        "Mizoram": 4900, "Nagaland": 4700, "Odisha": 3200, "Punjab": 2600, "Rajasthan": 2600,
        "Sikkim": 4000, "Tamil Nadu": 600, "Telangana": 1200, "Tripura": 4700, "Uttar Pradesh": 2600,
        "Uttarakhand": 3000, "West Bengal": 2400, "Andaman and Nicobar Islands": 4200,
        "Chandigarh": 2600, "Dadra and Nagar Haveli and Daman and Diu": 3000,
        "Delhi": 2600, "Jammu and Kashmir": 3000, "Ladakh": 3400, "Lakshadweep": 600
    }
}
# Function to get distance
def get_distance(state1, state2):
    if state1 == state2:
        return 0
    if state1 in distances and state2 in distances[state1]:
        return distances[state1][state2]
    elif state2 in distances and state1 in distances[state2]:
        return distances[state2][state1]
    else:
        return None  # unknown distance
