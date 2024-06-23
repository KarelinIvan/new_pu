def uppercase_input():
    """
    принимает на вход строку и возвращает ее со всеми заглавными буквами
    """
    user_input = input("Введите текст: ")
    return user_input.upper()


uppercase_string = uppercase_input()
print(uppercase_string)
