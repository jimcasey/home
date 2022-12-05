package day05

func Part2() {
	stacks, moves := ParseInput()

	for _, move := range moves {
		count := move["move"]
		to := move["to"]
		from := move["from"]

		crates := make([]string, len(stacks[from]))
		copy(crates, stacks[from])

		stacks[to] = append(crates[:count], stacks[to]...)
		stacks[from] = stacks[from][count:]
	}

	Out(stacks)
}
