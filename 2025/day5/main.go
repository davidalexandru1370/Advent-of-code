package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func overlap(intervals [][]int, number int) bool {
	for _, interval := range intervals {
		if number >= interval[0] && number <= interval[1] {
			return true
		}
	}
	return false
}

func parseInterval(line string) []int {
	parts := strings.Split(line, "-")
	start, _ := strconv.Atoi(parts[0])
	end, _ := strconv.Atoi(parts[1])
	return []int{start, end}
}

func solvePart1(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}
	content := string(contentBytes)
	lines := strings.Split(content, "\n")
	index := 0
	intervals := make([][]int, 0)
	for index < len(lines) && lines[index] != "" {
		intervals = append(intervals, parseInterval(lines[index]))
		index++
	}
	overlapCount := 0
	for index < len(lines) {
		number, _ := strconv.Atoi(lines[index])

		if overlap(intervals, number) {
			overlapCount++
		}
		index++

	}
	fmt.Println(overlapCount)
}

func mergeIntervals(intervals [][]int) [][]int {
	if len(intervals) == 0 {
		return intervals
	}
	// Sort intervals by start time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	merged := [][]int{intervals[0]}

	for i := 1; i < len(intervals); i++ {
		lastMerged := merged[len(merged)-1]
		current := intervals[i]

		if current[0] <= lastMerged[1] {
			// Overlapping intervals, merge them
			lastMerged[1] = max(lastMerged[1], current[1])
		} else {
			// Non-overlapping interval, add it to the merged list
			merged = append(merged, current)
		}
	}

	return merged
}

func solvePart2(fileName string) {
	contentBytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}
	content := string(contentBytes)
	lines := strings.Split(content, "\n")
	index := 0
	intervals := make([][]int, 0)
	for index < len(lines) && lines[index] != "" {
		intervals = append(intervals, parseInterval(lines[index]))
		index++
	}

	mergedIntervals := mergeIntervals(intervals)
	totalLength := 0
	for _, interval := range mergedIntervals {
		length := interval[1] - interval[0] + 1
		totalLength += length
	}
	fmt.Println(totalLength)
}

func main() {
	// solvePart1("input.txt")
	solvePart2("input.txt")
}
