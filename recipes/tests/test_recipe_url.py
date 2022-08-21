

from django.test import TestCase  # deriva da classe padrão do django unit test
from django.urls import reverse
from recipes.models import Category, Recipe, User


# Create your tests here.
class RecipeURLSTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 2 == 2, 'dois igual a dois'

    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, '/')

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
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(first_name='user', last_name='name', username='username', password='123456', email='user@gmail.com')
        recipe =  Recipe.objects.create(category=category, author=author, title='title', description='desc',preparation_time='5', slug='slug', 
        preparation_time_unit='minutos', servings='4', servings_unit='pessoas', preparation_steps='lalalalala',preparation_steps_is_html=False,
         is_published=True)
        assert  1 == 1


    def test_recipe_category_url_is_correct(self):
        url = reverse("recipes:category", kwargs={'category_id':1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_category_view_returns_status_code_404_if_no_recipe(self):
        response = self.client.get(reverse("recipes:category", kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)


    def test_recipe_detail_url_is_correct(self):
        url = reverse("recipes:recipe", kwargs={'id':1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_detail_view_returns_status_code_404_if_no_recipe(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={'id':1000}))
        self.assertEqual(response.status_code, 404)




