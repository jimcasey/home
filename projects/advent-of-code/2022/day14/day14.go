package day14

import (
	u "jimcasey/aoc/utils"
	"strings"
)

func init() {
	u.Register(14, part1, part2)
}

func NewCoord(str string) Coord {
	arr := strings.Split(str, ",")
	return Coord{
		u.ToInt(arr[0]),
		u.ToInt(arr[1]),
	}
}

type Coord struct {
	x int
	y int
}

func NewCave(hasFloor bool) Cave {
	return Cave{
		make(map[Coord]struct{}),
		make(map[Coord]struct{}),
		hasFloor,
		0,
	}
}

type Cave struct {
	rocks    map[Coord]struct{}
	sand     map[Coord]struct{}
	hasFloor bool
	floor    int
}

func (cave *Cave) addRock(coord Coord) {
	cave.rocks[coord] = struct{}{}
	cave.floor = u.Max(cave.floor, coord.y+2)
}
func (cave *Cave) addSand(coord Coord) {
	cave.sand[coord] = struct{}{}
}
func (cave *Cave) free(coord Coord) bool {
	_, rockExists := cave.rocks[coord]
	_, sandExists := cave.sand[coord]
	return !rockExists && !sandExists
}
func (cave *Cave) dropSand(coord Coord) bool {
	for ; cave.free(Coord{coord.x, coord.y + 1}); coord.y++ {
		if coord.y+1 == cave.floor {
			if cave.hasFloor {
				cave.addSand(coord)
				return true
			}
			return false
		}
	}

	for _, xOffset := range []int{-1, 1} {
		offset := Coord{coord.x + xOffset, coord.y + 1}
		if cave.free(offset) {
			return cave.dropSand(offset)
		}
	}

	cave.addSand(coord)
	if cave.hasFloor && coord.y == 0 {
		return false
	}
	return true
}

func run(hasFloor bool) {
	cave := NewCave(hasFloor)

	for _, line := range u.Read() {
		nodes := strings.Split(line, " -> ")
		for i := 1; i < len(nodes); i++ {
			a := NewCoord(nodes[i-1])
			b := NewCoord(nodes[i])

			for x := u.Min(a.x, b.x); x <= u.Max(a.x, b.x); x++ {
				for y := u.Min(a.y, b.y); y <= u.Max(a.y, b.y); y++ {
					cave.addRock(Coord{x, y})
				}
			}
		}
	}

	for cave.dropSand(Coord{500, 0}) {
	}
	u.Out(len(cave.sand))
}

func part1() {
	run(false)
}

func part2() {
	run(true)
}
