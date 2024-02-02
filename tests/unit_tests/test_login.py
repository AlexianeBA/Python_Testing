from server import app

class TestLogin:
    client = app.test_client()
    
    def test_login(self):
        result = self.client.get('/')
        assert result.status_code == 200