import { useState } from "react";
import PropertyForm, { defaults } from "./components/PropertyForm";
import PredictionPanel from "./components/PredictionPanel";
import { requestPrediction } from "./services/api";

export default function App() {
  const [values, setValues] = useState(defaults), [errors, setErrors] = useState({});
  const [busy, setBusy] = useState(false), [result, setResult] = useState(null), [error, setError] = useState("");
  const change = (event) => setValues({ ...values, [event.target.name]: event.target.value });
  async function submit(event) {
    event.preventDefault(); const numeric = Object.fromEntries(Object.entries(values).map(([key, value]) => [key, Number(value)]));
    const nextErrors = Object.fromEntries(Object.entries(numeric).filter(([, value]) => !Number.isFinite(value)).map(([key]) => [key, "Enter a valid number."]));
    if (Object.keys(nextErrors).length) return setErrors(nextErrors);
    setErrors({}); setBusy(true); setError(""); setResult(null);
    try { setResult(await requestPrediction(numeric)); } catch (err) { setError(err.message); } finally { setBusy(false); }
  }
  return <><header><div className="brand">EstateValue</div><div>Residential property valuation</div></header><main><section className="intro"><span className="eyebrow">Valuation workspace</span><h1>Estimate a California home value</h1><p>Use documented housing and location characteristics to generate a model estimate.</p></section><div className="workspace"><section className="form-panel"><PropertyForm values={values} errors={errors} busy={busy} onChange={change} onSubmit={submit} /></section><PredictionPanel result={result} values={values} error={error} /></div></main><footer>EstateValue · Model estimates are not certified valuations.</footer></>;
}
