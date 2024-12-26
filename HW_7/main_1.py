def say_hi(name, age):
    """
    Returns a greeting with the name and age.

    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.

    Returns:
    str: A greeting with the name and age.
    """
    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('OK')
