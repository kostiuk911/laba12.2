def remove_value_from_list(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            lst.remove(lst[i+1])
            break
    return lst

list = [1, 2, 3, 4, 5]
value = 3
new_list = remove_value_from_list(list, value)
print(new_list)
