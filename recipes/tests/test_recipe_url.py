
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

    def test_recipe_category_url_is_correct(self):
        url = reverse("recipes:category", kwargs={'category_id':1})
        self.assertEqual(url, '/recipes/category/1/')

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



    def test_recipe_detail_url_is_correct(self):
        url = reverse("recipes:recipe", kwargs={'id':1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_detail_view_returns_status_code_404_if_no_recipe(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={'id':1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_recipes(self):
        needed_title = 'This is a detail page - and loads only one recipe'
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse("recipes:recipe", kwargs={'id':1,}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
    
    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        recipe  = self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:recipe",  kwargs={'id':recipe.id,}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_url_is_Correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
