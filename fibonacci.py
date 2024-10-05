def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms: {fibonacci_series(num_terms)}")
