# Functions & Fibonacci Sequence

def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    fib_sequence = [0] * (n + 1)
    return fib_sequence
  else:
    fib_sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, n + 1):
      c = a + b
      fib_sequence.append(c)
      a, b = b, c
    return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)