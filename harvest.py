############
# Part 1   #
############

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)



    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        

    def __repr__(self):
        return f'<MelonType {self.code} {self.first_harvest} {self.color} {self.is_seedless} {self.is_bestseller} {self.name} {self.pairings}>'

# muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
# print(muskmelon)

# muskmelon.add_pairing("mint")
# print(muskmelon)

# muskmelon.update_code("new_code")
# print(muskmelon)


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    
    casaba = MelonType("cas", 2003, "orange", True, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("prosciutto")

    yellow_watermelon = MelonType("yw", "2013", "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")


    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])

    return all_melon_types

# print(make_melon_types())

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
  
    # melon_types = [ Muskmelon, Casaba, Crenshaw, Yellow Watermon]
    # Muskmelon
    # Muskmelon.pairings = ["mint"]
    # len(Muskmelon.pairings) = 1


    # Casaba
    
    # loops through each melon in melon_types list
    for melon in melon_types:
        # checks if that specific melon has any items that it pairs well with
        
        # if it doesn't have any items that it pairs well with, then go to the next melon
        if len(melon.pairings) == 0:
            continue

        # if it does have item/items that it pairs well with print them
        else:
            print(f'{melon.name} pairs with')

            # to print each pair item separately 
            for pair in melon.pairings:
                print(f'- {pair}')
            


# all_melon_types = make_melon_types()
# print_pairing_info(all_melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}

    for melon in melon_types:
        melon_type_dict[melon.code] = melon

    return melon_type_dict

# all_melon_types = make_melon_types()
# make_melon_type_lookup(all_melon_types)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by

    # a melon is able to be sold if both its shape and color ratings are greater than 5, 
    # and it didn’t come from field 3, which was found to have poisonous fertilizer planted 
    # by a competing melon farm.
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.from_field != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    muskmelon, casaba, crenshaw, yellow_watermelon = melon_types

    all_melons = []

    melon1 = Melon(yellow_watermelon, 8, 7, 2, "Sheila")
    melon2 = Melon(yellow_watermelon, 3, 4, 2, "Sheila")
    melon3 = Melon(yellow_watermelon, 9, 8, 3, "Sheila")
    melon4 = Melon(casaba, 10, 6, 35, "Sheila")
    melon5 = Melon(crenshaw, 8, 2, 35, "Michael")
    melon6 = Melon(crenshaw, 8, 2, 35, "Michael")
    melon7 = Melon(crenshaw, 2, 3, 4, "Michael")
    melon8 = Melon(muskmelon, 6, 7, 4, "Michael")
    melon9 = Melon(yellow_watermelon, 7, 10, 3, "Sheila")

    all_melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return all_melons

all_melon_types = make_melon_types()
all_melons = make_melons(all_melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        is_sellable = melon.is_sellable()

        if is_sellable == True:
            print(f"Harvested by {melon.harvested_by} from Field {melon.from_field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvested_by} from Field {melon.from_field} (NOT SELLABLE)")


get_sellability_report(all_melons)