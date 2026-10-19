#1
def countdown(number):
    if number == 0:
        print("Time's up!")
        return
    print(number)
    countdown(number - 1)

countdown(5)

#2
def build_and_unwind(level):
    if level == 0:
        print("Base case reached. Now unwinding begins.")
        return
    print("Building level:", level)
    build_and_unwind(level - 1)
    print("Unwinding level:", level)

build_and_unwind(3)

#3
def count_up(number, limit=10): #here number is the starting point(where countdown has to start) and limit is the ending point 
    if number > limit:
        return
    print(number)
    count_up(number + 1, limit)

count_up(1, 5) #count from 1 to 5

#4
def factorial(number):
    # Base Case
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

print("5! =", factorial(5))


#5: STACK OVERFLOW SAFETY DEMO
# If a recursive function does not have a base case, it keeps calling itself and may cause a stack overflow. Do not run this function unless you understand the risk.

#def factorial(number):
#     return number * factorial(number - 1)