country_capital_dict = {
    "Россия": "Москва",
    "Китай": "Пекин",
    "США": "Вашингтон",
    "Канада": "Оттава",
    "Япония": "Токио",
    "Южная Корея": "Сеул",
    "Великобритания": "Лондон",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Норвегия": "Осло",
    "ОАЭ": "Дубай",
    "Испания": "Мадрид",
    "Италия": "Рим"
}

erudite_dict = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ",
}

student_lang_dict = {
    "Алексей": ["Русский язык", "Английский язык", "Китайский язык"],
    "Роман": ["Русский язык", "Английский язык", "Итальянский язык"],
    "Амир": ["Русский язык", "Испанский язык"],
    "Алдар": "Английский язык",
    "Петр": ["Китайский язык", "Арабский язык", "Французский язык"]
}


def all_couples(): # Начало задания 6.1
    for i in country_capital_dict:
        print(i+":", country_capital_dict[i])


def get_capital(country):
    if country in country_capital_dict.keys():
        print(country_capital_dict.get(country))
    else:
        print("Такой страны не существует")


def sorted_dict():
    sorted_list = sorted(country_capital_dict.items())
    for i in sorted_list:
        print(i)


def word_total(text):  # Начало задания 6.2
    print(sum(
        [k for i in text for k, v in erudite_dict.items() if i in v]
    ))


def all_language():  # Начало задания 6.3
    lang_set = set()
    for i in student_lang_dict.values():
        if type(i) is not list:
            lang_set.add(i)
        else:
            for j in i:
                lang_set.add(j)

    return lang_set


def count_of_lang():
    print("Количество языков, которые знают студенты: ", len(all_language()))


def sorted_set():
    print(sorted(all_language()))


def xi_lang_student():
    print("Студенты, которые знают Китайский язык: ")
    for i in student_lang_dict.values():
        if "Китайский язык" in i:
            print(" ", get_key(student_lang_dict, i))


def get_key(d, value):  # Функция для получения ключа по значению
    for k, v in d.items():
        if v == value:
            return k


print("Задание 6.1\n")
all_couples()  # a)
get_capital(input("Введите страну: "))  # b)
sorted_dict()  # c)

print("\n")

print("Задание 6.2\n")
word_total(input("Введите слово: ").upper())

print("\n")

print("Задание 6.3\n")
count_of_lang()
sorted_set()
xi_lang_student()