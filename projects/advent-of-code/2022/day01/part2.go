package day01

import (
	u "jimcasey/aoc/utils"
	"sort"
	"strconv"
)

func Part2() {
	elves := make([]int, 1)

	for _, line := range u.Read("day01") {
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
