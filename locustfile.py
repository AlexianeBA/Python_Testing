from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

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
    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def logout(self):
        self.client.get("/logout")
