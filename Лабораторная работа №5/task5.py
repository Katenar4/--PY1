import string
from random import sample


def get_random_password(n=8) -> str:
    alphabet = str(string.ascii_letters + string.digits)
    return "".join(sample(alphabet, n))


print(get_random_password())
