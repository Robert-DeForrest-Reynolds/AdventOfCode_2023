from typing import List

ExampleCase = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")


def Determine_Scratch_Pile_Worth(ScratchCardPile:List[str]):
    TotalPoints = 0
    for ScratchCard in ScratchCardPile:
        Points = 0
        ScratchCardSplit = ScratchCard.split(": ")
        CardNumber = ScratchCardSplit[0]
        ScratchCardSplit = ScratchCardSplit[1].split(" | ")
        WinningNumbers = ScratchCardSplit[0].replace("  ", " ").split(" ")
        PlayerNumbers = ScratchCardSplit[1].replace("  ", " ").replace("\n", "").split(" ")
        WinningNumbers = [Number for Number in WinningNumbers if Number != ""]
        PlayerNumbers = [Number for Number in PlayerNumbers if Number != ""]
        FoundNumbers = []
        print(CardNumber)
        print(WinningNumbers)
        print(PlayerNumbers)
        for Number in PlayerNumbers:
            if Number in WinningNumbers:
                if Number not in FoundNumbers:
                    FoundNumbers.append(Number)
                    if Points == 0:
                        Points = 1
                    else:
                        Points *= 2
        print(Points)
        print(FoundNumbers)
        print("\n\n")
        TotalPoints += Points
    return TotalPoints


with open("Day4PuzzleInput.txt") as ScratchCardsFile:
    Answer:int = Determine_Scratch_Pile_Worth(ScratchCardsFile.readlines())
    print(Answer)

# Answer:int = Determine_Scratch_Pile_Worth(ExampleCase)
# print(Answer)