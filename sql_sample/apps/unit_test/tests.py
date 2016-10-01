from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from apps.models.blog import Blog
from django.contrib.auth.models import User


class AnimalTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(name="lion")
        Blog.objects.create(name="cat")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Blog.objects.get(name="lion")
        cat = Blog.objects.get(name="cat")
        self.assertEqual(lion.name, 'lion')
        self.assertEqual(cat.name, 'cat')


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='duizhang', email="dui_zhang@163.com", password="123456")

    def testUser(self):
        '''test'''
        u = User.objects.get(username='duizhang')
        self.assertEqual(u.username, 'duizhang')
        self.assertEqual(u.email, 'dui_zhang@163.com')

    # def testTrue(self):
    #     '''test true'''
    #     self.assertTrue('')


