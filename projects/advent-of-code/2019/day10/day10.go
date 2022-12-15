package day10

import (
	"jimcasey/aoc/utils"
)

func init() {
	utils.Register(10, part1)
}

type Coord struct {
	x int
	y int
}

func (coord *Coord) add(a Coord) Coord {
	return Coord{coord.x + a.x, coord.y + a.y}
}
func (coord *Coord) subtract(a Coord) Coord {
	return Coord{coord.x - a.x, coord.y - a.y}
}
func (coord *Coord) inBounds(max Coord) bool {
	return 0 <= coord.x && coord.x < max.x && 0 <= coord.y && coord.y < max.y
}
func (coord *Coord) offset(a Coord) Coord {
	b := coord.subtract(a)
	if b.x == 0 {
		return Coord{0, b.y}
	}
	if b.y == 0 {
		return Coord{b.x, 0}
	}

	n := utils.Abs(b.x)
	m := utils.Abs(b.y)

	for m != 0 {
		t := m
		m = n % m
		n = t
	}

	return Coord{b.x / n, b.y / n}
}

type CoordMap struct {
	items map[Coord]struct{}
}

func NewCoordMap() CoordMap {
	return CoordMap{make(map[Coord]struct{})}
}

func (coordMap *CoordMap) add(coord Coord) {
	coordMap.items[coord] = struct{}{}
}
func (coordMap *CoordMap) exists(coord Coord) bool {
	_, exists := coordMap.items[coord]
	return exists
}
func (coordMap *CoordMap) delete(coord Coord) {
	delete(coordMap.items, coord)
}
func (coordMap *CoordMap) pop() Coord {
	var coord Coord
	for c := range coordMap.items {
		coord = c
	}
	coordMap.delete(coord)
	return coord
}
func (coordMap *CoordMap) len() int {
	return len(coordMap.items)
}

// // greatest common divisor (GCD) via Euclidean algorithm
// func GCD(a, b int) int {
// 	for b != 0 {
// 		t := b
// 		b = a % b
// 		a = t
// 	}
// 	return a
// }

// // find Least Common Multiple (LCM) via GCD
// func LCM(a, b int, integers ...int) int {
// 	result := a * b / GCD(a, b)

// 	for i := 0; i < len(integers); i++ {
// 		result = LCM(result, integers[i])
// 	}

// 	return result
// }

func parseInput() (CoordMap, Coord) {
	asteroids := NewCoordMap()
	max := Coord{0, 0}

	for y, line := range utils.Read() {
		max.y = utils.Max(max.y, y)
		for x, c := range line {
			max.x = utils.Max(max.x, x)
			if c == '#' {
				asteroids.add(Coord{x, y})
			}
		}
	}
	return asteroids, max
}

func part1() {
	asteroids, max := parseInput()

	// for _, asteroid := range asteroids {
	// }
	asteroid := Coord{3, 4}

	visible := NewCoordMap()
	searchMap := NewCoordMap()
	for coord := range asteroids.items {
		searchMap.add(coord)
	}

	for search := searchMap.pop(); searchMap.len() > 0; search = searchMap.pop() {
		if search == asteroid {
			visible.add(search)
			continue
		}

		offset := search.offset(asteroid)
		blocker := false
		for possible := asteroid.add(offset); possible.inBounds(max); possible = possible.add(offset) {
			if asteroids.exists(possible) {
				if blocker {
					searchMap.delete(possible)
				} else {
					blocker = true
					visible.add(possible)
				}
			}
		}
	}
	utils.Out(visible.len())

	// center := Coord{0, 0}
	// inBounds := func(coord Coord, offset Coord) bool {
	// 	return 0-offset.x <= coord.x &&
	// 		coord.x < width-offset.x &&
	// 		0-offset.y <= coord.y &&
	// 		coord.y < height-offset.y
	// }

	// // for coord := range asteroids {
	// coord := Coord{3, 4}
	// possible := make(map[Coord]struct{})
	// for c := range asteroids {
	// 	possible[Coord{
	// 		coord.x - c.x,
	// 		coord.y - c.y,
	// 	}] = struct{}{}
	// }

	// // pop := func() Coord {
	// // 	var find Coord
	// // 	for c := range possible {
	// // 		find = c
	// // 	}
	// // 	delete(possible, find)
	// // 	return find
	// // }

	// visible := make(map[Coord]struct{})
	// // for len(possible) > 0 {
	// // 	test := pop()
	// utils.Out(possible)
	// for test := range possible {
	// 	utils.Out("---")

	// 	if test == center {
	// 		visible[center] = struct{}{}
	// 		continue
	// 	}

	// 	_, testExists := possible[test]
	// 	utils.Out("test", test, testExists)

	// 	// blocker := false
	// 	offset := getOffset(test)

	// 	_, offsetExists := possible[offset]
	// 	utils.Out("offset", offset, offsetExists)

	// 	for search := offset; inBounds(search, coord); search = addCoord(search, offset) {
	// 		_, exists := possible[search]
	// 		utils.Out("search", search, exists)
	// 		// if _, exists := possible[search]; exists {
	// 		// 	// utils.Out("found", search, blocker)
	// 		// 	// blocker = true
	// 		// 	// if !blocker {
	// 		// 	visible[search] = struct{}{}
	// 		// 	// 	blocker = true
	// 		// 	// } else {
	// 		// 	// 	delete(possible, search)
	// 		// 	// }
	// 		// }
	// 	}
	// }
	// // }
	// utils.Out(visible)

	// // A 3,1 6,2 9,3 = 3,1
	// // B 3,2 6,4 9,6 = 3,2
	// // C 3,3 4,4 5,5 6,6 7,7 8,8, 9,9 = 1,1
	// // D 2,3 4,6 6,9 = 2,3
	// // E 1,3 2,6 3,9 = 1,3
	// // F 2,4 3,6 4,8 = 1,2

	// // t := [][]Coord{
	// // 	{{3, 1}, {6, 2}, {9, 3}},
	// // 	{{3, 2}, {6, 4}, {9, 6}},
	// // 	{{3, 3}, {4, 4}, {5, 5}, {6, 6}, {7, 7}, {8, 8}, {9, 9}},
	// // 	{{2, 3}, {4, 6}, {6, 9}},
	// // 	{{1, 3}, {2, 6}, {3, 9}},
	// // 	{{2, 4}, {3, 6}, {4, 8}},
	// // }
	// // utils.Out(t)

	// // for _, coords := range t {
	// // 	for _, c := range coords {
	// // 		g := gcd(c.x, c.y)
	// // 		utils.Out(c, Coord{c.x / g, c.y / g})
	// // 	}
	// // 	utils.Out("---")
	// // }

	// // }
}
