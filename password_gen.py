# Random password generator

import random
import array

MAX_LEN = 14

DIGITS = ['1','2','3','4','5','6','7','8','9','0']

UPPER_CASE = ['A','B','C','D','E','F','G','H','I','J',
               'K','L','M','N','O','P','Q','R','S','T',
               'U','V','W','X','Y','Z']

LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
    
SYMBOLS = ['!','@','#','$','%','^','&','*','(',')','-','+','=','|','<','>','?','/']


COMBINED_PWD = DIGITS + UPPER_CASE + LOWER_CASE + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_uprcase = random.choice(UPPER_CASE)
rand_low = random.choice(LOWER_CASE)
rand_sym = random.choice(SYMBOLS)

TEMP_PASS = rand_digit + rand_uprcase + rand_low + rand_sym

for x in range(MAX_LEN -4 ) :
    TEMP_PASS = TEMP_PASS + random.choice(COMBINED_PWD)

    temp_pass_list = array.array('u', TEMP_PASS)
    random.shuffle(temp_pass_list)

password = ""

for x in temp_pass_list :
    password = password + x

print("The generated password is : ", password)