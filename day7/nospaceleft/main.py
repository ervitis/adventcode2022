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
            else:
                for i in range(len(path)+1):
                    try:
                        dirs['/'.join(path[:i])] += int(line[0])
                    except:
                        pass

    max_size_files = 100000
    total_size = 0
    for k, v in dirs.items():
        if v <= max_size_files:
            total_size += v
    print(total_size)


if __name__ == '__main__':
    main()
