#pylint: disable=C0103, W0612
""" Python testing file checking each page returns the correct response"""
from django.test import TestCase
from django.urls import reverse
# from django.contrib.auth.models import User
from grocery.models import Category, Product
from django.contrib.auth.models import User
from users.models import Profile

class DataFilledTestCase(TestCase):
    """ fill Category with list """
    def test_product_filled(self):
        """ Method use to fill both categories and products """
        CATEGORYNAME = [
            "Pizzas",
            "Conserves",
            "Fromages",
            "Boissons",
            "Snacks sucrés",
            "Viandes",
            "Charcuteries",
            "Epicerie",
            "Desserts",
            "Surgelés",
            "Sauces",
            "Biscuits",
            "Chocolats",
            "Gâteaux",
            "Confitures",
            "Apéritif",
            "Condiments",
            "Yaourts",
            "Pains",
            "Huiles",
        ]
        for name in CATEGORYNAME:
            categ = Category.objects.create(name=name)
        categ = Category.objects.get(name='Confitures')
        product = Product.objects.create(name='nutella', nutrigrade='a', image='url.htt',\
        url='url.htt', nutrient='url.htt', category=categ)
        products = Product.objects.all()
        self.assertTrue(products.exists)

# Homepage
class IndexPageTestCase(TestCase):
    """ Class Test that the function returns the home page with response 200 """
    def test_index_page(self):
        """ Test that the function returns the home page with response 200 """
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

# Mention page
class MentionPageTestCase(TestCase):
    """ Class Test that the function returns the mention page with response 200 """
    def test_mention_page(self):
        """ Test that the function returns the mention page with response 200 """
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200)

# # results page
# class ResultsPageTestCase(TestCase):
#     """ Class Test that the function returns the results page with response 200 """
#     def setUp(self):
#         categ = Category.objects.create(name='pate')
#         product = Product.objects.create(name='nutella', nutrigrade='a', image='url.htt',\
#         url='url.htt', nutrient='url.htt', category=categ)
#         self.product = Product.objects.get(name='nutella')
#     def test_results_page(self):
#         """ Test that the function returns the results page with response 200 """
#         product = self.product.name
#         response = self.client.get(reverse('results', args=(product,)))
#         self.assertEqual(response.status_code, 200)

# Detail page
class DetailPageTestCase(TestCase):
    """ Create an object and its instance """
    def setUp(self):
        categ = Category.objects.create(name='pate')
        product = Product.objects.create(name='nutella', nutrigrade='a', image='url.htt',\
        url='url.htt', nutrient='url.htt', category=categ)
        self.product = Product.objects.get(name='nutella')

    # test that detail page returns 200 if the item exists
    def test_detail_page_returns_200(self):
        """ Test that the function returns the detail page with response 200 """
        product = self.product.id
        response = self.client.get(reverse('detail', args=(product,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns 404 if the item exists
    def test_detail_page_returns_404(self):
        """ Test that the function returns the error page with response 404 """
        product = self.product.id + 1000
        response = self.client.get(reverse('detail', args=(product,)))
        self.assertEqual(response.status_code, 404)

class ModelTests(TestCase):
    """ Test string returns """

    def test_str_Category(self):
        """ test str method for the model Category """
        categ = Category.objects.create(name='Pate')
        self.assertIs(categ.__str__(), "Pate")

    def test_str_product(self):
        """ test str method for the model Product """
        categ = Category.objects.create(name='pate')
        product = Product.objects.create(name="Coca", nutrigrade='a', image='url.htt',\
        url='url.htt', nutrient='url.htt', category=categ)
        self.assertIs(product.__str__(), "Coca")

