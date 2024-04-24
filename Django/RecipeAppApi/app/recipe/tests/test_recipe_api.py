import tempfile, os

from PIL import Image

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Ingredient

from recipe.serializers import RecipeSerializer, RecipeDetailSerializer


RECIPE_URL = reverse('recipe:recipe-list')

# /api/recipe/recipes
# /api/recipe/recipes/1/

def image_upload_url(recipe_id):
    '''' return URL for recipe image upload '''
    return reverse('recipe:recipe-upload-image', args=[recipe_id])


def detail_url(recipe_id):
    """ return recipe detail url """
    return reverse('recipe:recipe-detail', args=[recipe_id])


def sample_recipe(user, **params):
    ''' Create and return asample recipe '''
    defaults = {
        'title' : 'Sample Recipe',
        'time_minutes': 10,
        'price': 5.00
    }
    defaults.update(params)

    return Recipe.objects.create(user=user, **defaults)

def sample_tag(user, name='Main course'):
    ''' Create and return asample tag '''
    return Tag.objects.create(user=user, name=name)

def sample_ingredients(user, name='Cinnamon'):
    ''' Create and return asample ingredient '''
    return Ingredient.objects.create(user=user, name=name)


class PublicRecipeApiTests(TestCase):
    ''' test public available recipes API '''

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        ''' Test that login is required for retrieving tags '''
        res = self.client.get(RECIPE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipesApiTests(TestCase):
    ''' test the authorized user recipes API '''

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@recipeapp.com',
            'password123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        ''' test retrieving recipes '''
        sample_recipe(user=self.user)
        sample_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(serializer.data))

    def test_recipes_limited_to_user(self):
        ''' teste that recipes returned are for the authenticated user '''
        user2 = get_user_model().objects.create_user(
            'other@recipeapp.com',
            'password123'
        )
        recipe = sample_recipe(user=user2)
        sample_recipe(user=self.user)

        res = self.client.get(RECIPE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['title'], recipe.title)

    def test_view_recipe_detail(self):
        """ test viewing detail recipe """
        recipe = sample_recipe(user=self.user)
        recipe.tags.add(sample_tag(user=self.user))
        recipe.ingredients.add(sample_ingredients(user=self.user))

        url = detail_url(recipe.id)
        res = self.client.get(url)
        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_create_recipe_with_ingredients(self):
        """ test viewing detail recipe """
        ingredient1 = sample_ingredients(user=self.user, name='Prawns')
        ingredient2 = sample_ingredients(user=self.user, name='Ginger')
        payload = {
            'title': 'Thai prawn red curry',
            'ingredients': [ingredient1.id, ingredient2.id],
            'time_minutes': 20,
            'price': 7.00
        }
        res = self.client.post(RECIPE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients)
        
    def test_partial_update_recipe(self):
        """ test updating a recipe with patch """
        recipe = sample_recipe(user=self.user)
        recipe.tags.add(sample_tag(user=self.user))
        new_tag = sample_tag(user=self.user, name='Curry')
        
        payload = {'title': 'Chicken tikka', 'tags': [new_tag.id]}
        url = detail_url(recipe.id)
        self.client.patch(url, payload)
        
        recipe.refresh_from_db()
        self.assertEqual(recipe.title, payload['title'])
        tags = recipe.tags.all()
        self.assertEqual(len(tags), 1)
        self.assertIn(new_tag, tags)
        
    def test_full_update_recipe(self):
        ''' test updating a recipe with put '''
        recipe = sample_recipe(user=self.user)
        recipe.tags.add(sample_tag(user=self.user))
        payload= {
            'title': 'Spaghetti carbonara',
            'time_minutes': 25,
            'price': 5.00
        }
        url = detail_url(recipe.id)
        self.client.put(url, payload)
        
        recipe.refresh_from_db()
        self.assertEqual(recipe.title, payload['title'])
        self.assertEqual(recipe.time_minutes, payload['time_minutes'])
        self.assertEqual(recipe.price, payload['price'])
        tags = recipe.tags.all()
        self.assertEqual(len(tags), 0)
        
class RecipeImageUploadTests(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@api.com', 'testpass'
        )
        self.client.force_authenticate(self.user)
        self.recipe = sample_recipe(user=self.user)
        
    def tearDown(self):
        self.recipe.image.delete()
        
    def test_upload_image_to_recipe(self):
        ''' Test uploading an email to recipe '''
        url = image_upload_url(self.recipe.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10,10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'image': ntf }, format='multipart')
        
        self.recipe.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(self.recipe.image.path))
    
    def test_upload_image_bad_request(self):
        ''' test uploading an invalid image '''
        url = image_upload_url(self.recipe.id)
        res = self.client.post(url, {'image': 'noimage' }, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_filter_recipes_by_tags(self):
        ''' test returning recipes with specific tags '''
        recipe1 = sample_recipe(user=self.user, title='Thai vegetable curry')
        recipe2 = sample_recipe(user=self.user, title='Aubergini with tahini')
        tag1 = sample_tag(user=self.user, name='Vegan')
        tag2 = sample_tag(user=self.user, name='Vegetarian')
        recipe1.tags.add(tag1)
        recipe2.tags.add(tag2)
        recipe3 = sample_recipe(user=self.user, title='Fish and chips')
        
        res = self.client.get(
            RECIPE_URL,
            { 'tags': f'{tag1.id},{tag2.id}'}
        )
        
        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        serializer3 = RecipeSerializer(recipe3)
        
        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)
        
    def test_filter_recipes_by_ingredients(self):
        ''' test returnning with specific ingredientes '''
        recipe1 = sample_recipe(user=self.user, title='Posh beans on toast')
        recipe2 = sample_recipe(user=self.user, title='Chicken cacciatore')
        ingredient1 = sample_ingredients(user=self.user, name='Feta Cheese')
        ingredient2 = sample_ingredients(user=self.user, name='Chicken')
        recipe1.ingredients.add(ingredient1)
        recipe2.ingredients.add(ingredient2)
        recipe3 = sample_recipe(user=self.user, title='Steak and mushrooms')
    
        res = self.client.get(
            RECIPE_URL,
            { 'ingredients': f'{ingredient1.id},{ingredient2.id}'}
        )
        
        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        serializer3 = RecipeSerializer(recipe3)
        
        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)
        
        