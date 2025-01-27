from tabulate import tabulate


def count_prob(a, b):
    return sum(x > y for x in a for y in b) / (len(a) * len(b))


class DiceProbability:
    def __init__(self, dice):
        self.dice = dice
        self.probabilities = []

    def calculate_probabilities(self):
        size = len(self.dice)
        self.probabilities = [[None] * size for _ in range(size)]

        for i, die_a in enumerate(self.dice):
            for j, die_b in enumerate(self.dice):
                if i == j:
                    self.probabilities[i][j] = f"- ({1 / len(die_a):.4f})"
                else:
                    if die_a == die_b:
                        self.probabilities[i][j] = f"- ({1 / len(die_a):.4f})"
                    else:
                        self.probabilities[i][j] = f"{count_prob(die_a, die_b):.4f}"

    def make_table(self):
        if not self.probabilities:
            raise ValueError("Probabilities not calculated. Call `calculate_probabilities` first.")
        headers = ["User dice v"] + [str(die) for die in self.dice]
        rows = []

        for i, die in enumerate(self.dice):
            row = [str(die)] + self.probabilities[i]
            rows.append(row)

        return tabulate(rows, headers=headers, tablefmt="grid")