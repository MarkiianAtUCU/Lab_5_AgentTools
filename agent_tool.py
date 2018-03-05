def get_valid_input(input_string, valid_options):
    """
    (str, list) -> str

    Function get input from keyboard and if input is incorrect asks again
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Class represents property with (area, number of beds, number of baths)
    """

    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """
        (str, str, str, str) -> None

        Function initialise property class
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        (None) -> None

        Function displays info about property
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        (None) -> dict

        Function gets info about property from keyboard
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter a number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class represents appartment with type of (loundries, balconies)
    """
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        (str, str) -> None

        Function initialise Apartment class
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        (None) -> None

        Function displays info about apartment
        """
        super().display()
        print("APARTMENT DETAILS")
        print('laundry: %s' % self.laundry)
        print('has balcony : %s' % self.balcony)

    def prompt_init():
        """
        (None) -> dict

        Function gets info about apartment from keyboard
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilitirs does"
                                  "the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Class represent House with (num of stories, garage type, is fenced)
    """
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        (str, str, str) -> None

        Function initialise House class
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        (None) -> None

        Function displays info about house
        """
        super().display()
        print('HOUSE DETAILS')
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        (None) -> dict

        Function gets info about house from keyboard
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How mwny stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Clas represents purchase with (price, taxes)
    """

    def __init__(self, price='', taxes='', **kwargs):
        """
        (str, str) -> None

        Function initialise Purchase class
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        (None) -> None

        Function displays info about purchase
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        (None) -> dict

        Function gets info about purchase from keyboard
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Clas represents rental with (is furnished, is utilities, ammount of rent)
    """

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        (str, str, str) -> None

        Function initialise Rental class
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        (None) -> None

        Function displays info about rent
        """
        super().display()
        print("RENTAL DETAILS")
        print('rent: {}'.format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        (None) -> dict

        Function gets info about rent from keyboard
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Class represents House Rental with attributes of house and rent
    """
    def prompt_init():
        """
        (None) -> dict

        Function gets info about house rent from keyboard
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Class represents Apartment Rental with attributes of apartment and rent
    """
    def prompt_init():
        """
        (None) -> dict

        Function gets info about apartment rent from keyboard
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Class represents Apartment Purchase with attributes of apartment
    and purchase
    """
    def prompt_init():
        """
        (None) -> dict

        Function gets info about apartment purchase from keyboard
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Class represents Apartment Purchase with attributes of house and purchase
    """
    def prompt_init():
        """
        (None) -> dict

        Function gets info about house purchase from keyboard
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class represents Agent
    """

    def __init__(self):
        """
        (None) -> None

        Function initialise Agent class
        """
        self.property_list = []

    def display_properties(self):
        """
        (None) -> None

        Function displays info about all properties
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def display_price_less(self, price):
        """
        (int) -> None

        Function displays property with price less than given
        """
        for property in self.property_list:
            if type(property) in [HousePurchase, ApartmentPurchase]:
                if eval(property.price) <= price:
                    property.display()

    def display_rent_less(self, price):
        """
        (int) -> None

        Function displays property with rent less than given
        """
        for property in self.property_list:
            if type(property) in [HouseRental, ApartmentRental]:
                if eval(property.rent) <= price:
                    property.display()

    def add_property(self):
        """
        (None) -> None

        Function adds property of chosen type
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        print(init_args)
        self.property_list.append(PropertyClass(**init_args))
