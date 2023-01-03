import random


def login_to_messenger():
    random_int = random.randint(1, 10)
    if random_int < 9:
        return True
    return False