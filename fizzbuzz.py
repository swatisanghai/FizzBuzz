
def fizz_buzz():
    for i in range(1, 101):  # Loop through numbers from 1 to 100
        
        if i % 3 == 0 and i % 5 == 0:  # Check if the number is divisible by both 3 and 5
            print("FizzBuzz")  # If divisible by both, print "FizzBuzz"
        elif i % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz")  # If divisible by 3, print "Fizz"
        elif i % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz")  # If divisible by 5, print "Buzz"
        else:
            print(i)  # If not divisible by 3 or 5, print the number itself

# Call the function to execute Fizz Buzz
fizz_buzz()
