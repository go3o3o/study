### iSharp 
code = input()
s = code[:-1].replace(',', '').split()

data_type = s[0]
for i in range(1, len(s)):
    if s[i].isalpha():
        print(data_type, s[i] + ';')
    else:
        for j in range(0, len(s[i])):
            if not s[i][j].isalpha():
                print(data_type + s[i][:j-1:-1].replace('][', '[]'), s[i][:j] + ';')
                break