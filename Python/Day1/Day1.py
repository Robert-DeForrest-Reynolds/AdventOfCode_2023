from typing import List

ExampleCase = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def Parse_Calibration_Numbers(CalibrationDocumentContents:List[str]) -> int:
    Sum = 0
    for Line in CalibrationDocumentContents:
        CalibrationValue = []
        for Character in Line:
            if Character.isnumeric():
                CalibrationValue.append(int(Character))
        FirstCalibrationNumber = CalibrationValue[0]
        SecondCalibationNumber = CalibrationValue[len(CalibrationValue)-1]
        Sum += int(f"{FirstCalibrationNumber}{SecondCalibationNumber}")
    return Sum

with open("Day1PuzzleInput.txt") as CalibrationDocument:
    Answer:int = Parse_Calibration_Numbers(CalibrationDocument.readlines())
    print(Answer)