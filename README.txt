https://github.com/tyaser/Person_Class
The purpose of the class Person is to create objects with human attributes such as one's name, age, height, eyes, and hair. 
The class can also be used as a random person generator the the data variables have a default value set to a randomizer. 
Though, in order for the random name generator two external files have to be downloaded in the same place as the class program. 
Since the data variables in the Person class are private there are get-set methods for each of the variables to access them outside of the class. 
The class contains other methods to get the ID of a Person object, the year they were born in, and what generation their birth year lands in.

The first class variable is the species which is 'human' since the class refers to people not any other species.
The second class variable is state of living the person is in which is automatically assigned as 'alive' since the methods and overall class assumes the object is alive.
There are five data variables:
name - refers to the object's name.
age - refers to the object's age, given as an integer.
height - refers to the object's height, measurement system doesn't matter and N/A is given if randomizer is used.
eyes - refers to the color of the object's eyes, given as an RGB code if randomizer is used.
hair - refers to the color of the object's hair, given as an RGB code if randomizer is used.

There are five get methods, one for each data variable:
get_name - returns the name of object, no arguments are needed just the object itself. While demonstrating method, implementation would look like Person1.get_name(), Person1 being an object made under Person class
get_age - returns the age of object, no arguments are needed just the object itself. While demonstrating method, implementation would look like Person1.get_age(), Person1 being an object made under Person class
get_height - returns the height of object, no arguments are needed just the object itself. While demonstrating method, implementation would look like Person1.get_height(), Person1 being an object made under Person class
get_eyes - returns the eye color of object, no arguments are needed just the object itself. While demonstrating method, implementation would look like Person1.get_eyes(), Person1 being an object made under Person class
get_hair - returns the hair color of object, no arguments are needed just the object itself. While demonstrating method, implementation would look like Person1.get_hair(), Person1 being an object made under Person class

There are five set methods, one for each data variable:
set_name - takes in one argument which is a name of the user's choosing. The input is then set and assigned as the object's name and the name is returned in the method, and if the name was set before it is changed to the input.
set_age - takes in one argument which is an age of the user's choosing. The input is then set and assigned as the object's name and the name is returned in the method, and if the name was set before it is changed to the input.
set_height - takes in one argument which is a height of the user's choosing. The input is then set and assigned as the object's name and the name is returned in the method, and if the name was set before it is changed to the input.
set_eyes - takes in one argument which is an eye color of the user's choosing. The input is then set and assigned as the object's name and the name is returned in the method, and if the name was set before it is changed to the input.
set_hair - takes in one argument which is a hair color of the user's choosing. The input is then set and assigned as the object's name and the name is returned in the method, and if the name was set before it is changed to the input.

The three other methods include:
ID - no arguments needed besides an object made under the class Person. This method returns a multi-lined string that shows all of the object's attributes listed in new lines and tabbed in to show the information. The method doesn't print so print() is needed to show the information.
birthyear - no arguments needed besides an object made under the class Person. This method returns an integer meant to show the birthyear of the object by using their age and the current year.
generation - no arguments needed besides an object made under the class Person. This method returns a string stating the object's name, age, and generation they were born in.

DEMO PROGRAM

The demo program for class Person is shown in the main code. In the main code I created three objects (x,y,z), two of which have already set attributes and the third being a randomized object. 
When the program is ran using python in terminal, 3 IDs are printed one for each object. Other attributes are printed like an object's age and two of their generations and I changed the object's name using set methods in the demo program.

Nothing else is needed to run the demo program, so you can just open the file using python in terminal and the information should appear. You can create your own objects by coding them in and using the Person class, whether or not you want to use the randomizer is up to you.
Also, if you were to test the demo program more than once, one of the printed IDs will be different each time since that is the randomized object.




