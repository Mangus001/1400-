def is_palindrome(str_str):
    s_str = str_str.replace(' ', '').upper()
    return s_str == s_str[::-1]
print(is_palindrome("АРГЕНТИНА МАНИТ НЕГРА"))
print(is_palindrome("ПОТ КАК ПОТОП"))
print(is_palindrome("А  РОЗА УПАЛА НА ЛАПУ АЗОРА"))
