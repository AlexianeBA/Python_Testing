from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def showSummary(self):
        self.client.post("/showSummary")

    @task
    def purchasePlaces(self):
        self.client.post("/purchasePlaces")

    @task
    def book(self):
        self.client.get("/book/Spring Festival/Simply Lift")

    @task
    def logout(self):
        self.client.get("/logout")
