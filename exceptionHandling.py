def div(a, b):
    ans = a / b
    return ans


try:
    x = int(input("Enter x value"))
    y = int(input("Enter y value"))
    result = div(x, y)
    print(result)
except ZeroDivisionError:
    print("err")
    y = int(input("Enter non zero value for y"))
    if y == 0:
        raise ZeroDivisionError
    else:
        result = div(x, y)
        print(result)
except ValueError:
    print("Entered value is not integer")
else:
    print("No errors in code")
finally:
    print("Program ends")
