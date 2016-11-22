import re


def phone_numbers(text):
    numbers = re.compile(r'(\(\d{3}\) \d{3}-\d{4})')
    numbers.findall(text)
    return numbers.findall(text)
