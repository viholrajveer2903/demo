square = lambda x: x**2
print(square(5)) 

reverse = lambda x: x[::-1]
print(reverse("hello")) 

maximum = lambda x, y: x if x > y else y
print(maximum(3, 7)) 

lst = [(1, 4), (2, 6), (3, 1)]
sort_lst = sorted(lst, key=lambda x: x[1])
print(sort_lst) 

lst = [1, 2, 3, 4, 5, 6]
even_lst = list(filter(lambda x: x % 2 == 0, lst))
print(even_lst) 
