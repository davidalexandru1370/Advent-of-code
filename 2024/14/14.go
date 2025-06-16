package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var inputFile string = "inputs/14.txt"

type Position struct {
	X int
	Y int
}

type Quadrant int

const (
	TOPLEFT Quadrant = iota
	TOPRIGHT
	BOTTOMLEFT
	BOTTOMRIGHT
	NONE
)

type Robot struct {
	Position
	StepX int
	StepY int
}

func Maybe[T any](v T, err error) T {
	if err != nil {
		fmt.Println("Error: ", err)
	}

	return v
}

func belongsToAQuadrant(pos Position, rows, cols int) bool {
	midRow := rows / 2
	midCols := cols / 2

	if pos.X == midCols || pos.Y == midRow {
		return false
	}

	return true
}

func getQuadrant(pos Position, rows, cols int) Quadrant {
	if !belongsToAQuadrant(pos, rows, cols) {
		return NONE
	}

	midRow := rows / 2
	midCols := cols / 2

	if pos.X < midCols {
		if pos.Y < midRow {
			return TOPLEFT
		}
		return BOTTOMLEFT
	} else {
		if pos.Y < midRow {
			return TOPRIGHT
		}
		return BOTTOMRIGHT
	}
}

func solve_14_part1() {
	input, err := os.ReadFile(inputFile)
	if err != nil {
		fmt.Println("Error reading from file", err)
		return
	}
	contentStr := string(input)

	rows := 103
	cols := 101
	steps := 100
	lines := strings.Split(contentStr, "\n")
	quadrants := make([]int, 4)
	for _, line := range lines {
		numberPattern := "[-+]?\\d+"
		re := regexp.MustCompile(numberPattern)
		matches := re.FindAllString(line, -1)
		for index := 0; index < len(matches); index += 4 {
			pos := Position{
				X: Maybe(strconv.Atoi(matches[index])),
				Y: Maybe(strconv.Atoi(matches[index+1])),
			}
			robot := Robot{
				Position: pos,
				StepX:    Maybe(strconv.Atoi(matches[index+2])),
				StepY:    Maybe(strconv.Atoi(matches[index+3])),
			}
			nextPos := Position{
				X: mod(mod(robot.StepX*steps, cols)+robot.X, cols),
				Y: mod(mod(robot.StepY*steps, rows)+robot.Y, rows),
			}
			if quadrant := getQuadrant(nextPos, rows, cols); quadrant != NONE {
				quadrants[quadrant] += 1
			}
		}
	}

	product := 1
	for _, q := range quadrants {
		if q > 0 {
			product *= q
		}
	}

	fmt.Println(quadrants)
	fmt.Println(product)
}

func solveDay14Part2() {
	input, err := os.ReadFile(inputFile)
	if err != nil {
		fmt.Println("Error reading from file", err)
		return
	}
	contentStr := string(input)

	rows := 103
	cols := 101
	steps := 100
	lines := strings.Split(contentStr, "\n")
	quadrants := make([]int, 4)
	var robots []Robot
	for _, line := range lines {
		numberPattern := "[-+]?\\d+"
		re := regexp.MustCompile(numberPattern)
		matches := re.FindAllString(line, -1)
		for index := 0; index < len(matches); index += 4 {
			pos := Position{
				X: Maybe(strconv.Atoi(matches[index])),
				Y: Maybe(strconv.Atoi(matches[index+1])),
			}
			robot := Robot{
				Position: pos,
				StepX:    Maybe(strconv.Atoi(matches[index+2])),
				StepY:    Maybe(strconv.Atoi(matches[index+3])),
			}
			robots = append(robots, robot)
		}
	}
	for index := 1; index <= steps; index++ {
		fmt.Sprintf("Iteration: %d\n", index)

		for _, robot := range robots {
			newPos := Position{
				X: robot.StepX + robot.Position.X,
				Y: robot.StepY + robot.Position.Y,
			}

			robot.Position = newPos
		}
	}
}

func day14() {
	// solve_14_part1()
	solveDay14Part2()
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func main() {
	day14()
}
