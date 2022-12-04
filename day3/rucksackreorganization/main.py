lowercases = {}
uppercases = {}

c = 1
for letter in 'abcdefghijklmnopqrstuvwxyz':
    lowercases[letter] = c
    c += 1

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    uppercases[letter] = c
    c += 1


def main():
    points = 0
    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            half = len(line) // 2
            first, second = line[half:], line[:half]
            inletter = set(first).intersection(second).pop()
            if inletter in lowercases:
                points += lowercases[inletter]
            if inletter in uppercases:
                points += uppercases[inletter]
    print(points)


if __name__ == '__main__':
    main()
