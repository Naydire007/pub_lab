class Customer:
  def __init__(self,name,wallet,age):
      self.name = name
      self.wallet = wallet
      self.age = age
      self.drunkenness = 0
  
  def reduce_wallet(self, amount):
      self.wallet -= amount
    
  def drunk_customer(self,drink):
      self.drunkenness += drink.drunkenness
    
  def sober_up(self,food):
      self.drunkenness -= food.rejuvenation_level
    
      