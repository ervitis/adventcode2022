from enum import Enum, IntEnum


class ElfHand(str, Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSOR = 'C'


class MyHand(str, Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSOR = 'Z'


class HandPoints(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class Points(IntEnum):
    WIN = 6
    DRAW = 3
    LOST = 0


def main():
    hands = {
        f'{ElfHand.PAPER} {MyHand.SCISSOR}': Points.WIN + HandPoints.SCISSOR,
        f'{ElfHand.PAPER} {MyHand.PAPER}': Points.DRAW + HandPoints.PAPER,
        f'{ElfHand.PAPER} {MyHand.ROCK}': Points.LOST + HandPoints.ROCK,
        f'{ElfHand.ROCK} {MyHand.SCISSOR}': Points.LOST + HandPoints.SCISSOR,
        f'{ElfHand.ROCK} {MyHand.PAPER}': Points.WIN + HandPoints.PAPER,
        f'{ElfHand.ROCK} {MyHand.ROCK}': Points.DRAW + HandPoints.ROCK,
        f'{ElfHand.SCISSOR} {MyHand.SCISSOR}': Points.DRAW + HandPoints.SCISSOR,
        f'{ElfHand.SCISSOR} {MyHand.PAPER}': Points.LOST + HandPoints.PAPER,
        f'{ElfHand.SCISSOR} {MyHand.ROCK}': Points.WIN + HandPoints.ROCK,
    }

    new_result = {
        MyHand.ROCK: {
            ElfHand.PAPER: MyHand.ROCK,
            ElfHand.ROCK: MyHand.SCISSOR,
            ElfHand.SCISSOR: MyHand.PAPER,
        },
        MyHand.PAPER: {
            ElfHand.PAPER: MyHand.PAPER,
            ElfHand.ROCK: MyHand.ROCK,
            ElfHand.SCISSOR: MyHand.SCISSOR,
        },
        MyHand.SCISSOR: {
            ElfHand.PAPER: MyHand.SCISSOR,
            ElfHand.ROCK: MyHand.PAPER,
            ElfHand.SCISSOR: MyHand.ROCK,
        }
    }

    points = 0
    r = 1
    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            elfh, myh = line.split(' ')
            elf = ElfHand(elfh)
            myhand = new_result[myh][elf]

            points += hands[f'{elf} {myhand}']
    print(points)


if __name__ == '__main__':
    main()
