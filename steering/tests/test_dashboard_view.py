from django.test import Client, TestCase
from django.urls import reverse

from steering.models import Project


class SteeringDashboardViewTests(TestCase):
    def test_dashboard_route_resolves_project(self):
        Project.objects.get_or_create(
            key="xeeaisto",
            defaults={"display_name": "XeeAISto"},
        )

        response = Client().get(reverse("steering_dashboard", kwargs={"project_key": "xeeaisto"}))

        assert response.status_code == 200
        assert b"Steering Dashboard" in response.content
        assert b"XeeAISto" in response.content
