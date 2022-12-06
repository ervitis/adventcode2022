def main():
    crates = []
    stacks = []
    in_moves = False

    with open('../data', 'r') as fp:
        for line in fp:
            if not line.rstrip():
                continue

            if not in_moves:
                if line[1] != '1':
                    crates.append(line)
                else:
                    in_moves = True
                    crates = [('   ' + i)[::4][1:] for i in crates[::-1]]

                    for i in range(int(line.split()[-1])):
                        stacks.append([crate[i] for crate in crates if crate[i] not in ('', ' ')])
                    stacks = [stack[:] for stack in stacks]
            else:
                moves, origin, destination = [int(n) for n in line.split()[1::2]]
                origin, destination = origin - 1, destination - 1

                stacks[destination] += stacks[origin][-1 * moves:]
                del stacks[origin][-1 * moves:]
    print(''.join([stack[-1] for stack in stacks]))


if __name__ == '__main__':
    main()
    