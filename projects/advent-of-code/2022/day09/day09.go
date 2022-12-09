package day09

import (
	"jimcasey/aoc/utils"
	"strconv"
	"strings"
)

func init() {
	utils.Register(9, part1, part2)
}

type Coord struct {
	x int
	y int
}

func run(ropeLength int) {
	rope := make([]Coord, ropeLength)
	tailPositions := make(map[Coord]struct{})

	for _, line := range utils.Read() {
		split := strings.Split(line, " ")
		direction := split[0]
		distance, _ := strconv.Atoi(split[1])

		var vector Coord
		switch direction {
		case "U":
			vector = Coord{0, 1}
		case "R":
			vector = Coord{1, 0}
		case "D":
			vector = Coord{0, -1}
		case "L":
			vector = Coord{-1, 0}
		}

		for i := 0; i < distance; i++ {
			rope[0] = Coord{rope[0].x + vector.x, rope[0].y + vector.y}

			for i := 1; i < len(rope); i++ {
				prev := rope[i-1]
				offset := Coord{prev.x - rope[i].x, prev.y - rope[i].y}

				if utils.Abs(offset.x) > 1 || utils.Abs(offset.y) > 1 {
					rope[i].x += offset.x / utils.Max(utils.Abs(offset.x), 1)
					rope[i].y += offset.y / utils.Max(utils.Abs(offset.y), 1)
				}
			}
			tailPositions[rope[len(rope)-1]] = struct{}{}
		}
	}

	utils.Out(len(tailPositions))
}

func part1() {
	run(2)
}

func part2() {
	run(10)
}
