def main():
    X = 1
    t0 = 0
    pixels = [['.' for _ in range(40)] for _ in range(6)]

    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().strip()
            if not line:
                break
            line = line.split(' ')
            if line[0] == 'noop':
                t0 += 1
                t = t0 - 1
                x = t//40
                y = t%40
                pixels[x][y] = '#' if abs(X - t%40) <= 1 else ' '
            else:
                _, value = line
                t0 += 1
                t = t0 - 1
                x = t//40
                y = t%40
                pixels[x][y] = '#' if abs(X - t%40) <= 1 else ' '
                t0 += 1
                t = t0 - 1
                x = t//40
                y = t%40
                pixels[x][y] = '#' if abs(X - t%40) <= 1 else ' '
                X += int(value)
    for r in pixels:
        print(''.join(r))


if __name__ == '__main__':
    main()
