from django.test import TestCase  # deriva da classe padrão do django unit test
from django.urls import reverse


# Create your tests here.
class RecipeURLSTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 2 == 2, 'Um não é igual a dois'

    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse("recipes:category", kwargs={'category_id':1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse("recipes:recipe", kwargs={'id':1})
        self.assertEqual(url, '/recipes/1/')
