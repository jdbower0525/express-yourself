import textminer.validator as v
import re


def words(number):
    if v.words(number):
        return number.split(' ')
    else:
        return None


def phone_number(number):
    if v.phone_number(number):
        num = re.sub(r'[^0-9]', '', number)
        return {"area_code": num[:3], "number": num[3:6]+'-'+num[6:]}


def money(number):
    if v.money(number):
        mon = re.sub(r'[\,]', '', number)
        return {'currency': mon[0], 'amount': float(mon[1:])}


def zipcode(number):
    zipcode = {}
    try:
        regex = re.match(r"^(\d{5})\-?(\d{4})?$", number).groups()
        zipcode["zip"] = regex[0]
        if regex[1]:
            zipcode["plus4"] = regex[1]
        else:
            zipcode["plus4"] = None
        return zipcode
    except:
        return None


def date(number):
    dates = {}
    try:
        match = re.match(r"(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})",
                         number).groups()
        if len(match[0]) < 4:
            dates["month"] = int(match[0].lstrip('0'))
            dates["day"] = int(match[1].lstrip('0'))
            dates["year"] = int(match[2])
        else:
            dates["year"] = int(match[0])
            dates["month"] = int(match[1].lstrip('0'))
            dates["day"] = int(match[2].lstrip('0'))
        return dates
    except AttributeError:
        return None
