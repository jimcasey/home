package day24

import (
	c "jimcasey/aoc/collections"
	u "jimcasey/aoc/utils"
	"strconv"
)

func init() {
	u.Register(24, part1, part2)
}

var vectors = map[string]Coord{
	"^": {0, -1},
	">": {1, 0},
	"v": {0, 1},
	"<": {-1, 0},
}

type Coord struct{ x, y int }

type Storm struct {
	dir string
	loc Coord
}

type Valley struct {
	grid     [][]string
	storms   []Storm
	moves    int
	entrance Coord
	exit     Coord
}

func NewValley() Valley {
	valley := Valley{
		[][]string{},
		[]Storm{},
		0,
		Coord{1, 0},
		Coord{},
	}
	for y, line := range u.Read() {
		row := []string{}
		for x, point := range line {
			row = append(row, string(point))
			if point != '#' && point != '.' {
				valley.storms = append(valley.storms, Storm{string(point), Coord{x, y}})
			}
		}
		valley.grid = append(valley.grid, row)
	}
	valley.exit = Coord{len(valley.grid[0]) - 2, len(valley.grid) - 1}
	return valley
}

func (valley *Valley) get(loc Coord) string {
	if loc.y < 0 || len(valley.grid)-1 < loc.y {
		return "#"
	}
	row := valley.grid[loc.y]
	if loc.x < 0 || len(row)-1 < loc.x {
		return "#"
	}
	return row[loc.x]
}
func (valley *Valley) move() {
	storms := make(map[Coord][]string)
	for index, storm := range valley.storms {
		vector := vectors[storm.dir]
		loc := Coord{storm.loc.x + vector.x, storm.loc.y + vector.y}
		if valley.get(loc) == "#" {
			switch storm.dir {
			case "^":
				loc.y = len(valley.grid) - 2
			case ">":
				loc.x = 1
			case "v":
				loc.y = 1
			case "<":
				loc.x = len(valley.grid[0]) - 2
			}
		}
		valley.storms[index] = Storm{
			storm.dir,
			loc,
		}
		if _, exists := storms[loc]; !exists {
			storms[loc] = []string{storm.dir}
		} else {
			storms[loc] = append(storms[loc], storm.dir)
		}
	}
	for y, row := range valley.grid {
		for x, point := range row {
			if point != "#" {
				dirs, exists := storms[Coord{x, y}]
				if exists {
					if len(dirs) == 1 {
						valley.grid[y][x] = dirs[0]
					} else {
						valley.grid[y][x] = strconv.Itoa(len(dirs))
					}
				} else {
					valley.grid[y][x] = "."
				}
			}
		}
	}
	valley.moves++
}
func (valley *Valley) search(start Coord, end Coord) {
	options := c.NewSet(start)
	for {
		next := c.NewSet(start)
		for loc := range options {
			if valley.get(loc) == "." {
				next.Add(loc)
			}
			for _, vector := range vectors {
				option := Coord{loc.x + vector.x, loc.y + vector.y}
				if option == end {
					return
				}
				if valley.get(option) == "." {
					next.Add(option)
				}
			}
		}
		options = next
		valley.move()
	}
}

func part1() {
	valley := NewValley()
	valley.search(valley.entrance, valley.exit)
	u.Out(valley.moves)
}

func part2() {
	valley := NewValley()
	valley.search(valley.entrance, valley.exit)
	valley.search(valley.exit, valley.entrance)
	valley.search(valley.entrance, valley.exit)
	u.Out(valley.moves)
}
