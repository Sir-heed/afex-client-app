import string
import random

def get_random_string(length):
    # choose from all letter and digits
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str