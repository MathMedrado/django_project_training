from urllib import response

from django.test import TestCase  # deriva da classe padrão do django unit test
from django.urls import resolve, reverse
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


# Create your tests here.
class RecipeCategoryViewsTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404_if_no_recipe(self):
        response = self.client.get(reverse("recipes:category", kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse("recipes:category", args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:category", kwargs={'category_id': recipe.category.id}))
        self.assertEqual(response.status_code, 404)
