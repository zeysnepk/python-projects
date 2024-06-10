#Printing only numbers in the string of the list

liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        print(int(i))
    except ValueError:
        continue  #pass
    
    
#Write a function that queries whether a number is even. This function returns *return* if the number is even. However, if the number is odd, the function throws a *ValueError* error with *raise*. Then, define a list of even and odd numbers and scroll through the list to print only the even numbers on the screen.

def evenORodd(num):
    if num % 2 == 0:
        return num
    
    else:
        raise ValueError(num,"is not even!")

num = int(input("Enter a number: "))
print(evenORodd(num))


    
Alist = [38,17,22,24,33,31,39]

for j in Alist:
    try:
        print(evenORodd(j))
    except ValueError:
        pass


