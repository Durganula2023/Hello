# mymodule.py file
import random


def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

print(generate_full_name('Durga','Bhavani'))

from random import *

def random_user_id():
    return random.randint('11a2345','90b879')

print(random_user_id())