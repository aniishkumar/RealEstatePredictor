# API design
`GET /health` reports ready only with metadata; `/model-info` reports actual saved metadata; `POST /predict` returns a typed response and generic 503/500 messages rather than stack traces. CORS permits the local Vite origin. Production changes: environment-configured origins, authentication, rate limits, HTTPS, structured logs, monitoring and artifact storage.

At 1,000 rps: use stateless API replicas behind a load balancer, each preloading a compatible model; add autoscaling, latency/error dashboards, request limits and a dedicated model-serving tier if needed.
