
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('Bart')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Working with Lists
# ======-----------Python book "" 5.8 - 5.10
# """
# my_list1 = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'admin']
#
# if my_list1:
#     for user in my_list1:
#         if user == 'admin':
#             print('hello ' + user + ', you are a special user')
#         else:
#             print('Hello ' + user + ' thanks for logging in')
# else:
#     print ('We need some users')
#
# current_users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'Admin']
# new_users = ['user7', 'user2', 'user9' ]
#
# for user in new_users:
#     if user in current_users:
#         print('hi '+user+' you had already that name')
#     else:
#         print('Hi, ' +user+ ' adding new user')
#
#
# numbers = (1,2,3,4,5,6,7,8,9)
# for number in numbers:
#     if number == 1:
#         print(number,'st')
#     elif number == 2:
#         print(number, 'nd')
#     elif number == 3:
#         print(number, 'rd')
#     else:
#         print(number, 'th')
#
# """
#
# # Working with Dictionaries
# # ======-----------Python book "" 6.1 - 6.3
# """
# person_wife = {'name': 'Katia', 'age': 32, 'last_name': 'Madej', 'city': 'Wsiewolosk'}
# print(person_wife)
#
# persons_favNumbers = {'Jan': 5, 'Agata': 32, 'Jacek': 87, 'Lukasz': 72}
#
# janFav = (persons_favNumbers['Jan'])
# agataFav = (persons_favNumbers['Agata'])
# jacetFav = (persons_favNumbers['Jacek'])
# LukaszFav = (persons_favNumbers['Lukasz'])
#
# print('Jan,', janFav)
# print('Agata,', agataFav)
# print('Jacek,', jacetFav)
# print('Lukasz,', LukaszFav)
#
# new_words = {'looping': 'to loop through some list or dictionary where there is more than one item', 'dictionary': 'data format with key-value pairs'}
# looping_value = new_words.get('looping', 'No point value assigned.')
# dictionary_value = new_words.get('dictionary', 'No point value assigned.')
#
# print('looping is \n'+looping_value)
# print('dictionary is \n'+dictionary_value)
#
# """
# # ======-----------Python book "" 6.4 - 6.6
#
# """
# new_words = {'looping': 'to loop through some list or dictionary where there is more than one item', 'dictionary': 'data format with key-value pairs'}
# for key, value in new_words.items():
#     print(f"\nKey: {key}")
#     print(f"\nValue: {value}")
#
# for key, value in new_words.items():
#     print(f"{key.title()} is  {value.title()}.")
#
# rivers = {'Wisla': 'Poland', 'Volga': 'Russia', 'Dnieper': 'Ukraine', 'Danube': 'Hungary', 'Elbe': 'Germany', 'Nile': 'Egypt'}
#
# for key, value in rivers.items():
#     if key == 'Wisla':
#         print(f"{key}is the biggest river in {value.title()}")
#     else:
#         print(f"{key} is a river that runs through {value.title()}")
#
# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
#
# persons = []
# for key, value in favorite_languages.items():
#     persons.append(key)
#
# print(persons)
#
# people_for_poll = ['phil', 'lisa', 'robert', 'paul', 'sarah', 'adam', 'jen']
#
# for person in people_for_poll:
#     if person in persons:
#         print("thanks " + person)
#     else:
#         print("could you take a poll " + person)
# """
#
# # ======-----------Python book "" 6.7 - 6.12
# """
# person_wife = {'name': 'Katia', 'age': 32, 'last_name': 'Madej', 'city': 'Wsiewolosk'}
#
# person_andrew = {'name': 'Andrzej', 'age': 66, 'last_name': 'Madej', 'city': 'Dolnik'}
#
# person_Mat = {'name': 'Mateusz', 'age': 38, 'last_name': 'Madej', 'city': 'Gorzow'}
#
# people = [person_wife, person_andrew, person_Mat]
#
# for person in people:
#     print(person['name'])
#
#
# favourite_places = {'Bart': ['plaza_debki', 'tatry','pilvilampi'], 'Katia': ['plaza_debki', 'Gdansk','SPB'], 'Ewa':['Darlowko', 'Zakopane']}
#
# for name, places in favourite_places.items():
#     print(f"\n{name}'s favourite place are:")
#     for place in places:
#         print(f"\n{place.title()}")
#
# persons_favNumbers = {'Jan': [5,3,75], 'Agata': [32,46],'Jacek': [87, 60], 'Lukasz': [72]}
#
# for name, numbers in persons_favNumbers.items():
#     print(f"\n{name}'s favourite numbers are:")
#     for number in numbers:
#         print(f"\n{number}")
#
# cities = {'Gdask': {'country': 'Poland', 'population': 490000, 'fact': 'biggest brick church'}, 'Moscow': {'country': 'Russia', 'population': 12000000, 'fact': 'red squeare'},
#           'Hamburg': {'country': 'Germany', 'population': 1700000, 'fact': 'st pauli district'} }
#
# for city, cities_info in cities.items():
#     print(f"\n City of: {city} ")
#     country = f"{cities_info['country']}"
#     population = f"{cities_info['population']}"
#     fact = f"{cities_info['fact']}"
#     print(f"\tis in country: {country}")
#     print(f"\thas population: {population}")
#     print(f"\tis known of: {fact}")
# """
# # ======-----------Python book "" 7.1 - 7.3
#
# """
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
#
# car = input("What kind of car would you like to rent today ?: ")
# print(f"let me check if we have any {car} available right now.....")
#
#
# amount_people = input("How many people are coming for a dinner ?: ")
# amount_people = int(amount_people)
# if amount_people > 8:
#     print("you have to wait for a table")
# else:
#     print("your table is ready")
#
# wynik = input("Podaj jakas liczbe:")
# wynik = int(wynik)
#
# while wynik != 8:
#     wynik = input("Podaj liczbe:")
#     wynik = int(wynik)
#     print(f"podales {wynik}")
#     if wynik == 8:
#         print("ok")
#
#
# number = input("enter some number:")
# number = int(number)
#
# if number % 10 == 0:
#     print(f"The number {number} is multiple of 10")
# else:
#     print(f"The number {number} is not multiple of 10")
# """
# # ======-----------Python book "" 7.4 - 7.7
# """
# while True:
#     ingridient = input(f"please specify your pizza topping:")
#     if ingridient == 'quit':
#         break
#     else:
#         print(f"adding {ingridient} to your pizza")
#
#
# while True:
#     age = input(f"please put your age:")
#     age = int(age)
#     if age == 0:
#         break
#     elif age < 3:
#         print(f"the cost for your ticket is free")
#     elif age >= 3 and age <= 12:
#         print(" your ticket costs 10 USD")
#     elif age > 12:
#         print("your ticket costs 15 USD")
#
#
# active = True
# while active:
#     ingridient = input(f"please specify your pizza topping:")
#     if ingridient == 'quit':
#         active = False
#     else:
#         print(f"adding {ingridient} to your pizza")
#
#  """
# # ======-----------Python book "" 7.8 - 7.10
#
# """
# sandwich_orders = ['pastrami','veggieburger','pastrami','bullshot','pigman','chickguy','cheescore','turchevil','pastrami', 'veggieburger']
#
# finished_sandwiches = []
#
# while 'pastrami' in sandwich_orders:
#     print('We run out of Pastrami')
#     sandwich_orders.remove('pastrami')
#
# print(sandwich_orders)
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I've made a {current_sandwich}")
#     finished_sandwiches.append(current_sandwich)
#
# print (finished_sandwiches)
# print(sandwich_orders)
#
#
# responses = {}
# # set a flag to True
# poll_active = True
#
# while poll_active:
#     name = input("\nPlease give your name:")
#     response = input("\nWhat is your most favourite place where you would like to go:")
#     # Store the response in the dictionary.
#     responses[name] = response
#     # Find out if anyone else is going to take the poll.
#     repeat = input("do you want to put another name?: yes/no")
#     if repeat == 'no':
#         poll_active = False
#
# # Polling is complete. Show the results.
# print("\n Show results:")
#
# for name, response in responses.items():
#     print(f"\n{name} would like to go to {response}.")
# """
# # ======-----------Python book "" 8.1 - 8.2
# """
# def favourite_book(book):
#     print(f"your favourite book is {book}")
#
# favourite_book('Esencjalista')
#
# """
# # ======-----------Python book "" 8.3 - 8.5
#
# """
# def make_shirt(size, message="I love Python"):
#     print(f'Your shirt size will be {size}')
#     print(f"\n And your text on your shirt will be {message}")
#
# #make_shirt(size = "Large")
#
# def describe_city(city, country="Poland"):
#     print(f'Your city is  {city}')
#     print(f"\n that is in the country:\n  {country}")
#
# describe_city(city = "Helsinki", country="Finlandia")
#
# """
# # ======-----------Python book "" 8.6 - 8.8
#
# """
# def city_country(city, country):
#     formated = f"\n {city}, {country}"
#     return formated
#
# while True:
#     print("\nPlease tell city name:")
#     print("(enter 'q' at any time to quit)")
#     city = input("City name: ")
#     if city == 'q':
#         break
#     country = input("Country name: ")
#     if city == 'q':
#         break
#
#     formatted_name = city_country(city, country)
#     print(f"{formatted_name}")
#
# """
# # ======-----------Python book "" 8.6 - 8.8
#
# """
# def make_album(artist_name, album_tittle, number_songs = None):
#     music_album = {'artist': artist_name, 'album': album_tittle, 'songs': number_songs}
#     return music_album
#
#
#
# while True:
#     print("First specify your artist, q to quit")
#     artist = input("\n Give artist name:")
#     if artist == 'q':
#         break
#     print("Now specify album, q to quit")
#     album = input("\n Give album name:")
#     if album == 'q':
#         break
#     print("Now specify number of songs, q to quit")
#     songs = input("\n Give number of songs")
#     if songs == 'q':
#         break
#     new_album = make_album(artist, album, songs)
#     print(new_album)
#
#
# album1 = make_album('Michael Jackson', 'Thriller')
# print(album1)
#
# album2 = make_album('AC/DC', 'Back in Black')
# print(album2)
#
# album3 = make_album('The dark side of the Moon', 'Pink Floyd', 6)
# print(album3)
#
# """
# # ======-----------Python book "" 8.9 - 8.11
# """
#
# list1 = ['sms1', 'sms2', 'sms3', 'sms4']
# sent_messages = []
# def send_messages(list):
#     while list:
#         current_message = list.pop()
#         print(current_message)
#         sent_messages.append(current_message)
#
#
#
# send_messages(list1)
# print(list1)
#
#
# list1 = ['sms1', 'sms2', 'sms3', 'sms4']
# sent_messages = []
# def send_messages(list):
#     while list:
#         current_message = list.pop()
#         print(current_message)
#         sent_messages.append(current_message)
#
#
#
# send_messages(list1[:])
# print(list1)
#
# # ======-----------Python book "" 8.12 - 8.14
#
# def sandwich_build(*items):
#     for item in items:
#         print(f" this will be on your sandwich: {item}")
#
# sandwich_build('cheese','tomato','ham','lettuce')
#
# # takes 2 necessary arguments and creates a dictionary with optional user_info data
# def build_profile(name, lastname, **user_info):
#     user_info['name'] = name
#     user_info['lastname'] = lastname
#     return user_info
#
# user_profile = build_profile('Bart', 'Madej', location = 'Gdansk', age = 41)
# print(user_profile)
# """
#
# # ======-----------Python book "" 8.15 - 8.17
# """
# from printing_functions import build_profile as bp
#
# user = bp('Bart', 'Mad', location = 'Gdansk')
# print(user)
#
# """
# # ======-----------Python book "" 9.1 - 9.3
# """
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
# """
# """Initialize restaurant name and cuisine type attributes."""
#
#         self.name = restaurant_name
#         self.type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"The restaurant name is  {self.name} , ")
#         print(f"And it has  {self.type} type of cuisine:")
#
#     def open_restaurant(self):
#         print(f"Restaurant {self.name} is open now")
#
# new_restaurant = Restaurant('DobreZarcie','PolskaKuchnia')
#
# #print(new_restaurant.name)
# #print(new_restaurant.type)
#
# new_restaurant.open_restaurant()
#
# wloska_rest = Restaurant('italiana', 'ItalianKitchen')
#
# wloska_rest.open_restaurant()
#
# thaiFood = Restaurant('Bangkok', 'ThaiFood')
#
# thaiFood.open_restaurant()

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
#
#     def describe_users(self):
#         print(self.user_info)
#
# new_user = User('Bart', 'Mad')
# new_user.describe_users()
# ======-----------Python book "" 9.4 - 9.5

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
# # Initialize restaurant name and cuisine type attributes.
#
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"The restaurant name is  {self.name} , ")
#         print(f"And it has  {self.type} type of cuisine:")
#
#     def set_number_served(self, number):
#         self.number_served = number
#
#     def increment_number_served(self, customers):
#         self.number_served += customers
#
#     def open_restaurant(self):
#         print(f"Restaurant {self.name} is open now")

# new_restaurant = Restaurant('DobreZarcie','PolskaKuchnia')
# print(new_restaurant.number_served)
# new_restaurant.number_served = 3
# print(new_restaurant.number_served)
# new_restaurant.set_number_served(56)
# print(new_restaurant.number_served)
# new_restaurant.increment_number_served(20)
# print(new_restaurant.number_served)

# class User:
#     def __init__(self, first_name, last_name, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = login_attempts
#
#     def increment_login_attempts(self):
#         self.login_attempts = self.login_attempts + 1
#
#
# user1 = User('Bart', 'Mad', 47)
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)

# ======-----------Python book "" 9.6 - 9.9

#     def increment_login_attempts(self):
#         self.login_attempts = self.login_attempts + 1
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['chocolate', 'cream']
#
#     def get_info(self):
#         print(f"this ice cream has flavours: {self.flavors}")

# new_restaurant = IceCreamStand('Nowa', 'polska')
# new_restaurant.get_info()
# new_restaurant.describe_restaurant()

# class Privilages:
#     def __init__(self, privilages = ['can do']):
#         self.privilages = privilages
#
#     def show_privilages(self):
#         print(f"Admin can: {self.privilages}")
# class Admin(User):
#     def __init__(self, first_name, last_name, login_attempts):
#         super().__init__(first_name, last_name, login_attempts)
#         self.privilages = Privilages()
#
#
#
#
#
# newUser = Admin('Bart','Mad',0)
# newUser.privilages.show_privilages()

# ======-----------Python book "" 9.10 - 9.12

# from restaurant import Restaurant
#
# my_restaurant = Restaurant('nowa2','polska')
# my_restaurant.describe_restaurant()

# ======-----------Python book "" 9.13 - 9.16
from random import randint
from random import choice

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        random_number = randint(1,self.sides)
        print(random_number)

# new_die = Die(sides=10)
#
# myList = [3, 56, 235, 8, 6, 98, 74, 32, 873, 50, 'j', 'd', 't', 'a', 'k' ]
#
# yourlist = []
# yourlist.append(choice(myList))
# yourlist.append(choice(myList))
# yourlist.append(choice(myList))
# yourlist.append(choice(myList))
#
# print(yourlist)
#
# active = True
# i = 0
# print(i)
# while active:
#     i += 1
#     lotterry = []
#     lotterry.append(choice(myList))
#     lotterry.append(choice(myList))
#     lotterry.append(choice(myList))
#     lotterry.append(choice(myList))
#     if lotterry == yourlist:
#         active = False
#
# print(lotterry)
# print(i)

# ======-----------Python book "" 10.1 - 10.2

# with open ('learning_python.txt') as my_file:
#     contents = my_file.read()
# print(contents)
#
# with open ('learning_python.txt') as my_file:
#     for line in my_file:
#         print(line)
#

# with open ('learning_python.txt') as my_file:
#     lines = my_file.readlines()
#
# info = ''
#
# for line in lines:
#     new_line = line.replace('Python', 'C')
#     info += new_line.rstrip()
#
# print(info)

# ======-----------Python book "" 10.3 - 10.5

# filename = 'guest.txt'
# user_name = input("what is your name ?")
# with open(filename, 'w') as file_object:
#     file_object.write(user_name)


# filename = 'guest.txt'
# active = True
# while active:
#     user_name = input("what is your name ?, q for quite")
#     if user_name == "q":
#         active = False
#     greeting = "welcome " + user_name + " as a visitor"
#     print(greeting)
#     with open(filename, 'a') as file_object:
#         file_object.write(greeting+"\n")

# script to create a new file with less lines


active = True
while active:
    filename = input("what is the whole file name? ")
    try:
        with open(filename) as my_file:
            lines = my_file.readlines()
    except FileNotFoundError:
        print("No such file")
    else:
        active = False

filename2 = 'dataafterfiltering.csv'

lenghth = len(lines)

a=0
new_list = []
line1 = lines[0]
with open(filename2, 'w') as f:
    f.write(line1)

active = True
while active:
    sampling = input("Specify sampling in s ")
    try:
        b = int(sampling)
    except ValueError:
        print("This is not a number")
    else:
        active = False

for item in lines:
    a += 1
    if a == b:
        a = 0
        new_list.append(item)
        with open(filename2, 'a') as f:
            f.write(item)

print(len(new_list))
print(a)









