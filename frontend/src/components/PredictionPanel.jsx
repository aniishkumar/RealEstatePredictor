function formatValue(value) { return new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(value); }

export default function PredictionPanel({ result, values, error }) {
  return <aside className="prediction" aria-live="polite"><span className="eyebrow">Model output</span>
    {!result && !error && <><h2>Estimated property value</h2><p className="empty">Enter property details to generate an estimated value.</p></>}
    {error && <><h2>Prediction unavailable</h2><p className="error-block">{error}</p><p>Verify that the API is running and try again.</p></>}
    {result && <><h2>Estimated property value</h2><output>{formatValue(result.predicted_price)}</output><p>Model estimate based on the submitted characteristics.</p>
      <dl><div><dt>Model</dt><dd>{result.model_name}</dd></div><div><dt>Version</dt><dd>{result.model_version}</dd></div><div><dt>House age</dt><dd>{values.house_age} years</dd></div><div><dt>Avg. rooms</dt><dd>{values.average_rooms}</dd></div></dl><p className="disclaimer">{result.disclaimer}</p></>}
  </aside>;
}
