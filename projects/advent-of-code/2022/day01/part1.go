package day01

import (
	u "jimcasey/aoc/utils"
	"math"
	"strconv"
)

func Part1() {
	var maxCalories float64 = 0
	var currentCalories float64 = 0
	for _, line := range u.Read("day01") {
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
