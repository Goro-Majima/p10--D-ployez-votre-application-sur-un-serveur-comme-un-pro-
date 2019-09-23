#!/bin/bash
#pylint: disable=W0223, C0413, C0103
""" Python file used once in order to populate data from OFF API """
import os
import requests as req
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "purbeurre.settings")
import django
django.setup()
from django.core.management.base import BaseCommand
from grocery.models import Category, Product


class Command(BaseCommand):
    """ Fill categary table then use it as a foreign key in product table """
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
        categ = Category.objects.get(name=name)
        count = 0
        for i in range(1, 20):
            url = ("https://fr.openfoodfacts.org/category/"+ name + "/"+ str(i) + ".json")
            extract = req.get(url)
            response_data = extract.json()
            for products in response_data["products"]:
                if "product_name" in products:
                    if "nutrition_grade_fr" in products:
                        if "image_url" in products:
                            if "url" in products:
                                if "image_nutrition_url" in products:
                                    product = Product.objects.filter(name=products["product_name"], category=categ)
                                    if product.exists():
                                        product.update(nutrigrade=products["nutrition_grade_fr"],\
                                            image=products["image_url"],\
                                            url=products["url"],\
                                            nutrient=products["image_nutrition_url"])
                                        print("produit mis à jour")
                                        print(product)
