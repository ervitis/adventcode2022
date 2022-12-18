def main():
    X = 1
    strength = {'20': 20, '60': 60, '100': 100, '140': 140, '180': 180, '220': 220}
    cycle_start = 0
    sum_strength = []

    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().strip()
            if not line:
                break
            line = line.split(' ')
            if line[0] == 'noop':
                cycle_start += 1
                if str(cycle_start) in strength:
                    sum_strength.append(X * strength[str(cycle_start)])
            else:
                _, value = line
                cycle_start += 1
                if str(cycle_start) in strength:
                    sum_strength.append(X * strength[str(cycle_start)])
                cycle_start += 1
                if str(cycle_start) in strength:
                    sum_strength.append(X * strength[str(cycle_start)])
                X += int(value)
    print(sum(sum_strength))


if __name__ == '__main__':
    main()
