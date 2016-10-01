from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from apps.models.blog import Blog


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
