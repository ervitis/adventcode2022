import time

class Item(object):
    calory: int


class Elf(object):
    calory: int

    def __str__(self):
        return f'{self.calory}'


def main():
    elves: list[Elf] = []

    elf = Elf()
    count_calory = 0
    cl = 0
    start = time.time()
    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().rstrip()

            if line:
                count_calory += int(line)
                cl = 0
            if not line:
                if cl > 1:
                    break
                cl += 1
                elf.calory = count_calory
                elves.append(elf)
                count_calory = 0
                elf = Elf()
    elves.sort(key = lambda x: x.calory, reverse = True)
    print(f'time in {time.time() - start}')


if __name__ == '__main__':
    main()