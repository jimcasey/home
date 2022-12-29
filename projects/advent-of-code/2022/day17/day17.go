package day17

import (
	c "jimcasey/aoc/collections"
	u "jimcasey/aoc/utils"
	"math"
)

func init() {
	u.Register(17, part1, part2)
}

type Coord struct{ x, y int }

type Stack struct {
	items     c.Set[Coord]
	height    int
	bottom    int
	tops      [7]int
	jets      string
	jetCount  int
	shapes    [][]Coord
	rockCount int
}

func NewStack() Stack {
	stack := []Coord{{0, 0}, {1, 0}, {2, 0}, {3, 0}, {4, 0}, {5, 0}, {6, 0}}

	return Stack{
		c.NewSet(stack...),
		0,
		0,
		[7]int{},
		u.Read()[0],
		0,
		[][]Coord{
			// ####
			{
				{2, 0}, {3, 0}, {4, 0}, {5, 0},
			},

			// .#.
			// ###
			// .#.
			{
				{3, 2},
				{2, 1}, {3, 1}, {4, 1},
				{3, 0},
			},

			// ..#
			// ..#
			// ###
			{
				{4, 2},
				{4, 1},
				{2, 0}, {3, 0}, {4, 0},
			},

			// #
			// #
			// #
			// #
			{
				{2, 3},
				{2, 2},
				{2, 1},
				{2, 0},
			},

			// ##
			// ##
			{
				{2, 1}, {3, 1},
				{2, 0}, {3, 0},
			},
		},
		0,
	}
}

func (s *Stack) jetIndex() int {
	return s.jetCount % len(s.jets)
}
func (s *Stack) shapeIndex() int {
	return s.rockCount % len(s.shapes)
}
func (s *Stack) blocked(rock []Coord) bool {
	for _, coord := range rock {
		if coord.x < 0 || 7 <= coord.x || s.items.Has(coord) {
			return true
		}
	}
	return false
}
func (s *Stack) move(rock []Coord, x, y int) []Coord {
	next := []Coord{}
	for _, coord := range rock {
		next = append(next, Coord{coord.x + x, coord.y + y})
	}
	return next
}
func (s *Stack) next() {
	rock := s.move(s.shapes[s.shapeIndex()], 0, s.height+4)
	s.rockCount++
	for {
		jet := s.jets[s.jetIndex()]
		s.jetCount++

		offset := 1
		if jet == '<' {
			offset = -1
		}

		next := s.move(rock, offset, 0)
		if !s.blocked(next) {
			rock = next
		}

		next = s.move(rock, 0, -1)
		if s.blocked(next) {
			break
		}
		rock = next
	}

	for _, coord := range rock {
		s.items.Add(coord)
		s.height = u.Max(s.height, coord.y)
		s.tops[coord.x] = u.Max(s.tops[coord.x], coord.y)
	}

	bottom := math.MaxInt
	for _, y := range s.tops {
		bottom = u.Min(bottom, y)
	}

	for y := bottom; y >= s.bottom; y-- {
		for x := 0; x < 7; x++ {
			s.items.Remove(Coord{y, x})
		}
	}

	s.bottom = bottom
}

type StateKey struct {
	shapeIndex, jetIndex int
	topo                 [7]int
}
type State struct{ rockCount, height int }

func part1() {
	stack := NewStack()
	for stack.rockCount < 2022 {
		stack.next()
	}
	u.Out(stack.height) // 3068, 3168
}

func part2() {
	stack := NewStack()
	states := make(map[StateKey]State)
	target := 1000000000000
	found := false

	for stack.rockCount < target {
		stack.next()
		if found {
			continue
		}

		key := StateKey{}
		key.shapeIndex = stack.shapeIndex()
		key.jetIndex = stack.jetIndex()
		for x, y := range stack.tops {
			key.topo[x] = y - stack.bottom
		}

		if state, exists := states[key]; exists {
			found = true

			cycleRockCount := stack.rockCount - state.rockCount
			remaining := target - stack.rockCount
			cycles := remaining / cycleRockCount
			stack.rockCount += cycleRockCount * cycles

			cycleHeight := stack.height - state.height
			heightOffset := cycleHeight * cycles
			stack.height += heightOffset
			stack.bottom += heightOffset

			items := c.NewSet[Coord]()
			for coord := range stack.items {
				items.Add(Coord{coord.x, coord.y + heightOffset})
			}
			stack.items = items

			for x := range stack.tops {
				stack.tops[x] += heightOffset
			}
		} else {
			states[key] = State{stack.rockCount, stack.height}
		}
	}
	u.Out(stack.height)
}
