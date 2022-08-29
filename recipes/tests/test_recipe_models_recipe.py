from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Recipe

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field,'T' * (max_length + 1) )
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
        
    def make_recipe_no_default(self):
        recipe = Recipe(
            category=self.make_category(name='Test default category'), 
            author=self.make_author(username='Newuser'), 
            title='title', 
            description='Recipe description',
            preparation_time='5', 
            slug='recipe-slug-new', 
            preparation_time_unit='Minutos', 
            servings='4', 
            servings_unit='pessoas', 
            preparation_steps='lalalalala',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.preparation_steps_is_html)

    def test_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.is_published)

    def test_recipe_string_representation(self):
        recipe_title = "Testing Representation"
        self.recipe.title = recipe_title 
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), recipe_title, msg=f'the string representatin must be 'f'"{recipe_title}" but "{str(self.recipe)}" was received.')
