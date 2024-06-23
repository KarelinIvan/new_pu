def uppercase_input():
    """
    принимает на вход строку и возвращает ее со всеми заглавными буквами
    :return:
    """
    user_input = input("Введите текст: ")
    return user_input.upper()


uppercase_string = uppercase_input()
print(uppercase_string)


def capitalize_words_input():
    """
    делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
    :return:
    """
    user_input = input("Введите строку: ")
    return user_input.title()


capitalize_string = capitalize_words_input()
print(capitalize_string)
