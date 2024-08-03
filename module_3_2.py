def invalid_email(email):
    if type(email) != str:
        return True
    if email.count('@') != 1:
        return True
    if (email[-4:].lower() != '.com'
            and email[-3:].lower() != '.ru'
            and email[-4:].lower() != '.net'):
        return True
    return False


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if invalid_email(recipient) or invalid_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
        return
    if sender.lower() == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
