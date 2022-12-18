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
            is_visible = False
            for x, y in dirs:
                rr = row
                cc = col
                can_see = True
                while True:
                    rr += x
                    cc += y
                    if not (0 <= rr < len(forest) and 0 <= cc < len(forest[0])):
                        break
                    if forest[rr][cc] >= forest[row][col]:
                        can_see = False
                if can_see:
                    is_visible = True
            if is_visible:
                trees += 1
    print(trees)


if __name__ == '__main__':
    main()
