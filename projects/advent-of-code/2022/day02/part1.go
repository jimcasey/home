package day02

import (
	u "jimcasey/aoc/utils"
	s "strings"
)

func Part1() {
	theirsMap := map[string]int{"A": 1, "B": 2, "C": 3}
	mineMap := map[string]int{"X": 1, "Y": 2, "Z": 3}
	outcomeMap := map[int]int{0: 3, 1: 6, 2: 0}

	score := 0
	for _, line := range u.Read("day02") {
		guide := s.Split(line, " ")
		theirs := theirsMap[guide[0]]
		mine := mineMap[guide[1]]
		outcome := outcomeMap[(mine-theirs+3)%3]
		score += mine + outcome
	}

	u.Out(score)
}
