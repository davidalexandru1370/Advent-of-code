package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solvePart1(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	content := string(contentBytes)
	lines := strings.Split(strings.TrimRight(content, "\n"), "\n")
	cols := strings.Fields(lines[0])
	numbers := make([][]int, len(cols))

	totalSum := 0

	for index, line := range lines {
		if index == len(lines)-1 {
			operators := strings.Fields(line)
			for index, operator := range operators {
				if operator == "+" {
					sum := 0
					for _, number := range numbers[index] {
						sum += number
					}
					totalSum += sum
				} else {
					product := 1
					for _, number := range numbers[index] {
						product *= number
					}
					totalSum += product
				}
			}
		} else {
			numStrs := strings.Fields(line)
			for i, numStr := range numStrs {
				number, _ := strconv.Atoi(numStr)
				numbers[i] = append(numbers[i], number)
			}
		}
	}

	fmt.Println("Total Sum:", totalSum)
}

func makeLinesEqualLength(lines []string) []string {
	maxLength := 0
	for _, line := range lines {
		if len(line) > maxLength {
			maxLength = len(line)
		}
	}

	for i, line := range lines {
		if len(line) < maxLength {
			lines[i] = line + strings.Repeat(" ", maxLength-len(line))
		}
	}

	return lines
}

func solvePart2(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	content := string(contentBytes)
	lines := strings.Split(content, "\n")
	lines = makeLinesEqualLength(lines)
	operators := strings.Fields(lines[len(lines)-1])
	indexOperators := 0
	ans := 0
	var currentNumbers []int
	for column := 0; column < len(lines[0]); column++ {
		allEmpty := true
		currentNumber := 0
		for row := 0; row < len(lines)-1; row++ {
			if lines[row][column] != ' ' {
				allEmpty = false
				number := 0
				if value, err := strconv.Atoi(string(lines[row][column])); err == nil {
					number = value
				}
				currentNumber = currentNumber*10 + number
			}
		}
		if allEmpty {
			total := 0
			if operators[indexOperators] == "+" {
				for _, number := range currentNumbers {
					total += number
				}
			} else {
				total = 1
				for _, number := range currentNumbers {
					total *= number
				}
			}
			indexOperators++
			ans += total
			currentNumbers = []int{}
		} else {
			currentNumbers = append(currentNumbers, currentNumber)
		}
	}

	if len(currentNumbers) > 0 {
		total := 0
		if operators[indexOperators] == "+" {
			for _, number := range currentNumbers {
				total += number
			}
		} else {
			total = 1
			for _, number := range currentNumbers {
				total *= number
			}
		}
		ans += total
	}

	fmt.Println(ans)

}

func main() {
	fileName := "input.txt"
	// solvePart1(fileName)
	solvePart2(fileName)
}
