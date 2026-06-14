package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solvePart1(fileName string) {
	fmt.Printf("Solving part 1 for file %s\n", fileName)
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	content := string(contentBytes)

	words := strings.Split(content, ",")
	sumIds := 0

	for _, word := range words {
		left := strings.Split(word, "-")[0]
		right := strings.Split(word, "-")[1]

		leftInt, _ := strconv.Atoi(left)
		rightInt, _ := strconv.Atoi(right)

		for start := leftInt; start <= rightInt; start++ {
			startStr := strconv.Itoa(start)
			if len(startStr)%2 == 0 {
				firstHalf := startStr[:len(startStr)/2]
				secondHalf := startStr[len(startStr)/2:]

				if firstHalf == secondHalf {
					sumIds += start
				}
			}
		}
	}

	fmt.Println("Sum: ", sumIds)

}

func solvePart2(fileName string) {
	fmt.Printf("Solving part 2 for file %s\n", fileName)
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	content := string(contentBytes)

	words := strings.Split(content, ",")
	sumIds := 0

	for _, word := range words {
		left := strings.Split(word, "-")[0]
		right := strings.Split(word, "-")[1]

		leftInt, _ := strconv.Atoi(left)
		rightInt, _ := strconv.Atoi(right)

		for start := leftInt; start <= rightInt; start++ {
			startStr := strconv.Itoa(start)
			for j := 0; j < len(startStr)/2; j++ {
				pattern := startStr[0 : j+1]
				stringWithPattern := ""
				for len(stringWithPattern) < len(startStr) {
					stringWithPattern += pattern
				}
				if stringWithPattern == startStr {
					sumIds += start
					break
				}
			}
		}
	}

	fmt.Println("Sum: ", sumIds)

}

func main() {
	fileName := os.Args[1]
	//solvePart1(fileName)
	solvePart2(fileName)
}
