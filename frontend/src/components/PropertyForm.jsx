const fields = [
  ["median_income", "Median income", "In tens of thousands of USD", 3.87, 0.01, 20],
  ["house_age", "House age", "Years", 28, 0, 100],
  ["average_rooms", "Average rooms", "Rooms per household", 5.43, 0.1, 100],
  ["average_bedrooms", "Average bedrooms", "Bedrooms per household", 1.1, 0.1, 50],
  ["population", "Population", "Local census block population", 1425, 0, 100000],
  ["average_occupancy", "Average occupancy", "People per household", 3.07, 0.1, 100],
  ["latitude", "Latitude", "California range: 32–43", 34.21, 32, 43],
  ["longitude", "Longitude", "California range: −125 to −114", -118.45, -125, -114],
];

export const defaults = Object.fromEntries(fields.map(([key, , , value]) => [key, value]));

export default function PropertyForm({ values, errors, busy, onChange, onSubmit }) {
  return <form onSubmit={onSubmit} noValidate>
    <div className="section-title"><h2>Property inputs</h2><p>Features available in the California Housing dataset.</p></div>
    <div className="field-grid">{fields.map(([key, label, hint, , min, max]) => <div className="field" key={key}>
      <label htmlFor={key}>{label}</label><input id={key} name={key} type="number" value={values[key]} min={min} max={max} step="any" onChange={onChange} aria-describedby={`${key}-hint ${errors[key] ? `${key}-error` : ""}`} />
      <small id={`${key}-hint`}>{hint}</small>{errors[key] && <span className="error" id={`${key}-error`} role="alert">{errors[key]}</span>}
    </div>)}</div>
    <button className="submit" disabled={busy}>{busy ? "Estimating…" : "Estimate value"}</button>
  </form>;
}
