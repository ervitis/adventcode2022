def main():
    hx, hy = 0, 0
    tx, ty = 0, 0
    num_pos = set()
    num_pos.add((tx, ty))
    directions = {'R': (1, 0), 'D': (0, -1), 'U': (0, 1), 'L': (-1, 0)}

    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().strip()
            if not line:
                break
            direction, steps = line.split(' ')
            steps = int(steps)
            while steps > 0:
                x, y = directions[direction]
                hx, hy = hx + x, hy + y
                if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
                    tx += 0 if tx == hx else (hx - tx) // abs(hx - tx)
                    ty += 0 if ty == hy else (hy - ty) // abs(hy - ty)
                num_pos.add((tx, ty))
                steps -= 1
    print(len(num_pos))


if __name__ == '__main__':
    main()
