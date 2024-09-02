ExampleCase = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

Mapping = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

global CalibrationValue
CalibrationValue = 0
global CalibrationValueSets
CalibrationValueSets = []
global CalibrationValuesFound
CalibrationValuesFound = []


def Parse_Line(Line) -> int:
    global CalibrationValuesFound
    CursorStart = 0
    CursorEnd = 3
    Cursor = Line[CursorStart:CursorEnd]
    if len(Cursor) > 0:
        if Cursor[0].isnumeric():
            CalibrationValuesFound.append(int(Cursor[0]))
            Parse_Line(Line[1:])
            return
        
        if Cursor in Mapping.keys():
            CalibrationValuesFound.append(Mapping[Cursor])
            Parse_Line(Line[1:])
            return
        else:
            Cursor = Line[CursorStart:CursorEnd+1]

        if Cursor in Mapping.keys():
            CalibrationValuesFound.append(Mapping[Cursor])
            Parse_Line(Line[1:])
            return
        else:
            Cursor = Line[CursorStart:CursorEnd+2]

        if Cursor in Mapping.keys():
            CalibrationValuesFound.append(Mapping[Cursor])
            Parse_Line(Line[1:])
            return
        
        Parse_Line(Line[1:])
        return


def Parse_Calibration_Document() -> None:
    global CalibrationValue
    global CalibrationValueSets
    global CalibrationValuesFound
    with open("Day1.2PuzzleInput.txt") as CalibrationDocument:
        for Line in CalibrationDocument.readlines():
            CalibrationValuesFound = []
            Parse_Line(Line)
            CalibrationValueSets.append(CalibrationValuesFound)

    for CalibrationValueSet in CalibrationValueSets:
        CalibrationValue += int(f"{CalibrationValueSet[0]}{CalibrationValueSet[len(CalibrationValueSet)-1]}")

    print(CalibrationValue)


Parse_Calibration_Document()
