const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function requestPrediction(input) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10000);
  try {
    const response = await fetch(`${API_URL}/predict`, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input), signal: controller.signal,
    });
    const body = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(body.detail || "Unable to generate a prediction right now.");
    return body;
  } catch (error) {
    if (error.name === "AbortError") throw new Error("The request timed out. Check that the API is running.");
    throw error;
  } finally { clearTimeout(timeout); }
}
