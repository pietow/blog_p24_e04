from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password='secret',
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):

        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(str(self.post), 'A good title')
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_detail_view(self):
        res = self.client.get('/post/1/')
        self.assertEqual(res.status_code, 200)

    def test_url_exists_at_correct_location_list_view(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)


