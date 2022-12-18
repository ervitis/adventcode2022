def main():
    forest = []
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            forest.append(line)

    trees = 0

    for row in range(len(forest)):
        for col in range(len(forest[0])):
            score = 1
            for x, y in dirs:
                rr = row + x
                cc = col + y
                distance = 1
                while True:
                    if not (0 <= rr < len(forest) and 0 <= cc < len(forest[0])):
                        distance -= 1
                        break
                    if forest[rr][cc] >= forest[row][col]:
                        break
                    distance += 1
                    rr += x
                    cc += y
                score *= distance
            trees = max(trees, score)
    print(trees)


if __name__ == '__main__':
    main()
