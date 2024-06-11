#append Function
nums = [1,2,3,4,5,6,7]
nums.append("Hi")

print(nums)

#extend() Function --> adds another list's values to a list
nums = [1,2,3,4,5,6,7]
nums.extend([8,9,10])
print(nums)

#insert() Function --> adds a value to given index
nums = [1,2,3,4,5,6,7]
nums.insert(2,"Hi")
print(nums)

#pop() Function --> removes a value in given index from a list
nums = [1,2,3,4,5,6,7]
print(nums.pop())
print(nums.pop(3))
print(nums)

#remove() Function --> removes the given value
langs = ["Python","Java","C","Php"]
print(langs.remove("Python"))
print(langs)

#index() Function --> finds the index from a given value 
nums = [1,2,3,4,3,5,6,3,7]
print(nums.index(3)) #starts to find at the beginning
print(nums.index(3,3)) #starts to find from 3th value

#count() Function
nums = [1,2,1,1,3,4,1,1,3,5,6,3,7]
print(nums.count(1))
print(nums.count(10))

#sort() Function
nums = [1,2,1,1,3,4,1,1,3,5,6,3,7]
nums.sort()
print(nums)

nums.reverse()
print(nums)

nums = [1,2,1,1,3,4,1,1,3,5,6,3,7]
nums.sort(reverse = True)
print(nums)

langs = ["Python","Java","C","Php"]
langs.sort()
print(langs)

langs = ["Python","Java","C","Php"]
langs.sort(reverse = True)
print(langs)



