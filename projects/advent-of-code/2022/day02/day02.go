package day02

import (
	"jimcasey/aoc/utils"
	"strings"
)

func init() {
	utils.Register(2, part1, part2)
}

func part1() {
	theirsMap := map[string]int{"A": 1, "B": 2, "C": 3}
	mineMap := map[string]int{"X": 1, "Y": 2, "Z": 3}
	outcomeMap := map[int]int{0: 3, 1: 6, 2: 0}

	score := 0
	for _, line := range utils.Read() {
		guide := strings.Split(line, " ")
		theirs := theirsMap[guide[0]]
		mine := mineMap[guide[1]]
		outcome := outcomeMap[(mine-theirs+3)%3]
		score += mine + outcome
	}

	utils.Out(score)
}

func part2() {
	theirsMap := map[string]int{"A": 1, "B": 2, "C": 3}
	outcomeMap := map[string]int{"X": 0, "Y": 3, "Z": 6}
	offsetMap := map[string]int{"X": -1, "Y": 0, "Z": 1}

	score := 0
	for _, line := range utils.Read() {
		guide := strings.Split(line, " ")
		theirs := theirsMap[guide[0]]
		mine := ((theirs + 2 + offsetMap[guide[1]]) % 3) + 1
		score += mine + outcomeMap[guide[1]]
	}

	utils.Out(score)
}
