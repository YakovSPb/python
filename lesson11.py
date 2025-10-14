# data = set('hello')
data = {5, 7, 4, 4, 4}

data.add(32)
data.update(['32',True, 3,65])
data.remove(True)


nums = [5, 7, 3, 5, 5]

nums = set(nums)

print(data)


new_data = frozenset([5,6,7,'32',3,4])

print(nums)