def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail адресов
    valid_domains = [".com", ".ru", ".net"]

    # Объяснение кода:
    # Определение функции: Функция send_email принимает три аргумента — два обычных (message и recipient) и один именованный с параметром по умолчанию (sender).
    
    if ("@" not in sender or not any(sender.endswith(domain) for domain in valid_domains) or
        "@" not in recipient or not any(recipient.endswith(domain) for domain in valid_domains)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Объяснение кода:
    # Проверка корректности e-mail:
    # Проверяем, содержится ли символ @ в обоих адресах и заканчиваются ли они на допустимые домены (например, .com, .ru, .net).
    # Если проверка не проходит, выводим сообщение об ошибке.
    
    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Объяснение кода:
    # Проверка на отправку самому себе: Если адрес отправителя совпадает с адресом получателя, выводим соответствующее сообщение.
    
    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

    # Объяснение кода:
    # Проверка на отправителя по умолчанию:
    # Если адрес отправителя по умолчанию (university.help@gmail.com), выводим сообщение об успешной отправке.
    # В противном случае, выводим сообщение о нестандартном отправителе.

# Пример выполнения функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Объяснение кода:
# Примеры вызовов функции: В конце кода приведены примеры вызовов функции с различными параметрами.
