from django.test import SimpleTestCase
from . import calc

class CalcTests(SimpleTestCase):

    def test_add(self):
        res = calc.add(1,2,3,4,5)

        self.assertEqual(res,14.9)