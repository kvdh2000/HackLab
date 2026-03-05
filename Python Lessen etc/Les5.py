''' Modules '''

import math
import datetime
import random
# import antigravity
import random as r
from random import randint
import Voorbeeld

# print(Voorbeeld.optellen(1, 2))

# for i in range(10):
#     print(random.randint(0, 100))
#     print(random.randrange(0, 100, 2))


# print(math.sqrt(25))
# print(25 ** (1/2))
# print(math.floor(5.9))
# print(int(5.9))
# print(math.ceil(5.1))

# print(round(6.5))

# print(datetime.date(2022, 9, 29))

# print(r.randint(10, 20))
# print(randint(0, 10))

Voorbeeld.groeten()
print(Voorbeeld.optellen(5, 6))
Voorbeeld.randomgetal()


'''
Algemene opbouw van code:
Imports
Variables
Functies
    Code

https://pypi.org/

In console: py -m pip install [modulenaam]
'''

# from datetime import *
# from dateutil.relativedelta import *
# now = datetime.now()

# print(now)
# now += relativedelta(months=+1)
# print(now)

from openai import OpenAI