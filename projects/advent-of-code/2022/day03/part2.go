package day03

import (
	u "jimcasey/aoc/utils"
	s "strings"
)

func Part2() {
	var lines []string
	lines = append(lines, u.Read("day03")...)

	const priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	var sum int

	for group := 0; group < len(lines); group += 3 {
		var match rune
		for _, itemA := range lines[group] {
			for _, itemB := range lines[group+1] {
				if itemA == itemB {
					for _, itemC := range lines[group+2] {
						if itemB == itemC {
							match = itemC
							break
						}
					}
				}
				if match != 0 {
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
