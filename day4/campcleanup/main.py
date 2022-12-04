import re


def main():
    with open('../data', 'r') as fp:
        pairs = 0
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            line = list(map(int, re.split('[-|,]', line)))
            if line[0] >= line[2] and line[1] <= line[3] or line[2] >= line[0] and line[3] <= line[1]:
                pairs += 1
    print(pairs)


if __name__ == '__main__':
    main()
