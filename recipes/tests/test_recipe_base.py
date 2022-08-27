from django.test import TestCase  # deriva da classe padrão do django unit test
from django.urls import reverse
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = self.make_category()
        author = self.make_author()
        recipe =  Recipe.objects.create(
            category=category, 
            author=author, 
            title='title', 
            description='Recipe description',
            preparation_time='5', 
            slug='recipe-slug', 
            preparation_time_unit='Minutos', 
            servings='4', 
            servings_unit='pessoas', 
            preparation_steps='lalalalala',
            preparation_steps_is_html=False,
            is_published=True)

        return super().setUp()
    
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self, 
        first_name='user', 
        last_name='name', 
        username='username', 
        password='123456', 
        email='username@gmail.com'
    ):
        return User.objects.create_user(
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
            password=password, 
            email=email)

    def make_recipe(
        self,
        category=category, 
        author=author, 
        title='title', 
        description='Recipe description',
        preparation_time='5', 
        slug='recipe-slug', 
        preparation_time_unit='Minutos', 
        servings='4', 
        servings_unit='pessoas', 
        preparation_steps='lalalalala',
        preparation_steps_is_html=False,
        is_published=True
    ):
        return Recipe.objects.create(
            category=category, 
            author=author, 
            title=title, 
            description=description,
            preparation_time=preparation_time, 
            slug=slug, 
            preparation_time_unit=preparation_time_unit, 
            servings=servings, 
            servings_unit=servings_unit, 
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published )