import unittest
#Aplication code
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
    return a*b
#Automated test cases
class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(20,10),10)
  def test_multiply(self):
    self.assertEqual(multiply(5,4),20)
#main application
if __name__ == "__main__":
  print("student calculator application")
  print("Addition",add(20,20))
  print("subtraction:",subtract(20,10))
  print("multiply:",multiply(5,4))
  print("\nexecuting automated tests...\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)
  
