#Write a Python program to guess a number between 1 to 9

n = int(input('enter the number : '))

if n <= 0:
    print("take another value")
else:
    for i in range(1,10):
        if i == n:
            print(i,'your guess is correct')
        print()
