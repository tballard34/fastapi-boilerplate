import json

import pytest

from app.endpoints.health import health


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok_status():
    """Ensure health endpoint returns correct status and response format."""
    response = await health()

    assert response.status_code == 200

    # Parse the JSON content
    content = json.loads(response.body)
    assert content == {"status": "ok"}
