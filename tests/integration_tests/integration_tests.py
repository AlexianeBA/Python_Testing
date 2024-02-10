import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_integration(client):
    # Test de connexion avec un e-mail valide
    login_response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert login_response.status_code == 200  # Vérifie que la connexion réussit

    # Test de réservation de places avec un club ayant suffisamment de points
    booking_response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": 5},
    )
    assert booking_response.status_code == 200
    assert b"Great-booking complete!" in booking_response.data

    # Test de réservation de places avec un club n'ayant pas suffisamment de points
    booking_response_insufficient_points = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Iron Temple", "places": 5},
    )
    assert booking_response_insufficient_points.status_code == 200
    assert b"You don't have enough points!" in booking_response_insufficient_points.data

    # Test de réservation de places pour une compétition passée
    booking_response_past_competition = client.post(
        "/purchasePlaces",
        data={"competition": "Fall Classic", "club": "Simply Lift", "places": 5},
    )
    assert booking_response_past_competition.status_code == 200
    assert (
        b"You cannot reserve for this competition because the date has passed"
        in booking_response_past_competition.data
    )