package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Pair[T int64, T2 int64] struct {
	First  T2
	Second T2
}

type Step struct {
	Coords   Pair[int64, int64]
	Tokens   int
	PressedA int
	PressedB int
}

func getCoords(coordinates string, split string) (coords Pair[int64, int64], err error) {
	xPattern := "X[+=]\\d+"
	yPattern := "Y[+=]\\d+"
	re := regexp.MustCompile(xPattern)

	coords.First, err = strconv.ParseInt(strings.Split(re.FindString(coordinates), split)[1], 10, 64)
	if err != nil {
		return Pair[int64, int64]{}, err
	}
	re = regexp.MustCompile(yPattern)

	coords.Second, err = strconv.ParseInt(strings.Split(re.FindString(coordinates), split)[1], 10, 64)
	if err != nil {
		return Pair[int64, int64]{}, err
	}

	return coords, nil

}

func solve1() {
	content, err := os.ReadFile("inputs/13.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	contentStr := string(content)
	cases := strings.Split(contentStr, "\n\n")
	totalTokens := 0
	for _, testCase := range cases {
		lines := strings.Split(testCase, "\n")
		buttonACoords, _ := getCoords(lines[0], "+")
		buttonBCoords, _ := getCoords(lines[1], "+")
		prizeCoords, _ := getCoords(lines[2], "=")

		tokensA := 3
		tokensB := 1
		minTokens := math.MaxInt32
		maxPressThreshold := 100

		var queue []Step
		queue = append(queue, Step{
			Coords:   Pair[int64, int64]{0, 0},
			Tokens:   0,
			PressedA: 0,
			PressedB: 0,
		})

		visited := make(map[Pair[int64, int64]]bool)
		visited[Pair[int64, int64]{0, 0}] = true
		for len(queue) > 0 {
			current := queue[0]
			queue = queue[1:]
			if current.Coords.First == prizeCoords.First && current.Coords.Second == prizeCoords.Second {
				minTokens = int(math.Min(float64(minTokens), float64(current.Tokens)))
			} else if current.Coords.First < prizeCoords.First && current.Coords.Second < prizeCoords.Second && current.PressedA < maxPressThreshold && current.PressedB < maxPressThreshold {
				nextPosWithA := Pair[int64, int64]{
					First:  current.Coords.First + buttonACoords.First,
					Second: current.Coords.Second + buttonACoords.Second,
				}

				nextPosWithB := Pair[int64, int64]{
					First:  current.Coords.First + buttonBCoords.First,
					Second: current.Coords.Second + buttonBCoords.Second,
				}

				if _, exists := visited[nextPosWithA]; !exists {
					queue = append(queue, Step{
						Coords:   nextPosWithA,
						Tokens:   current.Tokens + tokensA,
						PressedA: current.PressedA + 1,
						PressedB: current.PressedB,
					})
					visited[nextPosWithA] = true
				}

				if _, exists := visited[nextPosWithB]; !exists {
					queue = append(queue, Step{
						Coords:   nextPosWithB,
						Tokens:   current.Tokens + tokensB,
						PressedA: current.PressedA,
						PressedB: current.PressedB + 3,
					})
					visited[nextPosWithB] = true
				}
			}
		}

		if minTokens != math.MaxInt32 {
			totalTokens += minTokens
		}
	}
	fmt.Println(totalTokens)
}

func solve2() {
	content, err := os.ReadFile("inputs/13.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	contentStr := string(content)
	cases := strings.Split(contentStr, "\n\n")
	totalTokens := int64(0)
	gap := int64(10000000000000)
	for _, testCase := range cases {
		lines := strings.Split(testCase, "\n")
		buttonACoords, _ := getCoords(lines[0], "+")
		buttonBCoords, _ := getCoords(lines[1], "+")
		prizeCoords, _ := getCoords(lines[2], "=")
		prizeCoords.First += gap
		prizeCoords.Second += gap

		determinant := buttonACoords.First*buttonBCoords.Second - buttonACoords.Second*buttonBCoords.First
		cramer_coeff := prizeCoords.First*buttonBCoords.Second - prizeCoords.Second*buttonBCoords.First
		var a int64
		var b int64
		var cost int64 = 0
		if determinant != 0 && cramer_coeff%determinant == 0 {
			a = cramer_coeff / determinant
			if (prizeCoords.First-buttonACoords.First*a)%buttonBCoords.First != 0 {
				continue
			}
			b = (prizeCoords.First - buttonACoords.First*a) / buttonBCoords.First
			cost = 3*a + b
		}

		totalTokens += cost
	}
	fmt.Println(totalTokens)
}

func main() {
	// solve1()
	solve2()
}
