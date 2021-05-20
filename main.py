
lst1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lst2 = lst1
lst2.sort()
print(lst2)

lst3 = lst1
lst3.sort(reverse=True)
print(lst3)

lst_to_tuple = tuple(lst2)
x = slice(0, 9, 2)
print(lst_to_tuple[x])

y = slice(1, 9, 2)
print(lst_to_tuple[y])

result = list(filter(lambda x: (x % 3 == 0), lst1))
print(result)
