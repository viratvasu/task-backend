from django.test import TestCase
from application.models import UserProfile, BlogMetadata


class SimpleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    # Model Testing
    def create_user(self, name="TestUser2"):
        return UserProfile.objects.create(name=name)

    def create_blog(self, user_obj, title="Test Title", body="test body"):
        return BlogMetadata.objects.create(user=user_obj, title=title, body=body)

    def test_user(self):
        user = self.create_user()
        self.assertEqual("TestUser2", user.name)

    def test_blog(self):
        user = self.create_user()
        blob_obj = self.create_blog(user)
        self.assertEqual("Test Title", blob_obj.title)

    # Urls/views testing
    def test_all(self):
        response = self.client.get('/get_all/')
        self.assertEqual(response.status_code, 401)
