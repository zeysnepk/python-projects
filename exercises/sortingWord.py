#program that prints words separately

sentenceUser = input("Enter a sentence: ")

words = sentenceUser.split()
words.sort()

for i in words:
    print(i)