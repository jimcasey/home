package day01

import (
	u "jimcasey/aoc/utils"
	"math"
	"sort"
	"strconv"
)

func init() {
	u.Register(1, part1, part2)
}

func part1() {
	var maxCalories float64 = 0
	var currentCalories float64 = 0
	for _, line := range u.Read() {
		if line == "" {
			currentCalories = 0
		} else {
			calories, _ := strconv.Atoi(line)
			currentCalories += float64(calories)
		}
		maxCalories = math.Max(maxCalories, currentCalories)
	}

	u.Out(maxCalories)
}

func part2() {
	elves := make([]int, 1)

	for _, line := range u.Read() {
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

	u.Out(sum)
}
