#from arithmetic import add, subtract
#
#result_add = add(5, 3)
#result_subtract = subtract(10, 4)
#print(f"Addition Result: {result_add}")  # Output: 8
#print(f"Subtraction Result: {result_subtract}")  # Output: 6

#import arithmetic as math
#rest = math.add(5, 3)
#print(f"Addition Result: {rest}")  # Output: 8

#from random import randint, choice
#
#items = ['apple', 'banana', 'cherry', 'date']
#
#def random_fruit(fruit):
#    if not fruit:
#        return "The fruit list is empty."
#    return choice(fruit)
#
#fruit = random_fruit(items)
#print(f"Randomly selected fruit: {fruit}")



#from datetime import datetime, timedelta
#now = datetime.now()
#print(now)  # Output: Current date and time
#
#
#future_date = now + timedelta(days=7)
#print(f"Date after 7 days: {future_date}")  # Output: Date after
#
#formatted_date = future_date.strftime("%m-%d-%Y %H:%M:%S")
#print(f"Formatted Date: {formatted_date}")  # Output: Formatted Date: 2023-10-15 14:30:00

from pathlib import Path

#path = Path("example.txt")
#path=Path("./example.txt")
#
#contents = path.read_text()
#print(contents.upper())  # Output: Contents of example.txt



#mycontents = "This is a new content for the file."
#mycontents += "\nThis is an additional line."   
#mycontents += "\nThis is yet another line."
#path = Path("new_example.txt")
#path.write_text(mycontents)
#
#with Path.open("new_example.txt", "r") as file:
#    contents = file.read()
#    print(contents)  # Output: Contents of new_example.txt
    
    
#try:
#    with Path.open("new_example2.txt", "r") as file:
#        contents = file.read()
#        print(contents)  # Output: Contents of new_example.txt
#except FileNotFoundError:
#    print("The file does not exist.")


#try:
#    print(10 / 0)  # This will raise a ZeroDivisionError
#    print("Division successful.")
#except ZeroDivisionError:
#    print("You cannot divide by zero!")  # Output: You cannot divide by zero!
#finally:
#    print("This block will always execute.")  # Output: This block will always execute.


class MyCustomError(Exception):
    """A custom exception class for demonstration purposes."""
    pass

class AnotherCustomError(MyCustomError):
    """A more specific custom exception class."""
    pass

def check_value(number):
    if number < 5:
        raise MyCustomError("Number is less than 5.")
    elif number > 10:
        raise AnotherCustomError("Number is greater than 10.")
    else:
        print(f"{number} is within the acceptable range.")

try:
    check_value(3)  # This will raise MyCustomError
except MyCustomError as e:
    print(f"Caught an error: {e}")
    