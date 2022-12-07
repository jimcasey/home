package day03

import (
	"jimcasey/aoc/utils"
	"strings"
)

const priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func Part1() {
	var sum int
	for _, line := range utils.Read("day03") {
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

		sum += strings.Index(priorities, string(match)) + 1
	}

	utils.Out(sum)
}

func Part2() {
	var lines []string
	lines = append(lines, utils.Read("day03")...)

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
		sum += strings.Index(priorities, string(match)) + 1
	}
	utils.Out(sum)
}
