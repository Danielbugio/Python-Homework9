print("select a number between 1 and 100")
select_number = int(input())
print("")
number = 1

while number != select_number:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        number = number + 1
    elif number % 3 == 0:
        print("fizz")
        number = number + 1
    elif number % 5 ==0:
        print("buzz")
        number = number + 1
    else:
        print(str(number))
        number = number + 1

print(number)
