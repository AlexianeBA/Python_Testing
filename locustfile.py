from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def book(self):
        self.client.get("/book/Spring Festival/Simply Lift")
