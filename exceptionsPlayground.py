
print("Welcome to ITI package")
print(name)
print("0000000000000000000000")
r = 3
x = 10
print(r+x)


def sum_num() -> int:
    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter a number: "))
    except Exception as e:
        print(f"--- problem happened {e}")
        return False
    else:
        return num1 + num2
    finally:
        print("--- Process completed ")
    print("------------- process completed successfully")


print(sum_num())
