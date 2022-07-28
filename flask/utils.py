import random
import string

from faker import Faker

fake = Faker()
import requests


def get_password(length: int = 10) -> str:
    """
    generate password
    """

    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars)

    return password


def requirements_return():
    with open('requirements.txt') as file:
        result = file.read()
        return str(result)


def get_fake(quantity):
    result = {}
    for i in range(quantity):
        result[i] = {}
        result[i]['name'] = fake.name()
        result[i]['email'] = fake.email()
    return str(result)


def astronavt_get():
    r = requests.get('http://api.open-notify.org/astros.json')
    j = r.json()
    n = j['number']
    return str(n)

def average_all():
    import csv
    file = open('hw.csv')
    csvreader = csv.reader(file)
    height = 0
    weight = 0
    total_el = 0
    k_1 = float(2.54)
    k_2 = float(0.454)
    next(csvreader)
    for row in csvreader:
        if len(row) != 3:
            continue
        height += float(row[1])
        weight += float(row[2])
        total_el += 1
    final_height = (height / total_el) * k_1
    final_weight = (weight / total_el) * k_2
    return (f'Average height: {round(final_height)} cm, '
              f'Average weight: {round(final_weight)} kg.')