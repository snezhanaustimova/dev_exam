import requests
import re
from django import forms


# Функция для проверки ввода пользователя
def validate_input(user_input):
    # Проверка на наличие подозрительных символов
    if re.search(r'(\'|;|\")', user_input):
        raise forms.ValidationError("Suspicious characters found")

    # Проверка на наличие SQL-инъекций
    compile = re.compile(r'(SELECT|INSERT|UPDATE|DELETE|WHERE|HAVING|ORDER|BY|LIMIT)')
    if re.match(compile, user_input.upper()):
        raise forms.ValidationError("Suspicious SQL queries found")

    # Проверка длины ввода
    if len(user_input) > 35:
        raise forms.ValidationError("The maximum input length has been exceeded")

    # Проверка формата ввода
    compile = re.compile(r'[\w\d\-_\.\@\#]+$')
    if not re.match(compile, user_input):
        raise forms.ValidationError("The input contains invalid characters")

    # Проверка на словарные атаки
    if user_input.lower() in ["admin", "password", "root", "default", "guest"]:
        raise forms.ValidationError("The input is a dictionary word")
    
    return user_input