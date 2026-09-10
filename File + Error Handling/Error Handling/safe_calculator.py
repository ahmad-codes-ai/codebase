def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cant divide by 0"
    except TypeError:
        return "Invalid Input Type"
    except:
        return "Unknow Error Occured"


print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # Cannot divide by zero
print(safe_divide(10, "a"))    # Invalid input type