import server
from server import app

class TestAvailableEmailOrUnknowEmail:
    client = app.test_client()
    
    def test_available_email(self):
        result = self.client.post("/showSummary", data={"email": server.clubs[0]["email"]})
        assert result.status_code == 200
        
    def test_unknow_email(self):
        result = self.client.post("/showSummary", data={"email": "abcd"})
        assert result.status_code == 401