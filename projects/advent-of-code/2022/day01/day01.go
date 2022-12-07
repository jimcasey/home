package day01

import (
	"jimcasey/aoc/utils"
	"math"
	"sort"
	"strconv"
)

func Part1() {
	var maxCalories float64 = 0
	var currentCalories float64 = 0
	for _, line := range utils.Read("day01") {
		if line == "" {
			currentCalories = 0
		} else {
			calories, _ := strconv.Atoi(line)
			currentCalories += float64(calories)
		}
		maxCalories = math.Max(maxCalories, currentCalories)
	}

	utils.Out(maxCalories)
}

func Part2() {
	elves := make([]int, 1)

	for _, line := range utils.Read("day01") {
		if line == "" {
			elves = append(elves, 0)
		} else {
			calories, _ := strconv.Atoi(line)
			elves[len(elves)-1] += calories
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(elves)))

	var sum int
	for _, calories := range elves[0:3] {
		sum += calories
	}

	utils.Out(sum)
}
