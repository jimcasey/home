package day13

import (
	u "jimcasey/aoc/utils"
	"sort"
)

func init() {
	u.Register(13, part1, part2)
}

func parse(item string) []string {
	items := []string{}
	level := 0
	for _, c := range item[1 : len(item)-1] {
		switch c {
		case '[':
			level++
		case ']':
			level--
		case ',':
			if level == 0 {
				items = append(items, "")
				continue
			}
		}
		if len(items) == 0 {
			items = append(items, string(c))
		} else {
			items[len(items)-1] += string(c)
		}
	}
	return items
}

func evaluate(leftStr string, rightStr string) int {
	left := parse(leftStr)
	right := parse(rightStr)

	for i := 0; i < u.Max(len(left), len(right)); i++ {
		if i >= len(left) {
			return 1
		}
		if i >= len(right) {
			return 2
		}

		leftItem := left[i]
		rightItem := right[i]

		leftList := leftItem[0] == '['
		rightList := rightItem[0] == '['

		if !leftList && rightList {
			leftItem = "[" + leftItem + "]"
			leftList = true
		}

		if leftList && !rightList {
			rightItem = "[" + rightItem + "]"
			rightList = true
		}

		if leftList && rightList {
			e := evaluate(leftItem, rightItem)
			if e > 0 {
				return e
			} else {
				continue
			}
		}

		leftInt := u.ToInt(leftItem)
		rightInt := u.ToInt(rightItem)

		if leftInt < rightInt {
			return 1
		}

		if leftInt > rightInt {
			return 2
		}
	}

	return 0
}

func part1() {
	lines := u.Read()

	index := 1
	sum := 0
	for i := 0; i < len(lines); i += 3 {
		if evaluate(lines[i], lines[i+1]) == 1 {
			sum += index
		}
		index++
	}
	u.Out(sum)
}

func part2() {
	packets := []string{"[[2]]", "[[6]]"}
	for _, line := range u.Read() {
		if line == "" {
			continue
		}
		packets = append(packets, line)
	}

	sort.SliceStable(packets, func(i, j int) bool {
		return evaluate(packets[i], packets[j]) == 1
	})

	index := 1
	decoderKey := 0
	for _, packet := range packets {
		if packet == "[[2]]" || packet == "[[6]]" {
			if decoderKey == 0 {
				decoderKey = index
			} else {
				decoderKey *= index
				break
			}
		}
		index++
	}
	u.Out(decoderKey)
}
