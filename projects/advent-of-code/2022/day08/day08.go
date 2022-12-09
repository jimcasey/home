package day08

import (
	"jimcasey/aoc/utils"
	"strconv"
)

func init() {
	utils.Register(8, part1, part2)
}

type Coord struct {
	x int
	y int
}

func parseInput() (map[Coord]int, Coord) {
	grid := make(map[Coord]int)

	limit := Coord{}
	for y, line := range utils.Read() {
		limit.y = utils.Max(limit.y, y)
		for x, tree := range line {
			limit.x = utils.Max(limit.x, x)
			height, _ := strconv.Atoi(string(tree))
			grid[Coord{x, y}] = height
		}
	}
	return grid, limit
}

// TODO refactor
func part1() {
	grid, limit := parseInput()

	var searchPatterns [][]Coord

	for x := 1; x < limit.x; x++ {
		var p []Coord
		var pRev []Coord
		for y := 0; y <= limit.y; y++ {
			coord := Coord{x, y}
			p = append(p, coord)
			pRev = append([]Coord{coord}, pRev...)
		}
		searchPatterns = append(searchPatterns, p)
		searchPatterns = append(searchPatterns, pRev)
	}

	for y := 1; y < limit.y; y++ {
		var p []Coord
		var pRev []Coord
		for x := 0; x <= limit.x; x++ {
			coord := Coord{x, y}
			p = append(p, coord)
			pRev = append([]Coord{coord}, pRev...)
		}
		searchPatterns = append(searchPatterns, p)
		searchPatterns = append(searchPatterns, pRev)
	}

	visible := map[Coord]struct{}{
		{0, 0}:             {},
		{limit.x, 0}:       {},
		{0, limit.y}:       {},
		{limit.x, limit.y}: {},
	}

	for _, p := range searchPatterns {
		highest := -1
		for _, coord := range p {
			current := grid[coord]
			if current > highest {
				visible[coord] = struct{}{}
			}
			highest = utils.Max(highest, current)
		}
	}

	utils.Out(len(visible))
}

func part2() {
	grid, limit := parseInput()

	insideLimit := func(coord Coord) bool {
		return 0 <= coord.x && coord.x <= limit.x && 0 <= coord.y && coord.y <= limit.y
	}

	findVisible := func(coord Coord, iterate func(coord Coord) Coord) int {
		visible := 0
		for neighbor := iterate(coord); insideLimit(neighbor); neighbor = iterate(neighbor) {
			visible++

			if grid[neighbor] >= grid[coord] {
				break
			}
		}
		return visible
	}

	maxScore := 0
	for coord := range grid {
		up := findVisible(coord, func(c Coord) Coord { c.y--; return c })
		right := findVisible(coord, func(c Coord) Coord { c.x++; return c })
		down := findVisible(coord, func(c Coord) Coord { c.y++; return c })
		left := findVisible(coord, func(c Coord) Coord { c.x--; return c })
		maxScore = utils.Max(maxScore, left*right*up*down)
	}

	utils.Out(maxScore)
}
