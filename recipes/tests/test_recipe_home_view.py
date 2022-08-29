from urllib import response

from django.test import TestCase  # deriva da classe padrão do django unit test
from django.urls import resolve, reverse
from recipes import views
from recipes.tests.test_recipe_base import RecipeTestBase


# Create your tests here.
class RecipeViewsTest(RecipeTestBase):
    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, '/')
    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)


    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn('No recipes found here', response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        #need a recipe to this test
        self.make_recipe(author_data={'first_name':"mathew"})
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
        #check if recipe exist
        self.assertIn('title', content)
        self.assertIn('5   Minutos', content)
        self.assertIn('mathew', content)

        self.assertEqual(len(response_context_recipes), 1)
    
    def test_recipe_home_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:home"))
        self.assertIn('No recipes found here', response.content.decode('utf-8'))
        



