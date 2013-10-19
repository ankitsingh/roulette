

class Outcome(object):
  """Outcome contains a single outcome on which a bet can be placed."""
  
  def __init__(self,name, odds):
    """Constructor, creating the outcome instance"""
    self.name = name
    self.odds = odds
    
    
  def winAmount(self,amount):
    """calculating the amount won, which depends upon the odds and the amount played"""
    return self.odds * amount
  
  def __eq__(self,other):
    """to check if two outcome instances are equal"""
    # TIP: The is keyword is a test for object identity(referencing the same object) while == is a value comparison.
    return self.name == other.name
  
  def __ne__(self,other):
    """to check if two objects are unequal"""
    return self.name != other.name
  
  def __str__(self):
    """outputs the object in a clean, readable fashion like 'name (odds:1)'"""
    return "%s, (%d:1)" % (self.name, self.odds)
  
  
      
