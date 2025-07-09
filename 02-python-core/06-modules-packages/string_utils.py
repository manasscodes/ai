# string_utils.py
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def is_palindrome(s):
    return s == s[::-1]