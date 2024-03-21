from django.test import TestCase, Client
from django.urls import reverse
from store.models.product import Products

class CartViewTest(TestCase):

    def setUp(self):
        # Configura um cliente de teste
        self.client = Client()
        # Cria produtos para testar
        self.product1 = Products.objects.create(name='Produto 1', price=100, description='Descrição 1')
        self.product2 = Products.objects.create(name='Produto 2', price=200, description='Descrição 2')
        # Cria uma sessão de carrinho
        session = self.client.session
        session['cart'] = {str(self.product1.id): 1, str(self.product2.id): 2}
        session.save()

    def test_cart_view(self):
        # Faz uma requisição GET para a view Cart
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        # Verifica se o template correto está sendo usado
        self.assertTemplateUsed(response, 'cart.html')
        # Verifica se os produtos estão sendo passados para o template
        products_in_context = list(response.context['products'])
        self.assertIn(self.product1, products_in_context)
        self.assertIn(self.product2, products_in_context)
