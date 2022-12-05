package day05

import (
	u "jimcasey/aoc/utils"
	"strconv"
	s "strings"
)

type StackMap = map[int][]string
type Move = map[string]int

func ParseInput() (StackMap, []Move) {
	stacks := make(StackMap)
	var moves []Move

	for _, line := range u.Read("day05") {
		if s.Contains(line, "[") {
			stack := 0
			for i := 1; i < len(line); i += 4 {
				stack++
				crate := string(line[i])
				if crate != " " {
					stacks[stack] = append(stacks[stack], crate)
				}
			}
		} else if s.Contains(line, "move") {
			move := make(Move)
			if moves == nil {
				moves = make([]Move, 1)
				moves[0] = move
			} else {
				moves = append(moves, move)
			}

			split := s.Split(line, " ")
			for i := 0; i < 6; i += 2 {
				key := split[i]
				value, _ := strconv.Atoi(split[i+1])
				move[key] = value
			}
		}

	}

	return stacks, moves
}

func Out(stacks StackMap) {
	var topCrates string
	for i := 1; i <= len(stacks); i++ {
		topCrates += stacks[i][0]
	}
	u.Out(topCrates)
}
