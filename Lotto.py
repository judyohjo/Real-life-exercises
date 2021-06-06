'''
Generate 6 lotto numbers!
'''

import random

lotto_num = ''
for i in range(6):
    number = random.randrange(0, 99)
    lotto_num += str(number) + ' '
print("This week's lotto winner!")
print()
print("*********************************")
print("Lotto number:", lotto_num)
print("*********************************")
print()
print("Congratulations to the winner!")


