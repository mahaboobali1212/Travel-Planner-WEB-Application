// ========== main.js ==========
// Small UX helpers for date handling in your form

document.addEventListener("DOMContentLoaded", () => {
  const startInput = document.querySelector('input[name="start_date"]');
  const endInput = document.querySelector('input[name="end_date"]');
  const daysInput = document.querySelector('input[name="days"]');

  if (startInput && endInput && daysInput) {
    const recalcDays = () => {
      const startVal = startInput.value;
      const endVal = endInput.value;

      if (!startVal || !endVal) {
        daysInput.value = "";
        return;
      }

      const startDate = new Date(startVal);
      const endDate = new Date(endVal);

      if (isNaN(startDate) || isNaN(endDate)) {
        daysInput.value = "";
        return;
      }

      // Calculate difference in days (inclusive)
      const diffTime = endDate - startDate;
      const diffDays = Math.max(1, Math.round(diffTime / (1000 * 60 * 60 * 24)) + 1);

      daysInput.value = diffDays;
    };

    startInput.addEventListener("change", recalcDays);
    endInput.addEventListener("change", recalcDays);
  } else {
    console.warn("Date or days input fields not found in the DOM.");
  }
});
