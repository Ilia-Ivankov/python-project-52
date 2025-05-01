from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="test",
            last_name="test",
            username="TestUser",
            password="password123",
        )

    def test_user_list(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.context)
        users = response.context["users"]
        self.assertTrue(len(users) > 0)
        self.assertContains(response, "TestUser")

    def test_user_create(self):
        registration_url = reverse("user_create")
        response = self.client.post(
            registration_url,
            {
                "first_name": "test2",
                "last_name": "test2",
                "username": "test2user",
                "password1": "123456",
                "password2": "123456",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("login"))

        response = self.client.get(response.url)
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Пользователь успешно зарегистрирован")

    def test_user_update_not_authenticated(self):
        update_url = reverse("user_update", kwargs={"pk": self.user.id})
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

    def test_user_update_authenticated(self):
        update_url = reverse("user_update", kwargs={"pk": self.user.id})
        list_url = reverse("users")
        self.client.login(username=self.user.username, password="password123")

        # Обновление пользователя
        response = self.client.post(update_url, {
            'username': 'bib',
            'first_name': 'test',
            'last_name': 'test',
            'password1': 123,
            'password2': 123
        })
        response = self.client.get(list_url)
        self.assertContains(response, "bib")
        self.assertNotContains(response, "TestUser")

    def test_user_delete_authenticated(self):
        delete_url = reverse('user_delete', kwargs={'pk': self.user.id})
        list_url = reverse("users")
        self.client.login(username=self.user.username, password="password123")
        response = self.client.get(list_url)
        self.assertContains(response, "TestUser")
        response = self.client.post(delete_url)
        self.assertRedirects(response, list_url)
        response = self.client.get(list_url)
        self.assertNotContains(response, "TestUser")

    def test_user_delete_not_authenticated(self):
        delete_url = reverse('user_delete', kwargs={'pk': self.user.id})
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))