package day11

import (
	u "jimcasey/aoc/utils"
	"regexp"
	"sort"
	"strings"
)

func init() {
	u.Register(11, part1, part2)
}

type Monkey struct {
	items       []int
	operation   string
	value       int
	divisible   int
	ifTrue      int
	ifFalse     int
	inspections int
}

func run(worryDivider int, rounds int) {
	re, _ := regexp.Compile("[0-9]+")

	monkeys := make(map[int]Monkey)
	lines := u.Read()
	for i := 0; i < len(lines); i += 7 {
		monkey := u.ToInt(re.FindStringSubmatch(lines[i])[0])

		var items []int
		for _, item := range re.FindAllString(lines[i+1], -1) {
			items = append(items, u.ToInt(item))
		}

		operationLine := lines[i+2]
		var operation string
		var value int
		if strings.Contains(operationLine, "old * old") {
			operation = "square"
		} else {

			value = u.ToInt(re.FindStringSubmatch(operationLine)[0])
			if strings.Contains(operationLine, "*") {
				operation = "multiply"
			} else if strings.Contains(operationLine, "+") {
				operation = "add"
			}
		}

		divisible := u.ToInt(re.FindStringSubmatch(lines[i+3])[0])
		ifTrue := u.ToInt(re.FindStringSubmatch(lines[i+4])[0])
		ifFalse := u.ToInt(re.FindStringSubmatch(lines[i+5])[0])

		monkeys[monkey] = Monkey{
			items,
			operation,
			value,
			divisible,
			ifTrue,
			ifFalse,
			0,
		}
	}

	divider := 1
	for i := 0; i < len(monkeys); i++ {
		monkey := monkeys[i]
		divider *= monkey.divisible
	}

	for round := 1; round <= rounds; round++ {
		for current := 0; current < len(monkeys); current++ {
			monkey := monkeys[current]
			for _, item := range monkey.items {
				monkey.inspections++

				switch monkey.operation {
				case "square":
					item = item * item
				case "multiply":
					item = item * monkey.value
				case "add":
					item = item + monkey.value
				}
				item /= worryDivider
				item %= divider

				var next int
				if item%monkey.divisible == 0 {
					next = monkey.ifTrue
				} else {
					next = monkey.ifFalse
				}

				nextMonkey := monkeys[next]
				nextMonkey.items = append(nextMonkey.items, item)
				monkeys[next] = nextMonkey
			}
			monkey.items = []int{}
			monkeys[current] = monkey
		}
	}

	var inspections []int
	for _, monkey := range monkeys {
		inspections = append(inspections, monkey.inspections)
	}
	sort.Ints(inspections)

	monkeyBusiness := inspections[len(inspections)-1] * inspections[len(inspections)-2]
	u.Out(monkeyBusiness)
}

func part1() {
	run(3, 20)
}

func part2() {
	run(1, 10000)
}
