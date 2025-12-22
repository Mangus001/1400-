def is_palindrome_number(number):
    s = str(number)
    return s == s[::-1]

print(is_palindrome_number(12321)) 
print(is_palindrome_number(12345)) 
