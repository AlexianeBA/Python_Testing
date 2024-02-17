from server import app
import server


class TestCompetitionPassed:
    client = app.test_client()
    competition = [
        {"name": "test", "date": "2023-12-10 15:00:00", "numberOfPlaces": "22"}
    ]
    club = [{"name": "Test", "email": "test@test.fr", "points": "20"}]
    places_booked = [{"competition": "Test", "booked": [13, "Test"]}]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club
        server.places_booked = self.places_booked

    def test_purchase_places_for_past_competition(self):
    
        booked = 13

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"],
            },
        )
    
        assert result.status_code == 200
