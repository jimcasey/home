package day05

func Part1() {
	stacks, moves := ParseInput()

	for _, move := range moves {
		count := move["move"]
		to := move["to"]
		from := move["from"]

		for i := 0; i < count; i++ {
			stacks[to] = append([]string{stacks[from][0]}, stacks[to]...)
			stacks[from] = stacks[from][1:]
		}
	}

	Out(stacks)
}
