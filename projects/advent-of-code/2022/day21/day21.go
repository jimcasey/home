package day21

import (
	c "jimcasey/aoc/collections"
	u "jimcasey/aoc/utils"
	"strings"
)

func init() {
	u.Register(21, part1, part2)
}

type Monkey struct {
	name  string
	value float64
}

type Op struct {
	name     string
	operator string
	monkeys  []string
	values   []*float64
}

func (op *Op) set(name string, value float64) bool {
	for i := 0; i < 2; i++ {
		if op.monkeys[i] == name {
			op.values[i] = &value
		}
	}
	return op.values[0] != nil && op.values[1] != nil
}

func eval(a float64, b float64, operator string) float64 {
	switch operator {
	case "+":
		return a + b
	case "-":
		return a - b
	case "*":
		return a * b
	case "/":
		return a / b
	}
	return -1
}

func parseInput() (map[string]Op, map[string]string, []Monkey) {
	deps := make(map[string]string)
	ops := make(map[string]Op)
	values := []Monkey{}

	for _, line := range u.Read() {
		split := strings.Split(line, " ")
		monkey := split[0][0:4]

		if len(split) == 2 {
			values = append(values, Monkey{monkey, float64(u.ToInt(split[1]))})
		} else {
			op := Op{
				monkey,
				split[2],
				[]string{split[1], split[3]},
				[]*float64{nil, nil},
			}

			ops[monkey] = op
			deps[op.monkeys[0]] = monkey
			deps[op.monkeys[1]] = monkey
		}
	}

	return ops, deps, values
}

func part1() {
	ops, deps, values := parseInput()

	queue := c.NewQueue(values...)
	for queue.Length() > 0 {
		monkey := queue.Pop()
		op := ops[deps[monkey.name]]

		if op.set(monkey.name, monkey.value) {
			value := eval(*op.values[0], *op.values[1], op.operator)
			if op.name == "root" {
				u.Out(value)
				break
			}
			queue.Add(Monkey{op.name, value})
		}
	}
}

func part2() {
	ops, deps, initialValues := parseInput()

	valueQueue := c.NewQueue(initialValues...)
	for valueQueue.Length() > 0 {
		monkey := valueQueue.Pop()
		op := ops[deps[monkey.name]]

		if monkey.name == "humn" {
			continue
		}

		if op.set(monkey.name, monkey.value) {
			value := eval(*op.values[0], *op.values[1], op.operator)
			valueQueue.Add(Monkey{op.name, value})
		}
	}

	var root float64
	if ops["root"].values[0] == nil {
		root = *ops["root"].values[1]
	} else {
		root = *ops["root"].values[0]
	}

	offset := 10000000
	lower := -1
	upper := -1
	for n := 1; ; {
		test := float64(n)
		for name := deps["humn"]; name != "root"; name = deps[name] {
			op := ops[name]
			if op.values[0] == nil {
				test = eval(test, *op.values[1], op.operator)
			} else {
				test = eval(*op.values[0], test, op.operator)
			}
		}

		if int64(root*10) == int64(test*10) {
			u.Out(n)
			break
		}

		if lower == -1 && upper == -1 {
			if int64(root*10) > int64(test*10) {
				lower = n - offset
				upper = n
				n = lower + ((upper - lower) / 2)
			} else {
				n += offset
			}
		} else {
			if int64(root*10) > int64(test*10) {
				upper = n
			} else {
				lower = n
			}
			n = lower + ((upper - lower) / 2)
		}
	}
}
