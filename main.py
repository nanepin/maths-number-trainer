def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def check_ans(correct, user):
    if correct == user:
        print("Correct!")
    
    else:
        print("Wrong!")

def add_game():
    first = int(input("First number: "))
    second = int(input("Second number: "))
    ans = addition(first, second)
    user_attempt = int(input("Your answer: "))
    check_ans(ans, user_attempt)

def multiply_game():
    first_ = int(input("First number: "))
    second_ = int(input("Second number: "))
    numbers = [first_, second_]
    ans = multiplication(first_, second_)
    user_attempt = int(input("Your answer: "))
    check_ans(ans, user_attempt)

while True:
    print("Welcome to number trainer")

    print("1. Addition")
    print("2. Multiplication")
    print("3. Exit")

    option = int(input("Choose option: "))

    if option == 1:
        add_game()
        
    elif option == 2:
        multiply_game()

    elif option == 3:
        break

        



        
