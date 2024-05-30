import string
def is_palindrome(text):
    text = text.lower()
    i = 0
    while i < len(text):
        if text[i] in string.punctuation + " ":
            text = text[:i] + text[i + 1:]
            i -= 1
        i += 1
    if text == text[::-1]:
        return True
    return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")