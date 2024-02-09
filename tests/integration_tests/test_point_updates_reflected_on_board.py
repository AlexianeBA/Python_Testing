import server
from server import app


class TestPointsUpdate:
    client = app.test_client()
    competition = [
        {"name": "Test", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"}
    ]

    club = [{"name": "Test", "email": "test@test.fr", "points": "10"}]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club

    def test_points_update(self):
        club_points_before = int(self.club[0]["points"])
        places_booked = 1

        self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"],
            },
        )

        result = self.client.get("/")

        assert result.status_code == 200
