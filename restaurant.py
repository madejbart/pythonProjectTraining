class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
# Initialize restaurant name and cuisine type attributes.

        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is  {self.name} , ")
        print(f"And it has  {self.type} type of cuisine:")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open now")