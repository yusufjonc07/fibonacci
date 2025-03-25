def fibonacci_generator(n):
    
    if not n.isnumeric():
        print(f"Error Message: {n} is not a number. Please, enter a number!")
        return False
    else:
        n = int(n)
    
    if n < 3:
        print(f"Error Message: {n} is not greater than 2.")
        return False
    
    a, b = 0, 1
    fibo_arr = [a, b]
   
    for _ in range(n - 2):
        a, b = b, a + b
        fibo_arr.append(b)  # Add each calculated Fibonacci number
    
    print(fibo_arr)
    return True

# basic testing
assert fibonacci_generator("7"), print("Not successfull")
assert fibonacci_generator("10"), print("Not successfull")
assert not fibonacci_generator("2"), print("Not successfull")
assert not fibonacci_generator("-3"), print("Not successfull")
assert not fibonacci_generator("hello"), print("Not successfull")

# example usage
fibonacci_generator(input("Please enter a number higher than 2: \n"))