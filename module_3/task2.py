def is_correct_email(email):
    if '@' not in email:
        return False
    return email.endswith(".com") or email.endswith(".ru") or email.endswith(
        ".net")  # .endswith нашёл на просторах интернета, проверяет окончание введённых данных


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if sender == recipient:
        print('Невозможно отправить письмо самому себе!')
        return

    if not is_correct_email(sender) or not is_correct_email(recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!!! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Проверка работы кода', 'agamerson05@mail.ru')

send_email('НЕ мошенники', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Попытка отправить сообщение', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Нужно поставить себе напоминание', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
