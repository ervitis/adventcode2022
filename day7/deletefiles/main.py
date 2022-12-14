import math
from collections import defaultdict


def main():
    dirs = defaultdict(int)
    path = []
    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            line = line.split(' ')
            if line[1] == 'cd':
                if line[2] == '..':
                    path.pop()
                else:
                    path.append(line[2])
            elif line[1] == 'ls':
                continue
            elif line[0] == 'dir':
                continue
            else:
                for i in range(1, len(path)+1):
                    try:
                        dirs['/'.join(path[:i])] += int(line[0])
                    except:
                        pass

    best = math.inf
    to_clean = dirs['/'] - (70000000 - 30000000)
    for k, v in dirs.items():
        if v >= to_clean:
            best = min(best, v)
    print(best)


if __name__ == '__main__':
    main()
    