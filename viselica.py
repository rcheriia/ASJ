from random import choice
from main import print_text

def hangman():
    HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |    |
         | 
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   
         |   
         |     
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |   
         |   
        ----------
        """
    )

    max_wrong = len(HANGMAN) - 1
    words = ('Решётка', 'Квартира', 'Дельфинарий', 'Непогода', 'Вход', 'Полиция', 'Перекрёсток', 'Башня', 'Стрелка', 'Градусник', 'Бутылка', 'Щипцы', 'Наволочка', 'Павлин', 'Карточка', 'Записка', 'Лестница', 'Переулок', 'Сенокос', 'Рассол', 'Закат', 'Сигнализация', 'Журнал', 'Заставка', 'Тиранозавр', 'Микрофон', 'Прохожий', 'Квитанция', 'Пауза', 'Новости', 'Скарабей', 'Серебро', 'Творог', 'Осадок', 'Песня', 'Корзина', 'Сдача', 'Овчарка', 'Хлопья', 'Телескоп', 'Микроб', 'Угощение', 'Экскаватор', 'Письмо', 'Пришелец', 'Айсберг', 'Пластик', 'Доставка', 'Полка', 'Билет', 'Вторник', 'Льдина', 'Интерес', 'Троллейбус', 'Футболист', 'Лисёнок', 'Пример')  # Слова для угадывания

    word = choice(words)  # Слово, которое нужно угадать
    so_far = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
    wrong = 0  # Количество неверных предположений, сделанных игроком
    used = []  # Буквы уже угаданы

    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong])  # Вывод висельника по индексу
        print("\nВы использовали следующие буквы:\n", used)
        print("\nНа данный момент слово выглядит так:\n", so_far)

        guess = input("\n\nВведите свое предположение: ")  # Пользователь вводит предполагаемую букву

        while guess in used:
            print("Вы уже вводили букву", guess)  # Если буква уже вводилась ранее, то выводим соответствующее сообщение
            guess = input("Введите свое предположение: ")  # Пользователь вводит предполагаемую букву

        used.append(guess)  # В список использованных букв добавляется введённая буква

        if guess in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
            print("\nДа!", guess, "есть в слове!")
            new = ""
            for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nИзвините, буквы \"" + guess + "\" нет в слове.")  # Если буквы нет, то выводим соответствующее сообщение
            wrong += 1

    if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
        print(HANGMAN[wrong])
        print("\nКолдун повесил тебя и превратил в камень!")
        print_text('Попробуем снова? (да/нет)')
        k = input()
        while k not in ['да', 'нет']:
            print_text('Попробуем снова? (да/нет)')
        if k == 'да':
            hangman()
        if k == 'нет':
            print_text('Ты же ещё вернёшься спасти наш мир? В любом случае, удачи тебе!')
    else:  # Если кол-во ошибок не превышено, то игрок выиграл
        print("\nВ этом раунде ты обыграл колдуна! Пойдём дальше")

    print("\nЗагаданное слово было \"" + word + '\"')


hangman()