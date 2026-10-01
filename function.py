def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


formated_name = format_name(first_name="john", last_name="doe")  # Output: John Doe

##print(formated_name)

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.
    
    Args: 
        a (int or float): The first number.
        b (int or float): The second number.
    """
    return a * b

result = multiply(5, 3)
#print(result)  # Output: 15

def build_profile(first, last):
    """ Build a dictionary containing information about a person."""
    user = {
        'first_name': first,
        'last_name': last,
    }
    return user

user_profile = build_profile('albert', 'einstein')
#print(user_profile)  # Output: {'first_name': 'albert', 'last_name


def sum_numbers(*args):
    """ Returns the sum of all numbers passed as arguments."""
    return sum(args)

def build_profile(first, last, **user_info):
    """ Build a dictionary containing information about a person."""
    user = {
        'first_name': first,
        'last_name': last,
    }
    user.update(user_info)
    return user

print(build_profile('albert', 'einstein', age=45, location='princeton'))