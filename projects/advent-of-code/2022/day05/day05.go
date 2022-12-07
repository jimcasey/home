package day05

import (
	"jimcasey/aoc/utils"
	"strconv"
	"strings"
)

type StackMap = map[int][]string
type Move = map[string]int

func parseInput() (StackMap, []Move) {
	stacks := make(StackMap)
	var moves []Move

	for _, line := range utils.Read("day05") {
		if strings.Contains(line, "[") {
			stack := 0
			for i := 1; i < len(line); i += 4 {
				stack++
				crate := string(line[i])
				if crate != " " {
					stacks[stack] = append(stacks[stack], crate)
				}
			}
		} else if strings.Contains(line, "move") {
			move := make(Move)
			if moves == nil {
				moves = make([]Move, 1)
				moves[0] = move
			} else {
				moves = append(moves, move)
			}

			split := strings.Split(line, " ")
			for i := 0; i < 6; i += 2 {
				key := split[i]
				value, _ := strconv.Atoi(split[i+1])
				move[key] = value
			}
		}

	}

	return stacks, moves
}

func getTopCrates(stacks StackMap) string {
	var topCrates string
	for i := 1; i <= len(stacks); i++ {
		topCrates += stacks[i][0]
	}
	return topCrates
}

func Part1() {
	stacks, moves := parseInput()

	for _, move := range moves {
		count := move["move"]
		to := move["to"]
		from := move["from"]

		for i := 0; i < count; i++ {
			stacks[to] = append([]string{stacks[from][0]}, stacks[to]...)
			stacks[from] = stacks[from][1:]
		}
	}

	utils.Out(getTopCrates(stacks))
}

func Part2() {
	stacks, moves := parseInput()

	for _, move := range moves {
		count := move["move"]
		to := move["to"]
		from := move["from"]

		crates := make([]string, len(stacks[from]))
		copy(crates, stacks[from])

		stacks[to] = append(crates[:count], stacks[to]...)
		stacks[from] = stacks[from][count:]
	}

	utils.Out(getTopCrates(stacks))
}
