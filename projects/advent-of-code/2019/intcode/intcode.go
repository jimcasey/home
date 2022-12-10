package intcode

import (
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

type App struct {
	Status  string // waiting, done
	memory  []int
	pointer int
}

func (app *App) read(position int) int {
	op := app.memory[app.pointer]
	mode := op / int(math.Pow(10, float64(position)+1)) % 10

	switch mode {
	case 0:
		return app.memory[app.memory[app.pointer+position]]
	case 1:
		return app.memory[app.pointer+position]
	}

	return 0
}

func (app *App) write(position int, x int) {
	app.memory[app.memory[app.pointer+position]] = x
}

func (app *App) writeBool(position int, x bool) {
	value := 0
	if x {
		value = 1
	}
	app.write(position, value)
}

func (app *App) Result() int {
	return app.memory[0]
}

func (app *App) Exec(inputs ...int) int {
	for app.memory[app.pointer] != 99 {
		opcode := app.memory[app.pointer] % 100

		switch opcode {
		case 1: // addition
			app.write(3, app.read(1)+app.read(2))
			app.pointer += 4
		case 2: // multiplication
			app.write(3, app.read(1)*app.read(2))
			app.pointer += 4
		case 3: // input
			var input int
			if len(inputs) > 0 {
				input = inputs[0]
				inputs = inputs[1:]
			} else {
				app.Status = "waiting"
				return app.Result()
			}
			app.write(1, input)
			app.pointer += 2
		case 4: // output
			app.memory[0] = app.read(1)
			app.pointer += 2
		case 5: // jump-if-true
			if app.read(1) != 0 {
				app.pointer = app.read(2)
			} else {
				app.pointer += 3
			}
		case 6: // jump-if-false
			if app.read(1) == 0 {
				app.pointer = app.read(2)
			} else {
				app.pointer += 3
			}
		case 7: // less than
			app.writeBool(3, app.read(1) < app.read(2))
			app.pointer += 4
		case 8: // equals
			app.writeBool(3, app.read(1) == app.read(2))
			app.pointer += 4
		}
	}

	app.Status = "done"
	return app.Result()
}

func NewApp(program string, inputs ...int) App {
	app := App{
		Status:  "waiting",
		memory:  []int{},
		pointer: 0,
	}

	for _, s := range strings.Split(program, ",") {
		op, _ := strconv.Atoi(s)
		app.memory = append(app.memory, op)
	}

	for i, input := range inputs {
		app.memory[i+1] = input
	}

	return app
}

// func Load(program []int, inputs ...int) []int {
// 	memory := make([]int, len(program))
// 	for i, input := range inputs {
// 		memory[i+1] = input
// 	}
// 	copy(memory, program)
// 	return memory
// }

// func Run(memory []int, inputs ...int) ([]int, string) {
// 	var pointer int

// 	read := func(position int) int {
// 		op := memory[pointer]
// 		mode := op / int(math.Pow(10, float64(position)+1)) % 10

// 		switch mode {
// 		case 0:
// 			return memory[memory[pointer+position]]
// 		case 1:
// 			return memory[pointer+position]
// 		}

// 		return 0
// 	}

// 	write := func(position int, x int) {
// 		memory[memory[pointer+position]] = x
// 	}

// 	writeBool := func(position int, x bool) {
// 		value := 0
// 		if x {
// 			value = 1
// 		}
// 		write(position, value)
// 	}

// 	for pointer = 0; memory[pointer] != 99; {
// 		opcode := memory[pointer] % 100

// 		switch opcode {
// 		case 1: // addition
// 			write(3, read(1)+read(2))
// 			pointer += 4
// 		case 2: // multiplication
// 			write(3, read(1)*read(2))
// 			pointer += 4
// 		case 3: // input
// 			var input int
// 			if len(inputs) > 0 {
// 				input = inputs[0]
// 				inputs = inputs[1:]
// 			} else {
// 				return memory, "input-needed"
// 			}
// 			write(1, input)
// 			pointer += 2
// 		case 4: // output
// 			memory[0] = read(1)
// 			pointer += 2
// 		case 5: // jump-if-true
// 			if read(1) != 0 {
// 				pointer = read(2)
// 			} else {
// 				pointer += 3
// 			}
// 		case 6: // jump-if-false
// 			if read(1) == 0 {
// 				pointer = read(2)
// 			} else {
// 				pointer += 3
// 			}
// 		case 7: // less than
// 			writeBool(3, read(1) < read(2))
// 			pointer += 4
// 		case 8: // equals
// 			writeBool(3, read(1) == read(2))
// 			pointer += 4
// 		}
// 	}

// 	return memory, "done"
// }
