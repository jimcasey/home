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
//    (2) relative mode: value at parameter relative to base

type App struct {
	Status       string // waiting, done
	memory       map[int]int
	pointer      int
	relativeBase int
	output       []int
}

func NewApp(program string, inputs ...int) App {
	app := App{
		"waiting",
		make(map[int]int),
		0,
		0,
		[]int{},
	}

	for i, s := range strings.Split(program, ",") {
		value, _ := strconv.Atoi(s)
		app.memory[i] = value
	}

	for i, input := range inputs {
		app.memory[i+1] = input
	}

	return app
}

func (app *App) read(position int) int {
	op := app.memory[app.pointer]
	mode := op / int(math.Pow(10, float64(position)+1)) % 10

	var address int
	switch mode {
	case 0:
		address = app.memory[app.pointer+position]
	case 1:
		address = app.pointer + position
	case 2:
		address = app.relativeBase + app.memory[app.pointer+position]
	}

	value, exists := app.memory[address]
	if !exists {
		return 0
	}
	return value
}

func (app *App) write(position int, x int) {
	op := app.memory[app.pointer]
	mode := op / int(math.Pow(10, float64(position)+1)) % 10

	var address int
	switch mode {
	case 0:
		address = app.memory[app.pointer+position]
	case 2:
		address = app.relativeBase + app.memory[app.pointer+position]
	}

	app.memory[address] = x
}

func (app *App) writeBool(position int, x bool) {
	value := 0
	if x {
		value = 1
	}
	app.write(position, value)
}

func (app *App) Output() []int {
	return app.output
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
				return app.memory[0]
			}
			app.write(1, input)
			app.pointer += 2
		case 4: // output
			app.memory[0] = app.read(1)
			app.output = append(app.output, app.memory[0])
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
		case 9: // adjust relative base
			app.relativeBase += app.read(1)
			app.pointer += 2
		}
	}

	app.Status = "done"
	return app.memory[0]
}
