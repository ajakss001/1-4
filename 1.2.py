def swap_first_last_pop(lst):
    if len(lst) < 2:
        return lst
    first = lst.pop(0)
    last = lst.pop(-1)
    lst.insert(0, last)
    lst.append(first)
    return lst

sample_list_3 = ['a', 'l', 'f', 'd']
print(swap_first_last_pop(sample_list_3))