package day10

import (
	"fmt"
	"jimcasey/aoc/utils"
	"strconv"
	"strings"
)

func init() {
	utils.Register(10, part1, part2)
}

func parseInput() []int {
	instructions := utils.Read()
	values := []int{1}
	var addCache *int

	for index := 0; index < len(instructions) || addCache != nil; {
		values = append(values, values[len(values)-1])
		if addCache != nil {
			values[len(values)-1] += *addCache
			addCache = nil
		} else {
			instruction := instructions[index]
			index++
			if instruction != "noop" {
				add, _ := strconv.Atoi(strings.Split(instruction, " ")[1])
				addCache = &add
			}
		}
	}
	return values[:len(values)-1]
}

func part1() {
	signalStrength := 0
	for index, pos := range parseInput() {
		cycle := index + 1
		if cycle == 20 || (cycle-20)%40 == 0 {
			signalStrength += pos * cycle
		}
	}
	utils.Out(signalStrength)
}

func part2() {
	for cycle, pos := range parseInput() {
		rowPos := cycle % 40

		if pos-1 <= rowPos && rowPos <= pos+1 {
			fmt.Print("#")
		} else {
			fmt.Print(" ")
		}

		if rowPos == 39 {
			fmt.Println()
		}
	}
}
