# for i in range(6):
#     print(i)

# word = 'Hello World!'

# count = 0

# for i in word:
#     if i == 'l':
#         count+=1

# print("Count:", count)

# i = 5

# isHasCar = True

# while isHasCar:
#     if input() == "Stop":
#         isHasCar = False

# for i in range(1,11):

#     if(i >= 5): 
#         break

#     if i % 2 == 0: continue

#     print(i)

found = None

for i in "hello":
    if i == 'l':
        found = True
        break
else:
    found = False

print(found)