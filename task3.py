def generate_fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence


if __name__ == "__main__":
    print("=== Fibonacci Sequence Generator ===")

    try:
        n = int(input("Enter the number of terms: "))

        result = generate_fibonacci(n)
        print("Fibonacci Sequence:")
        print(result)

    except ValueError:
        print("Error: Please enter a valid integer.")
