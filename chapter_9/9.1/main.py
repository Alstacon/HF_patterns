from sentences import Sentence, SentenceSet, SentenceDict


def iter_sentence():
    sentence = Sentence('''I don't want to set the world on fire.''')
    for word in sentence:
        print(word)
    print('-' * 10)

    sentence = SentenceDict({
        'first word': 'People',
        'second word': 'are',
        'third word': 'strange'
    })
    for word in sentence:
        print(word)
    print('-' * 10)

    sentence = SentenceSet({'Padam', 'padam', 'padam'})
    for word in sentence:
        print(word)
    print('-' * 10)


if __name__ == '__main__':
    iter_sentence()
