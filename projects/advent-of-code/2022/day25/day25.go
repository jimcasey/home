package day25

import (
	u "jimcasey/aoc/utils"
)

func init() {
	u.Register(25, part1)
}

func toInt(snafu string) int {
	value := 0
	place := 1
	for index := len(snafu) - 1; index >= 0; index-- {
		if place == 0 {
			place = 1
		}
		switch snafu[index] {
		case '=':
			value -= place * 2
		case '-':
			value -= place
		case '1':
			value += place
		case '2':
			value += place * 2
		}
		place *= 5
	}
	return value
}

func toSnafu(value int) string {
	snafu := ""
	for value > 0 {
		switch value % 5 {
		case 3:
			snafu = "=" + snafu
			value = (value - value%5) + 5
		case 4:
			snafu = "-" + snafu
			value = (value - value%5) + 5
		case 0:
			snafu = "0" + snafu
		case 1:
			snafu = "1" + snafu
		case 2:
			snafu = "2" + snafu
		}
		value /= 5
	}
	return snafu
}

func part1() {
	sum := 0
	for _, line := range u.Read() {
		sum += toInt(line)
	}
	u.Out(toSnafu(sum))
}
