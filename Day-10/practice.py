# Warm-up 1: Nested list indexing
l = [[[1,2],[3,4]],[[5,6],[7,8]]]
l[0][0][-1]


# Warm-up 2: Basic inline even/odd list comprehension
l = ['even' if x%2 == 0 else 'odd' for x in range(10)]
l


# Warm-up 3: Cubes from 1 to 10
cubes = [x**3 for x in range(1,11)]
print(cubes)


# Warm-up 4: Odd numbers from 1 to 20
odd = [x for x in range(1,21) if x%2 != 0]
print(odd)


# Warm-up 5: Filtering languages starting with 'p'
lang = ["python", "java", "c++", "php"]
up_lang = [i for i in lang if i[0] == 'p']
print(up_lang)


# Warm-up 6: Filtering numbers greater than 30
n = [12, 55, 8, 90, 33]
new_n = [i for i in n if i>30]
print(new_n)


# Warm-up 7: Basket and Cart intersection starting with 'a'
basket = ['apple','banana','mango']
my_cart = ['apple','peach','grapes','anar']
nb = [i for i in my_cart if i in basket and i.startswith('a')]
print(nb)

