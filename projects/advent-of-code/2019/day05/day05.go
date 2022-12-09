package day05

import (
	"jimcasey/aoc/intcode"
	"jimcasey/aoc/utils"
)

func init() {
	utils.Register(5, part1)
}

func part1() {
	program := intcode.Parse(utils.Read()[0])
	utils.Out(intcode.Run(program))
}
