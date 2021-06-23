
class Pub:
  def __init__(self, name, till):
      self.name = name
      self.till = till
      self.drinks = []

  
  def add_drink(self,drink):
    self.drinks.append(drink)

  def reduce_drink(self,drink):
      self.drinks.remove(drink)

  def increase_till(self, amount):
      self.till += amount





  