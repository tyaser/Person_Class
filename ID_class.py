'''
Assignment 10.1: Your Own Class
Talia Yaser
CSE20
The purpose of this assignment is to create a class, in my case being a Person class which takes in 5 different data variables (name, age, height, eyes, hair) inspired by IDs. Since the variables are encapsulated
I implemented getter and setter methods to make them accessible outside of the class and I implemented three of my own methods which includes ID, birthyear, and generation. I demonstrated the use of my class and methods in
the main code. This class also acts like a randomizer if the user were to input no arguments, and I did this by using the random module. In order to use the random name generator, two other external files are needed.
Citations: generations taken from http://socialmarketing.org/archives/generations-xy-z-and-the-others/ names taken from http://random-name-generator.info/
'''
# importing date from datetime python module, random module, and variable randname from random_name file
from datetime import date
import random
from random_name import randname
# setting two global variables to generate a random RGB code for both eyes and hair using random.randint. If the user wants random colors, they're going to have to input returned RGB code into and external program to receive color
RANDCOLOR1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RANDCOLOR2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# declaring class Person
class Person:
  # setting two class variables, first being the species (human) since this class is meant to demonstrate real life people.
  species = "human"
  # the second being alive (defined by state class variable) since this program, specifically the birthyear method, assumes the person is still alive.
  state = "alive" 
  # setting default values for the data variables and using self to refer to the class and init to encapsulate the variables. When creating an object, age must also be an integer.
  def __init__(self, name = randname, age = random.randint(1,100), height = "N/A", eyes = RANDCOLOR1, hair = RANDCOLOR2):
    # using double underscores to make the variables fully private.
    self.__name = name
    self.__age = age
    self.__height = height
    self.__eyes = eyes
    self.__hair = hair
  # The following 5 get statements are there to allow the user to access the variables in the main method and outside of the class -- also objects created in Person class will be referred to as such and self refers back to object's class.
  def get_name(self):
    # returns name of object
    return self.__name
  def get_age(self):
    # returns age of object
    return self.__age
  def get_height(self):
    # returns height of object
    return self.__height
  def get_eyes(self):
    # returns color of object's eyes
    return self.__eyes
  def get_hair(self):
    # returns object's hair color
    return self.__hair
  # following set methods are used to set or change the data variables and take in one argument respective to the given variable
  def set_name(self, name):
    self.__name = name
    # returns newly assigned name private variable
    return self.__name
  # sets and returns age of object
  def set_age(self, age):
    self.__age = age
    return self.__age
  # sets and returns height of object (metric is up to the user)
  def set_height(self, height):
    self.__height =  height
    return self.__height
  # sets and returns new eye color
  def set_eyes(self, eyes):
    self.__eyes = eyes
    return self.__eyes
  # sets and returns new hair color
  def set_hair(self, hair):
    self.__hair = hair
    return self.__hair
  # The ID methodreturns a multi-lined string formatted using \n and \t to create new lines and tab information. This method is inspired by information shown on IDs and all it does is return (print can be done in main code)
  # the attributes of a given object and print a labelled list of them.
  def ID(self):
    # formatting string using f, brackets, and \n \t
    return (f"name:\t{self.__name}\nage:\t{self.__age}\nheight:\t{self.__height}\neyes:\t{self.__eyes}\nhair:\t{self.__hair}")
  # The birthyear method returns the birth year of an object in the class by using their assigned age attribute and subtracting it from the current year (2021 being the year this program was created in)
  def birthyear(self):
    # finding today's date using date attribute of datetime module that was imported previously
    todays_date = date.today()
    # assigning the present year (given as an intger and found by using .year) to presyear variable 
    presyear = todays_date.year
    # subtracting age of object by present year to find birth year which is assigned to presyear
    birthyr = (todays_date.year - self.__age)
    # returns birth year
    return birthyr
  # The generation method finds the generation of the object using the birthyear method and the generation names provided by aforementioned source.
  # If this program were used decades from now, this method would be considered invalid unless changed to refer to current era.
  def generation(self):
    # using if elif else statements to find if the object's birth year falls within given range, the second number being increased by one year since range doesn't include stopping point
    if self.birthyear() in range(1922,1928):
      # If object was born between 1922 and 1927 it makes them the WW2 generation, so I assigned that generation as a string to the gen variable.
      gen = "World War II generation"
    elif self.birthyear() in range(1928,1946):
      gen = "Post-War Cohort generation"
    elif self.birthyear() in range(1946,1955):
      gen = "a Baby Boomer"
    elif self.birthyear() in range(1955,1966):
      gen = "Generation Jones"
    elif self.birthyear() in range(1966,1977):
      gen = "Generation X"
    elif self.birthyear() in range(1977,1995):
      gen = "Generation Y"
    elif self.birthyear() in range(1995,2013):
      gen = "Generation Z"
    # If object's birthyear doesn't fall within any of the given ranges, N/A is assigned to gen
    else:
      gen = "N/A"
    # method returns a string stating object's name, birthyear, and what generation they were born in.
    return (f"{self.__name} was born in {self.birthyear()} making them {gen}.")

''' MAIN CODE TO DEMONSTRATE METHODS AND CLASS'''
def main():
    x = Person("Bob", 15, 174, "brown", "brown")
    print(x.get_age())
    y = Person("Cindy", 76, 183, "purple", "pink")
    y.set_name("Mister Rogers")
    print(y.ID())
    print(y.get_name())
    print((Person.state), (Person.species))
    z = Person()
    print(z.ID())
    print(z.birthyear())
    print(z.generation())
    print(y.generation())
    print(z.ID())
    print(x.ID())
    return
if __name__ == "__main__":
    main()
