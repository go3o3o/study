### HTML 
import sys

line_size = 0
while True:
    try:
        for word in input().split():
            if word == '<br>':
                line_size = 0
                print()
            elif word == '<hr>':
                if line_size:
                    print('\n' + '-' * 80)
                else:
                    print('-' * 80)
                line_size = 0
            else:
                word_len = len(word)
                if line_size + word_len > 80:
                    line_size = word_len
                    print()
                    print(word, end='')
                else:
                    line_size += word_len
                    print(word, end='')
                if line_size + 1 > 80:
                    line_size = 0
                    print()
                else:
                    line_size += 1
                    print(' ', end='')
    except:
        break
