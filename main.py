import sys
from dice import Dice


def formatDice(args):
    diceList = []
    if len(args) < 3:
        raise ValueError("Provide at least 3 dices")
    for arg in args:
        if ',' not in arg:
            raise ValueError("Each die must be comma-separated numbers.")
        try:
            faces = [int(face.strip()) for face in arg.split(",")]
        except ValueError:
            raise ValueError("The faces need to be integers")
        diceList.append(faces)
    face_count = len(diceList[0])
    if not all(len(die) == face_count for die in diceList):
        raise ValueError(f"All dice needs to have same number of faces")
    return diceList


if __name__ == "__main__":
    try:
        diceInput = sys.argv[1:]
        DiceArray = formatDice(diceInput)
        print("formatDice: ")
        for i, die in enumerate(DiceArray):
            print(f"Die {i + 1}: {die}")
        dice = Dice(DiceArray)
        dice.startgame(dice)
    except ValueError as e:
        print(e)
        sys.exit(1)
