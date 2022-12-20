package day20

import (
	u "jimcasey/aoc/utils"
)

func init() {
	u.Register(20, part1, part2)
}

func wrap(pos int, length int) int {
	for pos < 0 {
		pos += length
	}
	return pos % length
}

func run(iterations int, key int) {
	input := []*int{}
	var zero *int
	for _, line := range u.Read() {
		num := u.ToInt(line) * key
		input = append(input, &num)
		if num == 0 {
			zero = &num
		}
	}
	length := len(input)

	prev := make(map[*int]*int)
	next := make(map[*int]*int)

	for i := 0; i < length; i++ {
		prev[input[i]] = input[wrap(i-1, length)]
		next[input[i]] = input[wrap(i+1, length)]
	}

	for i := 0; i < iterations; i++ {
		for _, num := range input {
			if *num != 0 {
				next[prev[num]] = next[num]
				prev[next[num]] = prev[num]

				movePlaces := *num % (length - 1)

				var after *int
				var before *int
				if movePlaces > 0 {
					after = num
					for j := 0; j < movePlaces; j++ {
						after = next[after]
					}
					before = next[after]
				} else {
					before = num
					for i := 0; i > movePlaces; i-- {
						before = prev[before]
					}
					after = prev[before]
				}

				next[num] = before
				next[after] = num

				prev[num] = after
				prev[before] = num
			}
		}
	}

	sum := 0
	for i, num := 0, zero; i <= 3000; i, num = i+1, next[num] {
		if i%1000 == 0 {
			sum += *num
		}
	}
	u.Out(sum)
}

func part1() {
	run(1, 1)
}

func part2() {
	run(10, 811589153)
}
