package day04

import (
	u "jimcasey/aoc/utils"
	"strconv"
	s "strings"
)

func Part2() {
	count := 0

	for _, line := range u.Read("day04") {
		var pair []int
		for _, secStr := range s.FieldsFunc(line, func(c rune) bool {
			return c == ',' || c == '-'
		}) {
			secInt, _ := strconv.Atoi(secStr)
			pair = append(pair, secInt)
		}

		for i := pair[0]; i <= pair[1]; i++ {
			if pair[2] <= i && i <= pair[3] {
				count++
				break
			}
		}
	}
	u.Out(count)
}
