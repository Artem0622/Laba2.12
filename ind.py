def decor(func):
    def wrapper(*args):
        a1, a2 = func(*args)
        return dict(zip(a1, a2))

    return wrapper


def make_two_list(s1, s2):
    return s1.split(), s2.split()


s1 = 'Вася Коля Маша Аня Таня'
s2 = 'мальчик мальчик девочка девочка девочка'

print(make_two_list(s1, s2))
