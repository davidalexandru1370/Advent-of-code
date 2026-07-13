package main

import (
	"fmt"
	"os"
	"strings"
)

func isInside(x, y, rows, cols int) bool {
	return x >= 0 && x < cols && y >= 0 && y < rows
}

func solvePart1(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	content := string(contentBytes)
	lines := strings.Split(strings.TrimRight(content, "\n"), "\n")
	startX, startY := 0, 0
	for x, char := range lines[0] {
		if char == 'S' {
			startX = x
			startY = 0
		}
	}

	queue := []struct{ x, y int }{{startX, startY}}
	visited := make(map[[2]int]bool)
	split := 0
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		nextPositionX, nextPositionY := current.x, current.y+1

		if isInside(nextPositionX, nextPositionY, len(lines), len(lines[0])) && !visited[[2]int{nextPositionX, nextPositionY}] {
			if lines[nextPositionY][nextPositionX] == '^' {
				split++
				visited[[2]int{nextPositionX, nextPositionY}] = true
				if isInside(nextPositionX+1, nextPositionY, len(lines), len(lines[0])) && !visited[[2]int{nextPositionX + 1, nextPositionY}] {
					queue = append(queue, struct{ x, y int }{nextPositionX + 1, nextPositionY})
				}
				if isInside(nextPositionX-1, nextPositionY, len(lines), len(lines[0])) && !visited[[2]int{nextPositionX - 1, nextPositionY}] {
					queue = append(queue, struct{ x, y int }{nextPositionX - 1, nextPositionY})
				}
			} else {
				queue = append(queue, struct{ x, y int }{nextPositionX, nextPositionY})
			}
		}
	}

	fmt.Println(len(visited))
}

func main() {
	solvePart1("input.txt")
}
