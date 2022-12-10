package day05

import (
	"jimcasey/aoc/intcode"
	"jimcasey/aoc/utils"
)

func init() {
	utils.Register(5, part1, part2)
}

func part1() {
	program := utils.Read()[0]
	app := intcode.NewApp(program)
	utils.Out(app.Exec(1))
}

func part2() {
	program := utils.Read()[0]
	app := intcode.NewApp(program)
	utils.Out(app.Exec(5))
}
