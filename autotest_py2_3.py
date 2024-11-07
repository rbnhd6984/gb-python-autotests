
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

def calculate_word_value(word, char_values):
    points = 0
    for char in word.upper():
        for value, letters in char_values.items():
            if char in letters:
                points += value
    return points

chars = {
    1: "AEIOULNSTRАВЕИНОРСТ",
    2: "DGДКЛМПУ",
    3: "BCMPБГЁЬЯ",
    4: "FHVWYЙЫ",
    5: "KЖЗХЦЧ",
    8: "JXШЭЮ",
    10: "QZФЩЪ"
}

k = 'ноутбук'
word_value = calculate_word_value(k, chars)
print(word_value)
