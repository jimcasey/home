package day02

import (
	"jimcasey/aoc/intcode"
	"jimcasey/aoc/utils"
)

func init() {
	utils.Register(2, part1, part2)
}

func part1() {
	program := intcode.Parse(utils.Read()[0])
	utils.Out(intcode.Run(program, 12, 2))
}

func part2() {
	program := intcode.Parse(utils.Read()[0])
	for noun := 0; noun <= 100; noun++ {
		for verb := 0; verb <= 100; verb++ {
			result := intcode.Run(program, noun, verb)
			if result == 19690720 {
				utils.Out(100*noun + verb)
				return
			}
		}
	}
}
