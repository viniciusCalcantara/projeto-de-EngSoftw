from django.test import TestCase
from models import Category

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Cria algumas categorias para testar
        Category.objects.create(name="Categoria 1")
        Category.objects.create(name="Categoria 2")
        Category.objects.create(name="Categoria 3")

    def test_category_creation(self):
        # Testa a criação de uma categoria
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, 'Categoria 1')

    def test_get_all_categories(self):
        # Testa se o método get_all_categories retorna todas as categorias
        categories = Category.get_all_categories()
        self.assertEqual(categories.count(), 3)
        category_names = list(categories.values_list('name', flat=True))
        self.assertIn("Categoria 1", category_names)
        self.assertIn("Categoria 2", category_names)
        self.assertIn("Categoria 3", category_names)

    def test_str_method(self):
        # Testa o método __str__ do modelo
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), "Categoria 1")