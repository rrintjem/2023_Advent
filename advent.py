import sys
import Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day12,Day13,Day14

func_dict = {
    "1":Day1.day1,
    "2":Day2.day2,
    "3":Day3.day3,
    "4":Day4.day4,
    "5":Day5.day5,
    "6":Day6.day6,
    "7":Day7.day7,
    "8":Day8.day8,
    "9":Day9.day9,
    "12":Day12.day12,
    "13":Day13.day13,
    "14":Day14.day14
}


def readFile(day):
    argc = len(sys.argv)

    filename = 'inputTest.txt'
    if argc == 2:
        filename = 'input'+day+'.txt'
    return open(filename, "r")


def main():
    day = str(sys.argv[1])
    f = readFile(day)
    func_dict[day](f)

    
if __name__ == '__main__':
    main()