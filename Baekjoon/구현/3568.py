### iSharp
declaration = input()

for idx, value in enumerate(declaration.split()):
    if idx == 0:
        common = value
    else:
        name = ''
        first_alpha = False
        value = value[:-1]
        print(common, end = '')

        for word in reversed(value):
            if word == ']':
                print('[', end='')
            elif word == '[':
                print(']', end='')
            elif word.isalpha():
                if not first_alpha:
                    print(' ', end='')
                    first_alpha = True
                name = word + name
            else:
                print(word, end='')
        print(name, end ='')
        print(';')
            