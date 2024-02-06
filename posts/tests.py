from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = "testuser",
            email = "testemail@email.com",
            password = "testpass123"
        )
        cls.post = Post.objects.create(
            author = cls.user,
            title = "test title",
            body = "This is test body",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "test title")
        self.assertEqual(self.post.body, "This is test body")
        self.assertEqual(str(self.post), "test title")
