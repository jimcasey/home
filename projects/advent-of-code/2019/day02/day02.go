package day02

import (
	"jimcasey/aoc/intcode"
	"jimcasey/aoc/utils"
)

func init() {
	utils.Register(2, part1, part2)
}

func part1() {
	program := utils.Read()[0]
	app := intcode.NewApp(program, 12, 2)
	utils.Out(app.Exec())
}

func part2() {
	program := utils.Read()[0]
	for noun := 0; noun <= 100; noun++ {
		for verb := 0; verb <= 100; verb++ {
			app := intcode.NewApp(program, noun, verb)
			if app.Exec() == 19690720 {
				utils.Out(100*noun + verb)
				return
			}
		}
	}
}
