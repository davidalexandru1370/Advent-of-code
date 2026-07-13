package main

import (
	"fmt"
	"math/big"
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
	visited := make(map[[2]int]int)
	split := 1
	visited[[2]int{startX, startY}] = 0
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		nextPositionX, nextPositionY := current.x, current.y+1
		curr := visited[[2]int{current.x, current.y}]

		if isInside(nextPositionX, nextPositionY, len(lines), len(lines[0])) {
			if lines[nextPositionY][nextPositionX] == '^' {
				split += 2*curr + 1
				if isInside(nextPositionX+1, nextPositionY, len(lines), len(lines[0])) {
					visited[[2]int{nextPositionX + 1, nextPositionY}] = curr
					queue = append(queue, struct{ x, y int }{nextPositionX + 1, nextPositionY})
				}
				if isInside(nextPositionX-1, nextPositionY, len(lines), len(lines[0])) {
					visited[[2]int{nextPositionX - 1, nextPositionY}] = curr
					queue = append(queue, struct{ x, y int }{nextPositionX - 1, nextPositionY})
				}
			} else {
				queue = append(queue, struct{ x, y int }{nextPositionX, nextPositionY})
			}
		}
	}

	fmt.Println(split)
}

func solvePart2(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	content := string(contentBytes)
	lines := strings.Split(strings.TrimRight(content, "\n"), "\n")
	rows := len(lines)
	cols := len(lines[0])

	startCol := strings.IndexByte(lines[0], 'S')

	// beams[c] = number of beams currently falling down column c on the current row.
	// Beams that land on the same cell are merged by adding their counts, so the
	// whole board is processed once (O(rows*cols)) instead of enumerating every path.
	beams := make([]*big.Int, cols)
	for i := range beams {
		beams[i] = big.NewInt(0)
	}
	beams[startCol] = big.NewInt(1)

	split := big.NewInt(1)

	for r := 0; r+1 < rows; r++ {
		next := make([]*big.Int, cols)
		for i := range next {
			next[i] = big.NewInt(0)
		}
		for c := 0; c < cols; c++ {
			n := beams[c]
			if n.Sign() == 0 {
				continue
			}
			if lines[r+1][c] == '^' {
				split.Add(split, n)
				if c-1 >= 0 {
					next[c-1].Add(next[c-1], n)
				}
				if c+1 < cols {
					next[c+1].Add(next[c+1], n)
				}
			} else {
				next[c].Add(next[c], n)
			}
		}
		beams = next
	}

	fmt.Println(split.String())
}

func main() {
	// solvePart1("input.txt")
	solvePart2("input.txt")
}
