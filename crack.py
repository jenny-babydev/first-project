from string import ascii_letters
from itertools import product 

for passcode in product(ascii_letters, repeat=5):
    print(*passcode) 