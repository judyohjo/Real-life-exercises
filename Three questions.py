'''
Pick three random questions from bank of questions (10 questions).
'''

import random

bank_of_qs = ["What is your favourite song?", "What colour do you like?",
      "What is your hobby?", "Where are you from?", "What is your favourite movie?",
      "What is your dream job?", "What did you last weekend?", "What is your favourite book?",
      "What is your favourite TV programme?", "Where is your hometown?"]


for i in range(0, len(bank_of_qs)):
    num_q1 = random.randrange(0, len(bank_of_qs))
    num_q2 = random.randrange(0, len(bank_of_qs))
    num_q3 = random.randrange(0, len(bank_of_qs))
if num_q1 != num_q2 != num_q3:
    print("First question:", bank_of_qs[num_q1])
    print("Second question:", bank_of_qs[num_q2])
    print("Third question:", bank_of_qs[num_q3])
    
