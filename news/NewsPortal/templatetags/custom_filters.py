from django import template

register = template.Library()

@register.filter()
def censor(sentence):
    sentence_words = sentence.split()
    for i,  sentence_word in enumerate(sentence_words):
        if  sentence_word == 'Cybertruck':
            sentence_words[i] = 'C*********'
    sentence = ' '.join(sentence_words)
    return sentence
