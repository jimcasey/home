package day04

import (
	"jimcasey/aoc/utils"
	"strconv"
	"strings"
)

func init() {
	utils.Register(4, part1, part2)
}

func getPair(line string) []int {
	var pair []int
	for _, secStr := range strings.FieldsFunc(line, func(c rune) bool {
		return c == ',' || c == '-'
	}) {
		secInt, _ := strconv.Atoi(secStr)
		pair = append(pair, secInt)
	}
	return pair
}

func part1() {
	count := 0

	for _, line := range utils.Read() {
		pair := getPair(line)

		if (pair[0] <= pair[2] && pair[1] >= pair[3]) || (pair[2] <= pair[0] && pair[3] >= pair[1]) {
			count++
		}
	}
	utils.Out(count)
}

func part2() {
	count := 0

	for _, line := range utils.Read() {
		pair := getPair(line)

		for i := pair[0]; i <= pair[1]; i++ {
			if pair[2] <= i && i <= pair[3] {
				count++
				break
			}
		}
	}
	utils.Out(count)
}
