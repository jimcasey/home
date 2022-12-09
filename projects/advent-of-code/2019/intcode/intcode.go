package intcode

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// program: list of integers
// memory: current run of the program
// address: position in memory
// instruction: an opcode and set of values
// opcode: identifies what the instruction should do
// parameters: parameters of an instruction
// pointer: current position of the running instruction
// output: value at address 0 at the end of the run
// parameter modes:
// 		(0) position mode: memory address
// 		(1) immediate mode: value at the parameter

func Run(program []int, inputs ...int) int {
	var pointer int
	memory := make([]int, len(program))
	copy(memory, program)

	read := func(position int) int {
		op := memory[pointer]
		mode := op / int(math.Pow(10, float64(position)+1)) % 10

		switch mode {
		case 0:
			return memory[memory[pointer+position]]
		case 1:
			return memory[pointer+position]
		}

		return 0
	}

	write := func(position int, x int) {
		memory[memory[pointer+position]] = x
	}

	writeBool := func(position int, x bool) {
		value := 0
		if x {
			value = 1
		}
		write(position, value)
	}

	for i, input := range inputs {
		memory[i+1] = input
	}

	for pointer = 0; memory[pointer] != 99; {
		opcode := memory[pointer] % 100

		switch opcode {
		case 1: // addition
			write(3, read(1)+read(2))
			pointer += 4
		case 2: // multiplication
			write(3, read(1)*read(2))
			pointer += 4
		case 3: // input
			var input int
			fmt.Print("Input: ")
			fmt.Scanf("%d", &input)
			write(1, input)
			pointer += 2
		case 4: // output
			memory[0] = read(1)
			pointer += 2
		case 5: // jump-if-true
			if read(1) != 0 {
				pointer = read(2)
			} else {
				pointer += 3
			}
		case 6: // jump-if-false
			if read(1) == 0 {
				pointer = read(2)
			} else {
				pointer += 3
			}
		case 7: // less than
			writeBool(3, read(1) < read(2))
			pointer += 4
		case 8: // equals
			writeBool(3, read(1) == read(2))
			pointer += 4
		}
	}

	return memory[0]
}

func Parse(input string) []int {
	var program []int
	for _, s := range strings.Split(input, ",") {
		op, _ := strconv.Atoi(s)
		program = append(program, op)
	}
	return program
}
