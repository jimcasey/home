package day03

import (
	"jimcasey/aoc/utils"
	"math"
	"strconv"
	"strings"
)

func init() {
	utils.Register(3, part1, part2)
}

type Coord struct {
	x float64
	y float64
}

func parseInput() []map[Coord]float64 {
	var paths []map[Coord]float64
	for _, line := range utils.Read() {
		length := float64(0)
		path := make(map[Coord]float64)
		pos := Coord{x: 0, y: 0}

		for _, direction := range strings.Split(line, ",") {
			var offset Coord
			switch direction[0] {
			case 'U':
				offset.y = 1
			case 'R':
				offset.x = 1
			case 'D':
				offset.y = -1
			case 'L':
				offset.x = -1
			}

			steps, _ := strconv.Atoi(direction[1:])
			for step := 0; step < steps; step++ {
				length++
				coord := Coord{
					x: pos.x + offset.x,
					y: pos.y + offset.y,
				}
				path[coord] = length
				pos = coord
			}
		}
		paths = append(paths, path)
	}
	return paths
}

func part1() {
	paths := parseInput()

	distance := math.MaxFloat64
	for coord := range paths[1] {
		if _, exists := paths[0][coord]; exists {
			distance = math.Min(distance, math.Abs(coord.x)+math.Abs(coord.y))
		}
	}

	utils.Out(int(distance))
}

func part2() {
	paths := parseInput()

	length := math.MaxFloat64
	for coord, lengthA := range paths[1] {
		if lengthB, exists := paths[0][coord]; exists {
			length = math.Min(length, lengthA+lengthB)
		}
	}

	utils.Out(length)
}
