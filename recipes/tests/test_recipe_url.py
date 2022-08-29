
from unicodedata import category

from django.urls import resolve, reverse
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase

# Create your tests here.



class RecipeURLSTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    def test_the_pytest_is_ok(self):
        assert 2 == 2, 'dois igual a dois'

    def test_recipe_category_url_is_correct(self):
        url = reverse("recipes:category", kwargs={'category_id':1})
        self.assertEqual(url, '/recipes/category/1/')


