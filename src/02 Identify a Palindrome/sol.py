import re

def is_palindrome(phrase):
  # Implement palindrome check logic here
  list = ''.join(re.findall(r'[a-z]+', phrase.lower()))
  return (list[::-1]) == list