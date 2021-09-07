#1) Print all integers from 0 to 150
for i in range(0,150,1):
    print(i)

#2) Print all multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print(i)

#3) Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".


def dojo():
    for i in range(1, 101, 1):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)


dojo()

#4) Add odd integers from 0 to 500,000, and print the final sum.


def huge():
    final_sum = 0
    for i in range(1, 500000, 2):
        final_sum += i
    print(final_sum)


huge()

#5) Print positive numbers starting at 2018, counting down by fours.


def countdown():
    for i in range(2018, 0, -4):
        print(i)


countdown()

#6) Set three variable: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.


def counter(low_num, high_num, mult):
    for i in range(low_num, high_num + 1):
        if i % mult == 0:
            print(i)


counter(2, 9, 3)
