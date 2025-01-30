from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify
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
        self.assertEqual(self.post.get_absolute_url(), 
                                f"/post/{slugify(self.post.title)}/")

    def test_post_createview(self):
        response = self.client.post(
            reverse('post_new'),
            {
                'title': "New title",
                'body': 'New text',
                'author': self.user.id
            }

        )
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(Post.objects.get(id=2).title, 
        #                     'New title')
        self.assertEqual(Post.objects.last().title, 
                            'New title')
        self.assertEqual(Post.objects.last().body, 
                            'New text')
        self.assertEqual(Post.objects.last().author,
                            self.user)
    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args=[self.post.id]),
            {
                'title': 'updated title',
                'body': 'updated text'
            }
        ) 
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 
                            'updated title')
        self.assertEqual(Post.objects.last().body, 
                            'updated text')


    def test_post_deleteview(self):
        response = self.client.post(reverse('post_delete',
                                        args=['1']))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(bool(Post.objects.all()))
        

 


