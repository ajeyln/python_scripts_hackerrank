def minion_game(string):
    length = len(string)
    vowels = 'AEIOU'
    vowel_score = 0
    consonant_score = 0
    for i, char in enumerate(string):
        if vowels.count(char) == 1:
            vowel_score += length-i
        else:
            consonant_score += length-i
    
    if vowel_score == consonant_score:
        print("Draw")
    elif vowel_score > consonant_score:
        print("Kevin", vowel_score)
    else:
        print("Stuart", consonant_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)