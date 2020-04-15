print('Hello! My name is lups.')
print('I was created in 2020.')
print('Please, remind me your name.')
n = str(input())
print('What a great name you have,', n)
print('Let me guess your age.')
print('Say me remainders of dividing your age by 3, 5 and 7.')
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
a = (rem3 * 70 + rem5 * 21 + rem7 * 15)% 105
print("Your age is ", a,';', "that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
num = int(input())
g = 0
while g <= num:
    print(g, "!")
    g += 1
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print('Why do we use methods?')
t1 = 'To repeat a statement multiple times.'
t2 = 'To decompose a program into several small subroutines.'
t3 = 'To determine the execution time of a program.'
t4 = 'To interrupt the execution of a program.'
print("1. To repeat a statement multiple times?")
print('2. To decompose a program into several small subroutines?')
print('3. To determine the execution time of a program?' )
print('4. To interrupt the execution of a program?')
x = int(input())
if str(x) != 2:
    while x != 2:
        print('Please, try again.')
        x = int(input('>'))
        continue
        if str(x) == 2:
            break
print('Completed, have a nice day!')
