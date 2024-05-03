#printing elements of the array
nums = [1,2,3,4,5]
index = 0

while(index < len(nums)):
    print(nums[index])
    index += 1

#printing starts in while
index = 0
while (index < 10):
    index += 1
    print("* " * index)

#break 
while True:
    name = input("Enter your name(""enter 'q' to exit""): ")
    if name == 'q':
        print("Exiting the program...")
        break
    print("Your Name :",name)

#continue
num = list(range(15))
print(num)
i = 0

while i < len(num):
    i += 1
    if num[i-1] % 2 == 0:
        continue
    print(num[i-1])
    