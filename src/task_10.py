# Создайте декоратор @is_palindrome, который проверяет,
# что аргумент функции является палиндромом
# (строкой, которая читается одинаково слева направо и справа налево).

def is_palindrome(func):
    def wrapper(string):
        if string.lower() != string[::-1].lower():
            raise ValueError("Argument must be a palindrome")
        return func(string)
    return wrapper


@is_palindrome
def reverse_string(string):
    return string[::-1]

print(reverse_string('racecar')) # "racecar"
print(reverse_string('Racecar')) # "racecaR"
print(reverse_string('hello')) # Выбрасывает исключение ValueError с сообщением "Argument must be a palindrome"
