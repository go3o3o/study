### 일곱 난쟁이

dwarf = [int(input()) for i in range(9)]
total = sum(dwarf)

for i in range(9):
    for j in range(i + 1, 9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            num1, num2 = dwarf[i], dwarf[j]

            dwarf.remove(num1)
            dwarf.remove(num2)

            dwarf.sort()
            print('\n'.join(str(i) for i in dwarf))
            break
    if len(dwarf) < 9:
        break

