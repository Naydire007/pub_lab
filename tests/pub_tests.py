
import unittest
from src.pub import *
from src.drinks import *
from src.customer import *
from src.food import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony",100)
        self.drink = Drink("Rum", 2, 1)
        self.customer = Customer("John", 20, 35)
        self.customer2 = Customer("Juan",50,16)
        self.food = Food("chips", 1, 1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    def test_drink_has_name(self):
        self.assertEqual("Rum", self.drink.name)

    def test_pub_has_drinks(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(1, self.pub.stock_count(self.drink))
    
    def test_pub_can_sell_drinks(self):
        self.pub.add_drink(self.drink)
        self.pub.reduce_drink(self.drink)
        self.assertEqual(0,self.pub.stock_count(self.drink))
    
    def test_reduced_customer_wallet(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(18, self.customer.wallet)
    
    def test_increase_pub_till(self):
        amount_to_increase = self.drink.price
        self.pub.increase_till(amount_to_increase)
        self.assertEqual(102,self.pub.till)
    
    def test_sell_to_customer(self):
        self.pub.add_drink(self.drink)
        self.pub.customer_buys_drink(self.drink, self.customer)
        self.assertEqual(102, self.pub.till)
        self.assertEqual(18, self.customer.wallet)
        self.assertEqual(0, self.pub.stock_count(self.drink))
    
    def test_check_cust_age__True(self):
        self.assertEqual(True, self.pub.check_cust_age(self.customer))

    def test_check_cust_age__False(self):
        self.assertEqual(False,self.pub.check_cust_age(self.customer2))
        
    def test_customer_buys_drink(self):
        self.pub.add_drink(self.drink)
        self.pub.customer_buys_drink(self.drink, self.customer2)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(50, self.customer2.wallet)
        self.assertEqual(1, self.pub.stock_count(self.drink))
    
    def test_customer_gets_drunk(self):
        self.customer.drunk_customer(self.drink)
        self.assertEqual(1, self.customer.drunkenness)
    
    def test_customer_sober_up(self):
        self.customer.drunk_customer(self.drink)
        self.customer.sober_up(self.food)
        self.assertEqual(0, self.customer.drunkenness)
    
    def test_customer_buys_food(self):
        self.pub.add_food(self.food)
        self.pub.add_drink(self.drink)
        self.pub.customer_buys_drink(self.drink, self.customer)
        self.pub.customer_buys_food(self.customer, self.food)
        self.assertEqual(103, self.pub.till)
        self.assertEqual(17, self.customer.wallet)
        self.assertEqual(0, self.pub.stock_count(self.drink))
        self.assertEqual(0, len(self.pub.food))

