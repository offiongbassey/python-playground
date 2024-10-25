string = "aSb8"
print(bool(sum(1 for c in string if c.isalnum())))
print(bool(sum(1 for c in string if c.isalpha())))
print(bool(sum(1 for c in string if c.isdigit())))
print(bool(sum(1 for c in string if c.islower())))
print(bool(sum(1 for c in string if c.isupper())))

#The for loop iterates through string, the if statement checks if the type of string exist
# sum adds 1 each time the validation is True
#bool returns True if the sum has 1 and above or False if the sum is zero (0)