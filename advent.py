import sys
import Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day12,Day13

func_dict = {
    "Day1.day1":Day1.day1,
    "Day2.day2":Day2.day2,
    "Day3.day3":Day3.day3,
    "Day4.day4":Day4.day4,
    "Day5.day5":Day5.day5,
    "Day6.day6":Day6.day6,
    "Day7.day7":Day7.day7,
    "Day8.day8":Day8.day8,
    "Day9.day9":Day9.day9,
    "Day12.day12":Day12.day12,
    "Day13.day13":Day13.day13
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
    func_name = "Day"+day +".day"+day
    func_dict[func_name](f)

    
if __name__ == '__main__':
    main()