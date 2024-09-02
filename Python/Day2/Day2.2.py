from typing import List

ExampleCase = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def Parse_Gameplay(Gameplay, Mapping):
    for Round in Gameplay.split("; "):
        for Showing in Round.split(", "):
            ShowingSplit = Showing.split(" ")
            AmountShown = int(ShowingSplit[0])
            ColorShown = ShowingSplit[1].strip()
            if Mapping[ColorShown] == 0:
                Mapping[ColorShown] = AmountShown
            elif AmountShown > Mapping[ColorShown]:
                Mapping[ColorShown] = AmountShown


def Get_Power(Powers):
    return eval("*".join([str(Power) for Power in Powers.values()])) # What a fuckin beauty lmfao


def Parse_Games(Records:List[str]) -> List[int]:
    Powers = []
    for Game in Records:
        Mapping = {
            "red":0,
            "green":0,
            "blue":0,
        }
        GameDataSplit = Game.split(": ")
        GameNumber = int(GameDataSplit[0].split(" ")[1])
        Gameplay  = GameDataSplit[1]
        Parse_Gameplay(Gameplay, Mapping)
        Powers.append(Get_Power(Mapping))
    
    return sum(Powers)

with open("Day2.2PuzzleInput.txt") as GamesRecordsDocuments:
    Answer:int = Parse_Games(GamesRecordsDocuments.readlines())
    print(Answer)