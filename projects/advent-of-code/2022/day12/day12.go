package day12

import (
	"jimcasey/aoc/utils"
	"math"
)

func init() {
	utils.Register(12, part1, part2)
}

type Terrain = map[Coord]rune
type Steps = map[Coord]int
type Compare = func(rune, rune) bool
type Done = func(Coord) bool

type Coord struct {
	x int
	y int
}

type Neighbor struct {
	coord     Coord
	elevation rune
}

var terrain Terrain
var start, end Coord
var steps Steps

func setTerrain() {
	terrain = make(Terrain)
	for y, line := range utils.Read() {
		for x, elevation := range line {
			coord := Coord{x, y}
			switch elevation {
			case 'S':
				start = coord
				elevation = 'a'
			case 'E':
				end = coord
				elevation = 'z'
			}
			terrain[coord] = elevation
		}
	}
}

func findNeighbors(coord Coord) []Neighbor {
	offsets := []Coord{
		{-1, 0},
		{0, 1},
		{1, 0},
		{0, -1},
	}

	var neighbors []Neighbor
	for _, neighbor := range offsets {
		option := Coord{
			coord.x + neighbor.x,
			coord.y + neighbor.y,
		}
		elevation, exists := terrain[option]
		if exists {
			neighbors = append(neighbors, Neighbor{option, elevation})
		}
	}
	return neighbors
}

func findOptions(coord Coord, compare Compare) []Coord {
	var options []Coord
	for _, neighbor := range findNeighbors(coord) {
		if compare(terrain[coord], neighbor.elevation) {
			options = append(options, neighbor.coord)
			continue
		}
	}
	return options
}

func setSteps(coord Coord, step int, compare Compare, done Done) {
	for _, option := range findOptions(coord, compare) {
		optionStep, exists := steps[option]
		if exists && optionStep <= step {
			continue
		}
		steps[option] = step

		if !done(option) {
			setSteps(option, step+1, compare, done)
		}
	}
}

func part1() {
	setTerrain()

	compare := func(x rune, y rune) bool {
		return x+1 >= y
	}
	done := func(coord Coord) bool {
		return coord == end
	}
	steps = Steps{start: 0}
	setSteps(start, 1, compare, done)

	utils.Out(steps[end])
}

func part2() {
	setTerrain()

	compare := func(x rune, y rune) bool {
		return x-1 <= y
	}
	done := func(coord Coord) bool {
		return terrain[coord] == 'a'
	}
	steps = Steps{end: 0}
	setSteps(end, 1, compare, done)

	minSteps := math.MaxInt
	for coord, elevation := range terrain {
		s, exists := steps[coord]
		if exists && elevation == 'a' {
			minSteps = utils.Min(minSteps, s)
		}
	}

	utils.Out(minSteps)
}
