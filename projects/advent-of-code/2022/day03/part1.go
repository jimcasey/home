package day03

import (
	u "jimcasey/aoc/utils"
	s "strings"
)

func Part1() {
	const priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	var sum int
	for _, line := range u.Read("day03") {
		length := len(line) / 2
		compartment1 := line[0:length]
		compartment2 := line[length:]

		var match rune
		for _, item1 := range compartment1 {
			for _, item2 := range compartment2 {
				if item1 == item2 {
					match = item1
					break
				}
			}
			if match != 0 {
				break
			}
		}

		sum += s.Index(priorities, string(match)) + 1
	}

	u.Out(sum)
}
