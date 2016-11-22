import re


def binary(number):
    return re.search(r'^[^2-9]', number)


def binary_even(number):
    return re.search(r'0$', number)


def hex(number):
    return re.search(r'^[0-9a-fA-F]+$', number)


def word(number):
    return re.search(r'^[\w-]+[a-zA-Z]+$', number)


def words(number, count=0):
    word_list = re.split(' ', number)
    if len(word_list) != count and count != 0:
        return False
    for new_word in word_list:
        if not word(new_word):
            return False
    return True


def phone_number(number):
    return re.search(r'^\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$', number)


def money(number):
    return re.search(r'^\$([0-9]+(,[0-9]{3})*)(\.[0-9]{2})?$', number)


def zipcode(number):
    return re.search(r'^[0-9]{5}(-[0-9]{4})?$', number)


def date(number):
    return re.match(r'^[0-9]{1,4}[/-][0-9]{1,2}[/-][0-9]{2,4}$', number)
