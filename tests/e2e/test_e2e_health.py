import requests


def test_health_endpoint_e2e():
    """End-to-end check that the running API responds correctly at /health."""
    base_url = "http://localhost:8000"
    response = requests.get(f"{base_url}/health", timeout=5)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
