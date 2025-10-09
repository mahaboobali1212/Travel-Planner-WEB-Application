```javascript
// Small UX helpers could go here. Keeping minimal for now.
// Example: auto-calc days based on dates (optional)
document.addEventListener("DOMContentLoaded", () => {
  const start = document.querySelector('input[name="start_date"]');
  const end = document.querySelector('input[name="end_date"]');
  const daysInput = document.querySelector('input[name="days"]');
  if (start && end && daysInput) {
    const recalc = () => {
      if (!start.value || !end.value) return;
      const s = new Date(start.value);
      const e = new Date(end.value);
      const diff = Math.max(1, Math.round((e - s) / (1000*60*60*24)) + 1); // inclusive
      daysInput.value = diff;
    };
    start.addEventListener('change', recalc);
    end.addEventListener('change', recalc);
  }
});
```
