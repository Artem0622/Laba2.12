def decorator(function):
    def wrapper(*args):
        ar1, ar2 = function(*args)
        return dict(zip(ar1, ar2))

    return wrapper


@decorator
def strings_to_lists(a1, a2):
    return a1.split(), a2.split()


s1 = 'a b c d f g h l k'
s2 = '1 2 3 4 5 6 7 8 9'
print(strings_to_lists(s1, s2))

