import random
from googletrans import Translator
import sys


def ja(translator, Language):
    global IN
    global SRC
    if IN[1] == 'ja':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='ja').text]
    print(f'{Language[SRC[0]]} < 日本語', IN[0])
    SRC[0] = 'ja'
    IN.append(SRC[0])
    return IN


def en(translator, Language):
    global IN
    global SRC
    if IN[1] == 'en':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='en').text]
    print(f'{Language[SRC[0]]} < 英語', IN[0])
    SRC[0] = 'en'
    IN.append(SRC[0])
    return IN


def de(translator, Language):
    global IN
    global SRC
    if IN[1] == 'de':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='de').text]
    print(f'{Language[SRC[0]]} < ドイツ語', IN[0])
    SRC[0] = 'de'
    IN.append(SRC[0])
    return IN


def es(translator, Language):
    global IN
    global SRC
    if IN[1] == 'es':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='es').text]
    print(f'{Language[SRC[0]]} < スペイン語', IN[0])
    SRC[0] = 'es'
    IN.append(SRC[0])
    return IN


def fr(translator, Language):
    global IN
    global SRC
    if IN[1] == 'fr':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='fr').text]
    print(f'{Language[SRC[0]]} < フランス語', IN[0])
    SRC[0] = 'fr'
    IN.append(SRC[0])
    return IN


def ko(translator, Language):
    global IN
    global SRC
    if IN[1] == 'ko':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='ko').text]
    print(f'{Language[SRC[0]]} < 韓国語', IN[0])
    SRC[0] = 'ko'
    IN.append(SRC[0])
    return IN


def ru(translator, Language):
    global IN
    global SRC
    if IN[1] == 'ru':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='ru').text]
    print(f'{Language[SRC[0]]} < ロシア語', IN[0])
    SRC[0] = 'ru'
    IN.append(SRC[0])
    return IN


def uz(translator, Language):
    global IN
    global SRC
    if IN[1] == 'uz':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='uz').text]
    print(f'{Language[SRC[0]]} < ウズベク語', IN[0])
    SRC[0] = 'uz'
    IN.append(SRC[0])
    return IN


def el(translator, Language):
    global IN
    global SRC
    if IN[1] == 'el':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='el').text]
    print(f'{Language[SRC[0]]} < ギリシャ語', IN[0])
    SRC[0] = 'el'
    IN.append(SRC[0])
    return IN


def mt(translator, Language):
    global IN
    global SRC
    if IN[1] == 'mt':
        return IN
    IN = [translator.translate(IN[0], src=IN[1], dest='mt').text]
    print(f'{Language[SRC[0]]} < マルト語', IN[0])
    SRC[0] = 'mt'
    IN.append(SRC[0])
    return IN


def main():
    global IN
    global SRC
    #global translator
    translator = Translator()
    Lang = [ja, en, de, es, fr, ko, ru, uz, el, mt]
    Language = {
        "en": "英語",
        "de": "ドイツ語",
        "es": "スペイン語",
        "fr": "フランス語",
        "ko": "韓国語",
        "ru": "ロシア語",
        "uz": "ウズベク語",
        "el": "ギリシャ語",
        "ja": "日本語",
        "mt": "マルト語"
    }
    try:
        f = open(sys.argv[1], 'r', encoding='UTF-8')
        IN = [f.read()]
        f.close()
    except:
        IN = [input("文章を入力>>>")]
    L = translator.detect(IN[0]).lang
    print(f"入力言語を推論>>>{Language[L]}")
    try:
        SRC = [L, sys.argv[2]]
        IN.append(SRC[0])
    except:
        SRC = [L, L]
        IN.append(SRC[0])
    if not IN[0]:
        return -1
    random.shuffle(Lang)
    for i in Lang:
        IN = i(translator, Language)
    IN = translator.translate(IN[0], src=IN[1], dest=SRC[1]).text
    try:
        f = open(sys.argv[3], 'w', encoding='UTF-8')
        f.write(IN)
        f.close()
    except:
        print(IN)


if __name__ == '__main__':
    main()
