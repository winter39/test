from CharacterNetTrain import load_test
from CharacterSegment import segment_character


class Character_Recognition():
    def __init__(self):
        num, imges = segment_character('./AZ04.png')
        str1 = [''] * num
        for i in range(num):
            str1[i] = load_test(imges[i])

        result = ''
        for i in range(num):
            result = result + str1[i]
        print('result：' + result)


result = Character_Recognition()
