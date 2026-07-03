from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    """Reset in-memory activity state before each test."""
    activities.clear()
    activities.update(deepcopy(BASE_ACTIVITIES))


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
