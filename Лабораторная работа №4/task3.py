def delete(list_, index=None):
    if index is not None:
        first_part = list_[:index]
        second_part = list_[index+1:]

        return first_part + second_part

    else:
        list_.remove(list_[-1])

        return list_


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
