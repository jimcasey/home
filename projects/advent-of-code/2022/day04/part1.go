package day04

import (
	u "jimcasey/aoc/utils"
	"strconv"
	s "strings"
)

func Part1() {
	count := 0

	for _, line := range u.Read("day04") {
		var pair []int
		for _, secStr := range s.FieldsFunc(line, func(c rune) bool {
			return c == ',' || c == '-'
		}) {
			secInt, _ := strconv.Atoi(secStr)
			pair = append(pair, secInt)
		}

		if (pair[0] <= pair[2] && pair[1] >= pair[3]) || (pair[2] <= pair[0] && pair[3] >= pair[1]) {
			count++
		}
	}
	u.Out(count)
}
