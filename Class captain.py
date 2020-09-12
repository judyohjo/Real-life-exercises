'''
Randomly select two names to be class captains for the term.
'''

import random

random_name = []
roster = ['Ben', 'Alice', 'Henry', 'Sam', 'Jane', 'Kim', 'Dan', 'Clara', 'Tim', 'Michelle', 'Jim']
for i in range(0, 2):
    random_num = random.randrange(0, len(roster)-1)
    random_name.append(roster[random_num])
if random_name[0] != random_name[1]:
        print(random_name[0], "and", random_name[1], "are class captains for the term.")
