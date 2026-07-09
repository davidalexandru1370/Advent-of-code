package main

import (
	"fmt"
	"os"
	"strings"
)

func solvePart1(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	content := string(contentBytes)
	lines := strings.Split(content, "\n")
	rows := len(lines)
	cols := len(lines[0])
	matrix := make([][]string, rows)

	for i := 0; i < rows; i++ {
		matrix[i] = make([]string, cols)
		for j := 0; j < cols; j++ {
			matrix[i][j] = string(lines[i][j])
		}
	}

	rollsOfPaper := 0
	di := []int{-1, 0, 1, 0, -1, 1, 1, -1}
	dj := []int{0, 1, 0, -1, -1, 1, -1, 1}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			neighbours := 0
			if matrix[i][j] != "@" {
				continue
			}
			for k := 0; k < 8; k++ {
				neighbour_i := i + di[k]
				neighbour_j := j + dj[k]
				if neighbour_i >= 0 && neighbour_i < rows && neighbour_j >= 0 && neighbour_j < cols && matrix[neighbour_i][neighbour_j] == "@" {
					neighbours++
				}
			}

			if neighbours <= 3 {
				rollsOfPaper++
			}
		}
	}

	fmt.Println(rollsOfPaper)
}

func main() {
	fileName := "input.txt"
	solvePart1(fileName)
}
