package day1

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func Solve1() {
	var input = "2023/day1/1.txt"
	file, err := os.Open(input)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var array1 []int
	var array2 []int
	var resultSum = 0
	for scanner.Scan() {
		line := scanner.Text()        // Read the current line
		words := strings.Fields(line) // Split the line by spaces
		num1, _ := strconv.Atoi(words[0])
		num2, _ := strconv.Atoi(words[1])

		array1 = append(array1, num1)
		array2 = append(array2, num2)
	}

	sort.Ints(array1)
	sort.Ints(array2)
	for index := range array1 {
		resultSum += abs(array1[index] - array2[index])
	}

	fmt.Println(resultSum)
}

func Solve2() {
	var input = "2023/day1/1.txt"
	file, err := os.Open(input)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var array1 []int
	var freq = make(map[int]int)
	var resultSum = 0
	for scanner.Scan() {
		line := scanner.Text()        // Read the current line
		words := strings.Fields(line) // Split the line by spaces
		num1, _ := strconv.Atoi(words[0])
		num2, _ := strconv.Atoi(words[1])
		if _, exists := freq[num2]; !exists {
			freq[num2] = 1
		} else {
			freq[num2] = freq[num2] + 1
		}

		array1 = append(array1, num1)
	}

	for index := range array1 {
		frequency, exists := freq[array1[index]]
		if !exists {
			frequency = 0
		}
		resultSum += abs(array1[index] * frequency)
	}

	fmt.Println(resultSum)
}
