# nums = [5,6,7,3,1, True, "Hello", 6.7,[6,8]]

# # nums[0] = 50

# # print(nums[0])

# # numbers = [5, 2, 7]
# # # numbers[3] = 100
# # numbers.append(100)

# # numbers.extend([5,6,8])


# # numbers.sort()

# # #удаляет элемент
# # # numbers.pop()
# # # numbers.remove(6)


# # print(numbers)
# # print(numbers.count(5))
# # print(len(numbers))


# for el in nums:
#     print(el)


n = int(input("Enter length: "))

user_list = []

i = 0
while  i < n:
    string = "Enter number#" + str(i) + ":"
    user_list.append(input(string))
    i += 1
print(user_list)