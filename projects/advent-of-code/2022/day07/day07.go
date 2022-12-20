package day07

import (
	u "jimcasey/aoc/utils"
	"math"
	"strconv"
	"strings"
)

func init() {
	u.Register(7, part1, part2)
}

func getParent(path string) string {
	dirs := strings.Split(path, "/")
	return strings.Join(dirs[:len(dirs)-1], "/")
}

func parseInput() map[string]int {
	sizeMap := make(map[string]int)
	var path string
	for _, line := range u.Read() {
		if line == "$ ls" || strings.HasPrefix(line, "dir ") {
			continue
		}

		if strings.HasPrefix(line, "$ cd") {
			dir := line[5:]

			switch dir {
			case "/":
				path = "~"
			case "..":
				path = getParent(path)
			default:
				path = path + "/" + dir
			}
			continue
		}

		fileSize, _ := strconv.Atoi(strings.Split(line, " ")[0])
		for p := path; p != ""; p = getParent(p) {
			sizeMap[p] += fileSize
		}
	}
	return sizeMap
}

func part1() {
	sizeMap := parseInput()

	cullSize := 0
	for _, size := range sizeMap {
		if size <= 100000 {
			cullSize += size
		}
	}
	u.Out(cullSize)
}

func part2() {
	sizeMap := parseInput()

	freeSpace := 70000000 - sizeMap["~"]
	requiredSpace := 30000000 - freeSpace
	cullSpace := math.MaxInt
	for _, size := range sizeMap {
		if size >= requiredSpace {
			cullSpace = int(math.Min(float64(cullSpace), float64(size)))
		}
	}
	u.Out(cullSpace)
}
