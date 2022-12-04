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
        c = 0
        chunks = []
        while True:
            if c < 3:
                line = fp.readline().rstrip()
                if not line:
                    break
                c += 1
                chunks.append(line)
                continue

            common = set.intersection(*map(set, chunks)).pop()
            if common in lowercases:
                points += lowercases[common]
            if common in uppercases:
                points += uppercases[common]

            chunks = []
            c = 0

    print(points)


if __name__ == '__main__':
    main()
