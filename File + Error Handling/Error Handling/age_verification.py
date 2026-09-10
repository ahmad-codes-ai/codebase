def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 150:
        raise ValueError('Age seems too high')
    else:
        s = f"Valid Age: {age}"
        return s 

validate_age(25)    # Valid age: 25
validate_age(-5)    # Error: Age cannot be negative
validate_age(200)   # Error: Age seems too high