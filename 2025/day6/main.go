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

func main() {
	fileName := "input.txt"
	solvePart1(fileName)
}
