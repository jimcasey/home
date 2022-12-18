package day18

import (
	"jimcasey/aoc/queue"
	"jimcasey/aoc/set"
	"jimcasey/aoc/utils"
	"strings"
)

func init() {
	utils.Register(18, part1, part2)
}

type Point struct{ x, y, z int }

func (p *Point) adjacent() []Point {
	return []Point{
		{p.x, p.y, p.z + 1},
		{p.x, p.y, p.z - 1},
		{p.x, p.y + 1, p.z},
		{p.x, p.y - 1, p.z},
		{p.x + 1, p.y, p.z},
		{p.x - 1, p.y, p.z},
	}
}

func (p *Point) inside(start Point, end Point) bool {
	return start.x <= p.x && p.x <= end.x &&
		start.y <= p.y && p.y <= end.y &&
		start.z <= p.z && p.z <= end.z
}

func parseInput() (set.Set[Point], Point) {
	max := Point{0, 0, 0}
	cubes := make(set.Set[Point])
	for _, line := range utils.Read() {
		split := strings.Split(line, ",")
		cube := Point{
			utils.ToInt(split[0]),
			utils.ToInt(split[1]),
			utils.ToInt(split[2]),
		}
		cubes[cube] = struct{}{}
		max = Point{
			utils.Max(max.x, cube.x),
			utils.Max(max.y, cube.y),
			utils.Max(max.z, cube.z),
		}
	}
	return cubes, max
}

func calculateSides(cubes set.Set[Point]) int {
	sides := 0
	for cube := range cubes {
		for _, adjacent := range cube.adjacent() {
			if !cubes.Has(adjacent) {
				sides++
			}
		}
	}
	return sides
}

func part1() {
	cubes, _ := parseInput()
	utils.Out(calculateSides(cubes))
}

func part2() {
	cubes, end := parseInput()
	start := Point{0, 0, 0}

	q := queue.NewQueue[Point]()
	q.Add(start)
	seen := set.NewSet[Point]()
	for q.Length() > 0 {
		point := q.Pop()
		if point.inside(start, end) && !cubes.Has(point) {
			seen.Add(point)
			for _, adjacent := range point.adjacent() {
				if !seen.Has(adjacent) {
					q.Add(adjacent)
				}
			}
		}
	}

	total := set.NewSet[Point]()
	for z := 0; z <= end.z; z++ {
		for y := 0; y <= end.y; y++ {
			for x := 0; x <= end.x; x++ {
				p := Point{x, y, z}
				if !seen.Has(p) {
					total.Add(p)
				}
			}
		}
	}

	utils.Out(calculateSides(total))
}
