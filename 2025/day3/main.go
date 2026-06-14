package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solvePart1(fileName string) {
	content, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(content), "\n")
	power := 0

	for _, line := range lines {
		line := string(line)
		left := -1
		right := -1
		total := -1
		for i := 0; i < len(line); i++ {
			num, err := strconv.Atoi(string(line[i]))
			if err != nil {
				panic(err)
			}
			if left == -1 {
				left = num
				continue
			} else if right == -1 {
				right = num
				total = left*10 + right
			}
			if num > left {
				new := left*10 + num
				if new > total {
					total = new
				}
				left = num
				right = -1
			} else if num > right {
				new := left*10 + num
				if new > total {
					total = new
				}
				right = num
			}
		}
		fmt.Println(total)
		power += total
	}

	fmt.Println(power)
}

func solvePart2(fileName string) {
	content, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(content), "\n")
	power := 0

	for _, line := range lines {
		bank := string(line)
		k := 12
		num := 0
		for i := 0; i < k && len(bank) > 0; i++ {
			remove := 11 - i
			substr := bank[:len(bank)-remove]
			digit := 0
			idx := 0
			for letterIdx, letter := range substr {
				num, err := strconv.Atoi(string(letter))
				if err != nil {
					panic(err)
				}
				if num > digit {
					digit = num
					idx = letterIdx
				}

			}
			bank = bank[idx+1:]
			num = num*10 + digit
		}

		fmt.Println(num)
		power += num
	}

	fmt.Println(power)
}

func main() {
	fileName := os.Args[1]

	//solvePart1(fileName)
	solvePart2(fileName)
}
