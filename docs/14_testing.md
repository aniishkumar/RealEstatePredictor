# Testing
`tests/test_api.py` is an integration-focused API suite: it verifies health, successful response structure/type, invalid request validation, and ability to load artifacts. It does not assert an invented exact price. Tests skip before training because a model-backed API cannot truthfully pass without the artifact. Run `python -m ml.train` then `pytest`.
