def say_hello():
    print("hello")
    
def say_hello_to(name):
    print("Hello {}".format(name))
    
def double(integer):
    return integer * 2

def last_first(first_name, last_name):
    return "{}, {}".format(last_name, first_name)

def is_dead(num_incorrect_guesses):
    if num_incorrect_guesses >= 6:
        return True
    else:
        return False
