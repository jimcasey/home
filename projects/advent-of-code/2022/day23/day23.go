package day23

import (
	"fmt"
	"jimcasey/aoc/collections"
	u "jimcasey/aoc/utils"
	"math"
)

func init() {
	u.Register(23, part1, part2)
}

var offsets = map[string]Coord{
	"n": {0, -1},
	"s": {0, 1},
	"e": {1, 0},
	"w": {-1, 0},
}

type Coord struct{ x, y int }
type Size struct{ xMin, yMin, xMax, yMax int }

type Elves struct {
	elfLocation   map[int]Coord
	locationElf   map[Coord]int
	proposed      map[int]Coord
	proposedCount map[Coord]int
	size          Size
	dirs          []string
	round         int
}

func NewElves() Elves {
	elves := Elves{
		make(map[int]Coord),
		make(map[Coord]int),
		make(map[int]Coord),
		make(map[Coord]int),
		Size{math.MaxInt, math.MaxInt, 0, 0},
		[]string{"n", "s", "w", "e"},
		1,
	}

	for y, line := range u.Read() {
		for x, c := range line {
			if c == '#' {
				elves.add(Coord{x, y})
			}
		}
	}
	return elves
}

func (elves *Elves) add(loc Coord) {
	elf := len(elves.elfLocation)
	elves.set(elf, loc)
}
func (elves *Elves) set(elf int, loc Coord) {
	delete(elves.locationElf, elves.elfLocation[elf])
	elves.elfLocation[elf] = loc
	elves.locationElf[loc] = elf
	elves.size = Size{
		u.Min(elves.size.xMin, loc.x),
		u.Min(elves.size.yMin, loc.y),
		u.Max(elves.size.xMax, loc.x),
		u.Max(elves.size.yMax, loc.y),
	}
}
func (elves *Elves) propose(elf int, loc Coord) {
	elves.proposed[elf] = loc
	elves.proposedCount[loc]++
}
func (elves *Elves) accept(elf int) {
	loc := elves.proposed[elf]
	delete(elves.proposed, elf)
	delete(elves.proposedCount, loc)
	elves.set(elf, loc)
}
func (elves *Elves) reject(elf int) {
	loc := elves.proposed[elf]
	delete(elves.proposed, elf)
	delete(elves.proposedCount, loc)
}
func (elves *Elves) print() {
	for y := elves.size.yMin; y <= elves.size.yMax; y++ {
		for x := elves.size.xMin; x <= elves.size.xMax; x++ {
			if _, exists := elves.locationElf[Coord{x, y}]; exists {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Println()
	}
}
func (elves *Elves) emptyCount() int {
	count := 0
	for y := elves.size.yMin; y <= elves.size.yMax; y++ {
		for x := elves.size.xMin; x <= elves.size.xMax; x++ {

			if _, exists := elves.locationElf[Coord{x, y}]; !exists {
				count++
			}
		}
	}
	return count
}
func (elves *Elves) move() bool {
	for elf, loc := range elves.elfLocation {
		neighborDirs := collections.NewSet[string]()
		for y := -1; y <= 1; y++ {
			for x := -1; x <= 1; x++ {
				if x == 0 && y == 0 {
					continue
				}
				if _, exists := elves.locationElf[Coord{loc.x + x, loc.y + y}]; exists {
					if y == -1 {
						neighborDirs.Add("n")
					}
					if y == 1 {
						neighborDirs.Add("s")
					}
					if x == -1 {
						neighborDirs.Add("w")
					}
					if x == 1 {
						neighborDirs.Add("e")
					}
				}
			}
		}

		if len(neighborDirs) > 0 {
			for _, dir := range elves.dirs {
				if !neighborDirs.Has(dir) {
					offset := offsets[dir]
					elves.propose(elf, Coord{loc.x + offset.x, loc.y + offset.y})
					break
				}
			}
		}
	}

	accept := []int{}
	reject := []int{}
	for elf, proposed := range elves.proposed {
		if elves.proposedCount[proposed] > 1 {
			reject = append(reject, elf)
		} else {
			accept = append(accept, elf)
		}
	}

	if len(accept) == 0 {
		return false
	}

	for _, elf := range accept {
		elves.accept(elf)
	}
	for _, elf := range reject {
		elves.reject(elf)
	}
	elves.round++

	elves.dirs = append(elves.dirs[1:], elves.dirs[0])

	return true
}

func part1() {
	elves := NewElves()
	for i := 0; i < 10; i++ {
		elves.move()
	}

	elves.print()
	u.Out(elves.emptyCount())
}

func part2() {
	elves := NewElves()
	for elves.move() {
	}

	elves.print()
	u.Out(elves.round)
}
