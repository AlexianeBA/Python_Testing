from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def purchasePlaces(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": "1",
                "club": "Simply Lift",
                "competition": "Spring Festival",
            },
        )

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Iron%20Temple")

    @task
    def logout(self):
        self.client.get("/logout")

    @task
    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})
