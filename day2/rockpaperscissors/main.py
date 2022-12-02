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

    points = 0
    with open('../data', 'r') as fp:
        while True:
            line = fp.readline().rstrip()
            if not line:
                break
            points += hands[line]
    print(points)


if __name__ == '__main__':
    main()
