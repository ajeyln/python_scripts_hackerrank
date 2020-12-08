# Input Format
''' The input is read by the provided locked code template.
In the first line, there is a single integer n denoting the number of words.
In the second line, there are n space-separated lowercase words.'''

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if letter in ('aeiouy'):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1
    return score


n = int(input())
words = input().split()
print(score_words(words))