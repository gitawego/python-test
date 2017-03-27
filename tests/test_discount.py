import sys
import os
sys.path.append(os.getcwd())
from bookshop import checkout
import unittest

class TestDiscount(unittest.TestCase):
  """
  test discount
  """

  def test_calculate_discount_for_four_books(self):
    result = checkout.buy({
      "book1":2,
      "book2":3,
      "book3":1,
      "book4":5,
      "book5":2
    })
    self.assertEqual(result.get('price'), 4*8*0.85 + 3*8*0.9+2*8*0.95+4*8)
    print(result.get('discount_books'))

if __name__ == '__main__':
  unittest.main()
