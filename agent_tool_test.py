from agent_tool import *
ag = Agent()
# ag.add_property()
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
ag.display_properties()
