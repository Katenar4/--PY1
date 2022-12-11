from random import sample


def get_unique_list_numbers() -> list[int]:
    list_ = range(-10, 11)
    return sample(list_, 15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
