
class Pub:
  def __init__(self, name, till):
      self.name = name
      self.till = till
      self.drinks = []
      self.food = []
      self.stock = {}
  
  def add_drink(self,drink):
    self.drinks.append(drink)

  def reduce_drink(self,drink):
      self.drinks.remove(drink)

  def increase_till(self, amount):
      self.till += amount

  def check_cust_age(self, customer):
    if customer.age < 18:
      return False
    else:
      return True    
  
  def customer_buys_drink(self,drink,customer):
    if self.check_cust_age(customer) == False or customer.drunkenness > 5 :
      return "No Drink"
    else:
      customer.reduce_wallet(drink.price)
      self.increase_till(drink.price)
      self.reduce_drink(drink)
      customer.drunk_customer(drink)
  
  def customer_buys_food(self, customer, food):
      customer.reduce_wallet(food.price)
      self.increase_till(food.price)
      self.reduce_food(food)
      customer.sober_up(food)

  def add_food(self,food):
    self.food.append(food)

  def reduce_food(self,food):
      self.food.remove(food)