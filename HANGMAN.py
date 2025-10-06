from random import *
word_list = [
    "год",
    "человек",
    "время",
    "дело",
    "машина",
    "вода",
    "отец",
    "проблема",
    "час",
    "право",
    "нога",
    "решение",
    "дверь",
    "образ",
    "история",
    "власть",
    "закон",
    "война",
    "бог",
    "голос",
    "тысяча",
    "книга",
    "возможность",
    "результат",
    "ночь",
    "стол",
    "имя",
    "область",
    "статья",
    "число",
    "компания",
    "народ",
    "жена",
    "группа",
    "развитие",
    "представление",
    "солдат",
    "художник",
    "волос",
    "оружие",
    "соответствие",
    "ветер",
    "парень",
    "зрение",
    "генерал",
    "огонь",
    "понятие",
    "строительство",
    "ухо",
    "грудь",
    "нос",
    "страх",
    "услуга",
    "содержание",
    "радость",
    "безопасность",
    "продукт",
    "комплекс",
    "бизнес",
    "сад",
    "сотрудник",
    "лето",
    "курс",
    "предложение",
    "рот",
    "технология",
    "реформа",
    "отсутствие",
    "собака",
    "камень",
    "будущее",
    "рассказ",
    "контроль",
    "река",
    "продукция",
    "сумма",
    "техника",
    "здание",
    "сфера",
    "необходимость",
    "фонд",
    "подготовка",
]

def get_word():
    result = choice(word_list).upper()
    return result

def display_hangman(tries):
    stages = [ 
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=" ")
        else:
            print("_", end=" ")
    print()

def play(word):
    word_completion = "_" * len(
        word
    )  
    guessed = False  
    guessed_letters = []  
    guessed_words = []  
    tries = 6
    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    while True:
        char = input("Напишите вашу букву! \n").upper()
        while not char.isalpha():
            char = input("Это не похоже на букву \n")
            continue
        if char in guessed_words or char in guessed_letters:
            print("Снова это написал(")
            continue
        if len(char) > 1:
            if char == word:
                print("Поздравляем, вы угадали слово! Вы победили!")
                break
            else:
                guessed_words.append(char)
                tries -= 1
                print(f"Не верно, осталось попыток {tries}")
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f"Вы не смогли угадать слово: {word}")
                    break
                continue

        if char in word:
            guessed_letters.append(char)
            for c in word:
                if c not in guessed_letters:
                    print("Угадали букву")
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print_word(word, guessed_letters)
                print("Поздравляем, вы угадали слово! Вы победили!")
                break
        else:
            guessed_letters.append(char)
            tries -= 1
            print(f"Не верно, осталось попыток {tries}")
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f"Вы не смогли угадать слово: {word}")
            break
        
play(get_word().upper())
