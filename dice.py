import sys

from key import HmacSha3Generator
from randnum import RandNum
from probability import DiceProbability


class Dice:
    def __init__(self, die: list) -> None:
        self.compDice = []
        self.compScore = int
        self.userScore = int
        self.input = input
        self.die = die
        self.userDice = []
        self.result = None
        table = DiceProbability(die)
        table.calculate_probabilities()
        self.prob = table.make_table()

    @staticmethod
    def startgame(self) -> None:
        print("Let's determine who makes the first move.")
        hmac1 = HmacSha3Generator()
        num = RandNum.secure_int(0, 1)
        print("I selected a random value in the range 0..1")
        print(f"(HMAC={hmac1.generatehmac(num)})")
        while True:
            try:
                self.input = input("Try to guess my selection:\n0 - 0\n1 - 1\nX - exit\n? - help\nYour selection: ")
                if self.input.isdigit() and 0 <= int(self.input) <= 1:
                    print(f"My selection: {num}\n(KEY={hmac1.getKey()})")
                    if int(self.input) == num:
                        self.userfirst()
                    else:
                        self.compfirst()
                    break
                elif self.input == "X":
                    return
                elif self.input == "?":
                    print(self.prob)
                    continue
                else:
                    print("Error: Invalid input. Please try again.")
            except ValueError:
                print("You entered an invalid option")

    def compfirst(self) -> None:
        self.compDice = self.die[0]
        self.input = input(
            f"I make the first move and choose the {self.die[0]} dice\nChoose your dice:\n0 -{self.die[1]}\n1 - {self.die[2]}\nX - exit\n? - help\nYour selection: ")
        if self.input.isdigit():
            self.userDice = self.die[int(self.input) + 1]
            print(f"You choose the {self.userDice} dice\nIt's time for my throw.")
            result = self.throwDice()
            self.compScore = self.compDice[result]
            print(f"My throw is {self.compScore}\n Its time for your throw.")
            result = self.throwDice()
            self.userScore = self.userDice[result]
            self.computeDice(self.compScore, self.userScore)
        elif self.input == "X":
            return

    def userfirst(self) -> None:
        self.input = input(
            f"Choose your dice:\n0 - {self.die[0]}\n1 - {self.die[1]}\n2 - {self.die[2]}"
            f"\nX - exit\n? - help\nYour selection: ")
        if self.input.isdigit():
            self.userDice = self.die[int(self.input)]
            del self.die[int(self.input)]
            self.compDice = self.die[0]
            print(f"You choose the {self.userDice} dice\nI chose {self.die[0]}It's time for my throw.")
            result = self.throwDice()
            self.compScore = self.compDice[result]
            print(f"My throw is {self.compScore}\nIts time for your throw.")
            result = self.throwDice()
            self.userScore = self.userDice[result]
            self.computeDice(self.compScore, self.userScore)
        elif self.input == "X":
            return

    def throwDice(self) -> int:
        hmac = HmacSha3Generator()
        num = RandNum.secure_int(0, 5)
        print("I selected a random value in the range 0..5")
        print(f"(HMAC={hmac.generatehmac(num)})")
        print("Add your number modulo 6.\n0 - 0\n1 - 1\n2 - 2\n3 - 3\n4 - 4\n5 - 5\nX - exit\n? - help")
        self.input = input("Your selection: ")
        if self.input == "X":
            sys.exit()
        print(f"My number is {num}\n(KEY={hmac.getKey()})")
        result = self.calculateDice(num, int(self.input))
        return result

    @staticmethod
    def calculateDice(first: int, second: int) -> int:
        print(f"The result is {first} + {second} = {(first + second) % 6} (mod 6)")
        return (first + second) % 6

    def computeDice(self, first: int, second: int) -> None:
        if self.userScore < self.compScore:
            print(f"You lose ({first}>{second})")
        else:
            print(f"You win! ({second}>{first})")
