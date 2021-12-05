import first_name_list
import random
first_names = first_name_list.first_names1.split()
last_names = first_name_list.last_names1.split()
# print(first_names)
randname = random.choice(first_names) + " " + random.choice(last_names)