package day01

import (
	"jimcasey/aoc/utils"
	"math"
	"strconv"
)

func init() {
	utils.Register(1, part1, part2)
}

func calculateFuel(mass float64) float64 {
	return math.Floor(mass/3) - 2
}

func parseInput() []float64 {
	var modules []float64
	for _, line := range utils.Read() {
		mass, _ := strconv.ParseFloat(line, 64)
		modules = append(modules, mass)
	}
	return modules
}

func part1() {
	var fuelRequirements float64
	for _, mass := range parseInput() {
		fuelRequirements += calculateFuel(mass)
	}
	utils.Out(int(fuelRequirements))
}

func part2() {
	var fuelRequirements float64
	for _, mass := range parseInput() {
		for feul := calculateFuel(mass); feul >= 0; feul = calculateFuel(feul) {
			fuelRequirements += feul
		}
	}
	utils.Out(int(fuelRequirements))
}
