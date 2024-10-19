def validation_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 50:
        raise ValueError("Age cannot be greater than 50")
