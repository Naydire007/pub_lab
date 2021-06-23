
import unittest
from src.pub import *
from src.drinks import *
from src.customer import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony",100)
        self.drink = Drink("Rum", 2)
        self.customer = Customer("John", 20)
        

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    def test_drink_has_name(self):
        self.assertEqual("Rum", self.drink.name)

    def test_pub_has_drinks(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(1,len(self.pub.drinks))
    
    def test_pub_can_sell_drinks(self):
        self.pub.add_drink(self.drink)
        self.pub.reduce_drink(self.drink)
        self.assertEqual(0,len(self.pub.drinks))
    
    def reduced_customer_wallet(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(18, self.customer.wallet)
    
    def increase_pub_till(self):
        amount_to_increase = self.drink.price
        self.pub.increase_till(amount_to_increase)
        self.assertEqual(102,self.pub.till)
     

