import re


def main():
    with open('../data', 'r') as fp:
        pairs = 0
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            line = list(map(int, re.split('[-|,]', line)))
            if not(line[1] < line[2] or line[3] < line[0]):
                pairs += 1
    print(pairs)


if __name__ == '__main__':
    main()
