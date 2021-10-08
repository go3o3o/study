# https://leetcode.com/problems/reorder-data-in-log-files/

def noLambda(x):
    return x.split()[1], x.split()[0]

def reorderLogFiles(self, logs: [str]) -> [str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    # letters.sort(key=noLambda())
    return letters + digits