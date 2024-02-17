from server import app
import server


class TestDeductPoints:
    client = app.test_client()
    competition = [
        {"name": "test", "date": "2024-02-10 15:00:00", "numberOfPlaces": "22"}
    ]
    club = [{"name": "Test", "email": "test@test.fr", "points": "5"}]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club

    def test_deduct_points(self):
        club_points_before_reserved = int(self.club[0]["points"])
        places_booked = 2
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"],
            },
        )
        assert result.status_code == 200
        assert "Great-booking complete!" in result.data.decode()
        assert (
            int(self.club[0]["points"]) == club_points_before_reserved - places_booked
        )