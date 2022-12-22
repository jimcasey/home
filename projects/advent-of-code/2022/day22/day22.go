package day22

import (
	"fmt"
	u "jimcasey/aoc/utils"
	"regexp"
	"strings"
)

func init() {
	u.Register(22, part1, part2)
}

type Coord struct{ x, y int }
type Coords map[Coord]string

type Edges map[int]map[string]struct {
	newPos int
	newDir string
}

type Op struct {
	distance int
	turn     string
}

type State struct {
	pos int
	loc Coord
	dir string
}

func run(edges Edges) {
	lines := u.Read()

	var side int
	if *u.IsTest {
		side = 4
	} else {
		side = 50
	}

	size := Coord{0, 0}
	points := make(Coords)
	pointVisited := make(Coords)
	pointSector := make(map[Coord]int)
	sectors := make(map[int]Coords)
	sectorLoc := make(map[int]Coord)

	for y := 0; y < len(lines)-2; y++ {
		line := lines[y]
		for x, c := range line {
			if c == ' ' {
				continue
			}
			points[Coord{x, y}] = string(c)
			size.y = u.Max(size.y, y)
			size.x = u.Max(size.x, x)
		}
	}

	pos := 0
	for sectorY := 0; sectorY <= size.y/side; sectorY++ {
		for sectorX := 0; sectorX <= size.x/side; sectorX++ {
			pointX := sectorX * side
			pointY := sectorY * side
			if _, exists := points[Coord{pointX, pointY}]; !exists {
				continue
			}
			pos++
			sectors[pos] = make(Coords)
			sectorLoc[pos] = Coord{sectorX, sectorY}
			for y := 0; y < side; y++ {
				for x := 0; x < side; x++ {
					coord := Coord{x + pointX, y + pointY}
					sectors[pos][Coord{x, y}] = points[coord]
					pointSector[coord] = pos
				}
			}
		}
	}

	ops := []Op{}
	re := regexp.MustCompile("([0-9]+)|([RL])")
	matches := re.FindAllString(lines[len(lines)-1], -1)
	matches = append(matches, "")
	for i := 0; i < len(matches); i += 2 {
		ops = append(ops, Op{u.ToInt(matches[i]), matches[i+1]})
	}

	state := State{1, Coord{0, 0}, ">"}

	dirs := ">v<^"
	vectors := [...]Coord{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}

	for _, op := range ops {
		for i := 0; i < op.distance; i++ {
			pointVisited[Coord{
				sectorLoc[state.pos].x*side + state.loc.x,
				sectorLoc[state.pos].y*side + state.loc.y,
			}] = state.dir

			vector := vectors[strings.Index(dirs, state.dir)]
			next := State{
				state.pos,
				Coord{state.loc.x + vector.x, state.loc.y + vector.y},
				state.dir,
			}
			if _, exists := sectors[next.pos][next.loc]; !exists {
				edge := edges[next.pos][next.dir]
				next.pos = edge.newPos
				next.dir = edge.newDir

				switch next.dir {
				case ">":
					switch state.dir {
					case "v":
						next.loc.y = side - next.loc.x - 1
					case "<":
						next.loc.y = side - next.loc.y - 1
					case "^":
						next.loc.y = next.loc.x
					}
					next.loc.x = 0
				case "v":
					switch state.dir {
					case "<":
						next.loc.x = next.loc.y
					case "^":
						next.loc.x = side - next.loc.x - 1
					case ">":
						next.loc.x = side - next.loc.y - 1
					}
					next.loc.y = 0
				case "<":
					switch state.dir {
					case "^":
						next.loc.y = side - next.loc.x - 1
					case ">":
						next.loc.y = side - next.loc.y - 1
					case "v":
						next.loc.y = next.loc.x
					}
					next.loc.x = side - 1
				case "^":
					switch state.dir {
					case ">":
						next.loc.x = next.loc.y
					case "v":
						next.loc.x = side - next.loc.x - 1
					case "<":
						next.loc.x = side - next.loc.y - 1
					}
					next.loc.y = side - 1
				}
			}

			if sectors[next.pos][next.loc] == "#" {
				break
			}

			state = next
		}

		turnOffset := 0
		switch op.turn {
		case "R":
			turnOffset = 1
		case "L":
			turnOffset = -1
		}

		state.dir = string(dirs[(len(dirs)+strings.Index(dirs, state.dir)+turnOffset)%len(dirs)])
	}

	for y := 0; y <= size.y; y++ {
		for x := 0; x <= size.x; x++ {
			coord := Coord{x, y}
			point, exists := points[coord]
			if !exists {
				fmt.Print(" ")
				continue
			}

			visited, visitedExists := pointVisited[coord]
			if visitedExists {
				fmt.Print(visited)
				continue
			}

			if point == "." {
				fmt.Print(pointSector[coord])
				continue
			}

			fmt.Print(point)
		}
		fmt.Println()
	}

	row := sectorLoc[state.pos].y*side + state.loc.y + 1
	column := sectorLoc[state.pos].x*side + state.loc.x + 1
	facing := strings.Index(dirs, state.dir)
	password := 1000*row + 4*column + facing

	u.Out(password)
}

func part1() {
	var edges Edges
	if *u.IsTest {
		//   1
		// 234
		//   56
		edges = Edges{
			1: {
				">": {1, ">"},
				"v": {4, "v"},
				"<": {1, "<"},
				"^": {5, "^"},
			},
			2: {
				">": {3, ">"},
				"v": {2, "v"},
				"<": {4, "<"},
				"^": {2, "^"},
			},
			3: {
				">": {4, ">"},
				"v": {3, "v"},
				"<": {2, "<"},
				"^": {3, "^"},
			},
			4: {
				">": {2, ">"},
				"v": {5, "v"},
				"<": {3, "<"},
				"^": {1, "^"},
			},
			5: {
				">": {6, ">"},
				"v": {1, "v"},
				"<": {6, "<"},
				"^": {4, "^"},
			},
			6: {
				">": {5, ">"},
				"v": {6, "v"},
				"<": {5, "<"},
				"^": {6, "^"},
			},
		}
	} else {
		//  12
		//  3
		// 45
		// 6
		edges = Edges{
			1: {
				">": {2, ">"},
				"v": {3, "v"},
				"<": {2, "<"},
				"^": {5, "^"},
			},
			2: {
				">": {1, ">"},
				"v": {2, "v"},
				"<": {1, "<"},
				"^": {2, "^"},
			},
			3: {
				">": {3, ">"},
				"v": {5, "v"},
				"<": {3, "<"},
				"^": {1, "^"},
			},
			4: {
				">": {5, ">"},
				"v": {6, "v"},
				"<": {5, "<"},
				"^": {6, "^"},
			},
			5: {
				">": {4, ">"},
				"v": {1, "v"},
				"<": {4, "<"},
				"^": {3, "^"},
			},
			6: {
				">": {6, ">"},
				"v": {4, "v"},
				"<": {6, "<"},
				"^": {4, "^"},
			},
		}
	}

	run(edges) // 6032, 159034
}

func part2() {
	var edges Edges
	if *u.IsTest {
		//   1
		// 234
		//   56
		edges = Edges{
			1: {
				">": {6, "<"},
				"v": {4, "v"},
				"<": {3, "v"},
				"^": {2, "v"},
			},
			2: {
				">": {3, ">"},
				"v": {5, "^"},
				"<": {6, "^"},
				"^": {1, "v"},
			},
			3: {
				">": {4, ">"},
				"v": {5, ">"},
				"<": {2, "<"},
				"^": {1, ">"},
			},
			4: {
				">": {6, "v"},
				"v": {5, "v"},
				"<": {3, "<"},
				"^": {1, "^"},
			},
			5: {
				">": {6, ">"},
				"v": {2, "^"},
				"<": {3, "^"},
				"^": {4, "^"},
			},
			6: {
				">": {1, "<"},
				"v": {2, ">"},
				"<": {5, "<"},
				"^": {4, "<"},
			},
		}
	} else {
		//  12
		//  3
		// 45
		// 6
		edges = Edges{
			1: {
				">": {2, ">"},
				"v": {3, "v"},
				"<": {4, ">"},
				"^": {6, ">"},
			},
			2: {
				">": {5, "<"},
				"v": {3, "<"},
				"<": {1, "<"},
				"^": {6, "^"},
			},
			3: {
				">": {2, "^"},
				"v": {5, "v"},
				"<": {4, "v"},
				"^": {1, "^"},
			},
			4: {
				">": {5, ">"},
				"v": {6, "v"},
				"<": {1, ">"},
				"^": {3, ">"},
			},
			5: {
				">": {2, "<"},
				"v": {6, "<"},
				"<": {4, "<"},
				"^": {3, "^"},
			},
			6: {
				">": {5, "^"},
				"v": {2, "v"},
				"<": {1, "v"},
				"^": {4, "^"},
			},
		}
	}

	run(edges) // 5031, 147245
}
