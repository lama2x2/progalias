try:
    JUNIOR_WORDS = set(map(str.rstrip, open("junior_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('junior_words.txt not found')

try:
    MIDDLE_WORDS = set(map(str.rstrip, open("middle_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('middle_words.txt not found')

try:
    SENIOR_WORDS = set(map(str.rstrip, open("senior_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('senior_words.txt not found')

try:
    VERBAL_WORDS = set(map(str.rstrip, open("verbal_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('verbal_words.txt not found')
