from utils import add_numbers, multiply_numbers

def main():
    a = 5
    b = 10
    result_sum = add_numbers(a, b)
    result_product = multiply_numbers(a, b)
    print(f"The sum of {a} and {b} is {result_sum}")
    print(f"The product of {a} and {b} is {result_product}")

if __name__ == "__main__":
    main()

