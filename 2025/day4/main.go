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
	directions := []int{-1, 0, 1}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			neighbours := 0
			if matrix[i][j] != "@" {
				continue
			}
			for di := 0; di < 3; di++ {
				for dj := 0; dj < 3; dj++ {
					if directions[di] == 0 && directions[dj] == 0 {
						continue
					}
					neighbour_i := i + directions[di]
					neighbour_j := j + directions[dj]
					if neighbour_i >= 0 && neighbour_i < rows && neighbour_j >= 0 && neighbour_j < cols && matrix[neighbour_i][neighbour_j] == "@" {
						neighbours++
					}
				}

			}
			if neighbours <= 3 {
				rollsOfPaper++
			}
		}
	}

	fmt.Println(rollsOfPaper)
}

func solvePart2(fileName string) {
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
	directions := []int{-1, 0, 1}
	canPursue := true

	for canPursue {
		found := 0
		for i := 0; i < rows; i++ {
			for j := 0; j < cols; j++ {
				neighbours := 0
				if matrix[i][j] != "@" {
					continue
				}
				for di := 0; di < 3; di++ {
					for dj := 0; dj < 3; dj++ {
						if directions[di] == 0 && directions[dj] == 0 {
							continue
						}
						neighbour_i := i + directions[di]
						neighbour_j := j + directions[dj]
						if neighbour_i >= 0 && neighbour_i < rows && neighbour_j >= 0 && neighbour_j < cols && matrix[neighbour_i][neighbour_j] == "@" {
							neighbours++
						}
					}
				}
				if neighbours <= 3 {
					matrix[i][j] = "."
					rollsOfPaper++
					found++
				}
			}

		}
		if found == 0 {
			canPursue = false
		}
	}

	fmt.Println(rollsOfPaper)
}

func main() {
	fileName := "input.txt"
	// solvePart1(fileName)
	solvePart2(fileName)
}
