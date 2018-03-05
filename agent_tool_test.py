from agent_tool import *
import io
import sys
import unittest

# Preparation
ag = Agent()

hr = HouseRental(**{'square_feet': '20sq', 'beds': '20b', 'baths': '20ba',
                    'fenced': 'yes', 'garage': 'none', 'num_stories': '20',
                    'rent': '200',  'utilities': '20', 'furnished': 'no'})

hp = HousePurchase(**{'square_feet': '200', 'beds': '1', 'baths': '20',
                      'fenced': 'no', 'garage': 'none', 'num_stories': '20',
                      'price': '10',  'taxes': '20'})

ar = ApartmentRental(**{'square_feet': '20', 'beds': '10', 'baths': '20',
                        'laundry': 'coin',
                        'balcony': 'solarium', 'rent': '2000',
                        'utilities': '10', 'furnished': 'no'})

ap = ApartmentPurchase(**{'square_feet': '20', 'beds': '1', 'baths': '2',
                          'laundry': 'ensuite', 'balcony': 'no',
                          'price': '20000', 'taxes': '10'})
ag.property_list = [hr, hp, ar, ap]


def test_capture(st):
    """
    (str) -> str

    Function capture output from evaluation given string
    """
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    eval(st)
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()


# Test cases
t1 = "ag.display_properties()"
t2 = "ag.display_rent_less(1000)"
t3 = "ag.display_price_less(1000)"
t4 = "ag.display_price_less(20000)"

# Cannot make line shorter due to dark magic of python multiline strings
r1 = 'PROPERTY DETAILS\n================\nsquare footage: 20sq\nbedrooms: 20b\nbathrooms: 20ba\n\nHOUSE DETAILS\n# of stories: 20\ngarage: none\nfenced yard: yes\nRENTAL DETAILS\nrent: 200\nestimated utilities: 20\nfurnished: no\nPROPERTY DETAILS\n================\nsquare footage: 200\nbedrooms: 1\nbathrooms: 20\n\nHOUSE DETAILS\n# of stories: 20\ngarage: none\nfenced yard: no\nPURCHASE DETAILS\nselling price: 10\nestimated taxes: 20\nPROPERTY DETAILS\n================\nsquare footage: 20\nbedrooms: 10\nbathrooms: 20\n\nAPARTMENT DETAILS\nlaundry: coin\nhas balcony : solarium\nRENTAL DETAILS\nrent: 2000\nestimated utilities: 10\nfurnished: no\nPROPERTY DETAILS\n================\nsquare footage: 20\nbedrooms: 1\nbathrooms: 2\n\nAPARTMENT DETAILS\nlaundry: ensuite\nhas balcony : no\nPURCHASE DETAILS\nselling price: 20000\nestimated taxes: 10\n'
r2 = 'PROPERTY DETAILS\n================\nsquare footage: 20sq\nbedrooms: 20b\nbathrooms: 20ba\n\nHOUSE DETAILS\n# of stories: 20\ngarage: none\nfenced yard: yes\nRENTAL DETAILS\nrent: 200\nestimated utilities: 20\nfurnished: no\n'
r3 = 'PROPERTY DETAILS\n================\nsquare footage: 200\nbedrooms: 1\nbathrooms: 20\n\nHOUSE DETAILS\n# of stories: 20\ngarage: none\nfenced yard: no\nPURCHASE DETAILS\nselling price: 10\nestimated taxes: 20\n'
r4 = 'PROPERTY DETAILS\n================\nsquare footage: 200\nbedrooms: 1\nbathrooms: 20\n\nHOUSE DETAILS\n# of stories: 20\ngarage: none\nfenced yard: no\nPURCHASE DETAILS\nselling price: 10\nestimated taxes: 20\nPROPERTY DETAILS\n================\nsquare footage: 20\nbedrooms: 1\nbathrooms: 2\n\nAPARTMENT DETAILS\nlaundry: ensuite\nhas balcony : no\nPURCHASE DETAILS\nselling price: 20000\nestimated taxes: 10\n'


# Test
class TestStringMethods(unittest.TestCase):

    def test_main(self):
        self.assertEqual(test_capture(t1), r1)

    def test_display_rent_less(self):
        self.assertEqual(test_capture(t2), r2)

    def test_display_price_less_1(self):
        self.assertEqual(test_capture(t3), r3)

    def test_display_price_less_2(self):
        self.assertEqual(test_capture(t4), r4)


if __name__ == '__main__':
    unittest.main()
