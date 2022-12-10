package day07

import (
	"jimcasey/aoc/intcode"
	"jimcasey/aoc/utils"
)

func init() {
	utils.Register(7, part1, part2)
}

func part1() {
	program := utils.Read()[0]

	maxSignal := 0
	for _, phases := range utils.Permutations([]int{0, 1, 2, 3, 4}) {
		signal := 0
		for _, phase := range phases {
			app := intcode.NewApp(program)
			signal = app.Exec(phase, signal)
		}
		maxSignal = utils.Max(maxSignal, signal)
	}
	utils.Out(maxSignal)
}

func part2() {
	program := utils.Read()[0]

	maxSignal := 0
	for _, phases := range utils.Permutations([]int{5, 6, 7, 8, 9}) {
		apps := []intcode.App{}
		signal := 0
		for i, phase := range phases {
			apps = append(apps, intcode.NewApp(program))
			signal = apps[i].Exec(phase, signal)
		}

		for i := 0; apps[i].Status != "done"; i = (i + 1) % len(apps) {
			signal = apps[i].Exec(signal)
		}

		maxSignal = utils.Max(maxSignal, signal)
	}
	utils.Out(maxSignal)
}
