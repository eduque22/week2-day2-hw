##Exercise 1 - Using given list, print out a filtered version of the list with only the numbers < 10

alist = [1,11,14,5,8,9]

# b_list = []
# for num in alist:
#     if num < 10:
#         b_list.append(num)
# print(b_list)

b_list = [num for num in alist if num < 10]
print(b_list)



##Exercise 2 - Merge and sort the two list below

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_3 = l_1 + l_2
l_3.sort()
print('Sorted list is: ', l_3)

#how to write in lc?
# l_3 = [l_1 + l_2].sort()
# print(l_3)
# l_3 = sorted([l_1 + l_2])
# print(l_3)


##Exercise 3 - Square every number from 1-15

squared = [i**2 for i in range(1,16)]
print(squared)



##Exercise 4 - using list comprehension and given list, print out a filtered list with only names that start with the letter 'a' - output should be titlecased and have no whitespace

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
a_list = []

# for name in names_list:
#     new_name = name.title().strip()
#     a_list.append(new_name)
# for name in a_list:
#     if 'A' in name:
#         last_list.append(name)
# print(last_list)

last_list = [name.title().strip() for name in names_list if name.title().strip()[:1] == 'A']
print(last_list)



##Exercise 5 - Print all prime numbers from 1-100

prime_list = []
for num in range(2,100 + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
print(prime_list)
