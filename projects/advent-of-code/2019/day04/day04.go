package day04

import (
	"fmt"
	"jimcasey/aoc/utils"
	"strconv"
	"strings"
)

func init() {
	utils.Register(4, part1, part2)
}

func parseInput() []string {
	split := strings.Split(utils.Read()[0], "-")
	start, _ := strconv.Atoi(split[0])
	end, _ := strconv.Atoi(split[1])

	var pwds []string
	for pwd := start; pwd <= end; pwd++ {
		pwds = append(pwds, fmt.Sprint(pwd))
	}

	return pwds
}

func toInt(c byte) int {
	n, _ := strconv.Atoi(string(c))
	return n
}

func neverDecreases(pwd string) bool {
	for i := 1; i < 6; i++ {
		if toInt(pwd[i-1]) > toInt(pwd[i]) {
			return false
		}
	}
	return true
}

func hasRepeating(pwd string) bool {
	counts := make(map[rune]int)
	for _, c := range pwd {
		counts[c]++
	}

	for _, count := range counts {
		if count >= 2 {
			return true
		}
	}
	return false
}

func hasDouble(pwd string) bool {
	counts := make(map[rune]int)
	for _, c := range pwd {
		counts[c]++
	}

	for _, count := range counts {
		if count == 2 {
			return true
		}
	}
	return false
}

func part1() {
	count := 0
	for _, pwd := range parseInput() {
		if neverDecreases(pwd) && hasRepeating(pwd) {
			count++
		}
	}

	utils.Out(count)
}

func part2() {
	count := 0
	for _, pwd := range parseInput() {
		if neverDecreases(pwd) && hasDouble(pwd) {
			count++
		}
	}

	utils.Out(count)
}
