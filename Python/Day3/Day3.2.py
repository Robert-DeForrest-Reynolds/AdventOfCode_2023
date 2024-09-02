from typing import Tuple, List

ExampleCase = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

global Symbols
Symbols = []


def Find_Whole_Number(NumberPacket, Schematic):
    global Symbols
    SchematicLineSplit = Schematic.split("\n")
    SchematicLength = len(SchematicLineSplit[0])
    Number = NumberPacket[0]
    WholeNumber = Number
    X = NumberPacket[1][0]
    Y = NumberPacket[1][1]

    BackwardXTraverse = X
    while BackwardXTraverse != 0:
        BackwardXTraverse -= 1
        if BackwardXTraverse >= 0:
            if SchematicLineSplit[Y][BackwardXTraverse].isnumeric():
                WholeNumber = SchematicLineSplit[Y][BackwardXTraverse] + WholeNumber
            elif SchematicLineSplit[Y][BackwardXTraverse] in Symbols + ["."]:
                break
        else:
            break

    ForwardXTraverse = X
    while ForwardXTraverse != SchematicLength:
        ForwardXTraverse += 1
        if ForwardXTraverse < SchematicLength:
            if SchematicLineSplit[Y][ForwardXTraverse].isnumeric():
                WholeNumber = WholeNumber + SchematicLineSplit[Y][ForwardXTraverse]
            elif SchematicLineSplit[Y][ForwardXTraverse] in Symbols + ["."]:
                break
        else:
            break
    return WholeNumber


def Check_For_Gear(X:int, Y:int, Schematic:str) -> Tuple[int, int]:
    global Symbols
    SchematicLineSplit = Schematic.split("\n")
    SchematicHeight = len(SchematicLineSplit)
    SchematicLength = len(SchematicLineSplit[0])

    FoundNumbers = []

    # Top
    if Y - 1 >= 0:
        if SchematicLineSplit[Y-1][X] != ".":
            FoundNumbers.append((SchematicLineSplit[Y-1][X], (X, Y-1)))
    
    # Top Left
    if Y - 1 >= 0 and X - 1 >= 0:
        if SchematicLineSplit[Y-1][X-1] != ".":
            FoundNumbers.append((SchematicLineSplit[Y-1][X-1], (X-1, Y-1)))

    # Top Right
    if Y - 1 >= 0 and X + 1 <= SchematicLength:
        if SchematicLineSplit[Y-1][X+1] != ".":
            FoundNumbers.append((SchematicLineSplit[Y-1][X+1], (X+1, Y-1)))
    
    # Bottom
    if Y + 1 < SchematicHeight:
        if SchematicLineSplit[Y+1][X] != ".":
            FoundNumbers.append((SchematicLineSplit[Y+1][X], (X, Y+1)))

    # Bottom Left
    if Y + 1 < SchematicHeight and X - 1 >= 0:
        if SchematicLineSplit[Y+1][X-1] != ".":
            FoundNumbers.append((SchematicLineSplit[Y+1][X-1], (X-1, Y+1)))

    # Bottom Right
    if Y + 1 <= SchematicHeight - 1 and X + 1 <= SchematicLength:
        if SchematicLineSplit[Y+1][X+1] != ".":
            FoundNumbers.append((SchematicLineSplit[Y+1][X+1], (X+1, Y+1)))

    # Left
    if X - 1 >= 0:
        if SchematicLineSplit[Y][X-1] != ".":
            FoundNumbers.append((SchematicLineSplit[Y][X-1], (X-1, Y)))

    # Right
    if X + 1 <= SchematicLength:
        if SchematicLineSplit[Y][X+1] != ".":
            FoundNumbers.append((SchematicLineSplit[Y][X+1], (X+1 , Y)))


    WholeFoundNumbers = [int(Find_Whole_Number(Packet, Schematic)) for Packet in FoundNumbers]
    NonDuplicate = []
    for Number in WholeFoundNumbers:
        if Number not in NonDuplicate:
            NonDuplicate.append(Number)
    
    if SchematicLineSplit[Y][X] == "*":
        if len(NonDuplicate) == 2:
            return NonDuplicate[0] * NonDuplicate[1]


def Traverse_Schematic(Schematic:str) -> int:
    global Symbols
    GearValues = []
    X = 0
    Y = 0
    for Character in Schematic:
        if Character.isnumeric() == False and Character not in  [".", "\n"]:
            if Character not in Symbols:
                Symbols.append(Character)
        if Character in Symbols:
            PotentialGear = Check_For_Gear(X, Y, Schematic)
            if PotentialGear != None:
                GearValues.append(PotentialGear)
        if Character == "\n":
            X = 0
            Y += 1
        else:
            X += 1
    return sum(GearValues)


with open("Day3PuzzleInput.txt") as SchematicFile:
    Answer:int = Traverse_Schematic("".join(SchematicFile.readlines()))
    print(Answer)

# Answer:int = Traverse_Schematic(ExampleCase)
# print(Answer)