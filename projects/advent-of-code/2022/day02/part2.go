package day02

import (
	u "jimcasey/aoc/utils"
	s "strings"
)

func Part2() {
	theirsMap := map[string]int{"A": 1, "B": 2, "C": 3}
	outcomeMap := map[string]int{"X": 0, "Y": 3, "Z": 6}
	offsetMap := map[string]int{"X": -1, "Y": 0, "Z": 1}

	score := 0
	for _, line := range u.Read("day02") {
		guide := s.Split(line, " ")
		theirs := theirsMap[guide[0]]
		mine := ((theirs + 2 + offsetMap[guide[1]]) % 3) + 1
		score += mine + outcomeMap[guide[1]]
	}

	u.Out(score)
}
