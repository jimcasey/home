package day02

import (
	"jimcasey/aoc/utils"
	"strconv"
	"strings"
)

func init() {
	utils.Register(2, part1, part2)
}

func parseInput() []int {
	var program []int
	for _, s := range strings.Split(utils.Read()[0], ",") {
		op, _ := strconv.Atoi(s)
		program = append(program, op)
	}
	return program
}

func runProgram(program []int, noun int, verb int) int {
	memory := make([]int, len(program))
	copy(memory, program)

	memory[1] = noun
	memory[2] = verb

	for pointer := 0; memory[pointer] != 99; pointer += 4 {
		parameter1 := memory[memory[pointer+1]]
		parameter2 := memory[memory[pointer+2]]
		var result int

		switch memory[pointer] {
		case 1:
			result = parameter1 + parameter2
		case 2:
			result = parameter1 * parameter2
		}

		memory[memory[pointer+3]] = result
	}
	return memory[0]
}

func part1() {
	program := parseInput()
	utils.Out(runProgram(program, 12, 2))
}

func part2() {
	program := parseInput()
	for noun := 0; noun <= 100; noun++ {
		for verb := 0; verb <= 100; verb++ {
			result := runProgram(program, noun, verb)
			if result == 19690720 {
				utils.Out(100*noun + verb)
				return
			}
		}
	}
}
