package day06

import (
	u "jimcasey/aoc/utils"
)

func findPosition(markerOffset int, message string) int {
	var position int
	for i := 0; i <= len(message)-markerOffset; i++ {
		potentialMarker := message[i : i+markerOffset]
		counts := make(map[rune]int)
		for _, c := range potentialMarker {
			counts[c]++
			if counts[c] == 2 {
				potentialMarker = ""
				continue
			}
		}
		if potentialMarker != "" {
			position = i + markerOffset
			break
		}
	}
	return position
}

func Part1() {
	for _, line := range u.Read("day06") {
		u.Out(findPosition(4, line))
	}
}

func Part2() {
	for _, line := range u.Read("day06") {
		u.Out(findPosition(14, line))
	}
}
