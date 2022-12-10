package day06

import (
	"jimcasey/aoc/utils"
	"strings"
)

func init() {
	utils.Register(6, part1, part2)
}

func parseInput() map[string]string {
	objects := make(map[string]string)
	for _, line := range utils.Read() {
		split := strings.Split(line, ")")
		objects[split[1]] = split[0]
	}
	return objects
}

func part1() {
	objects := parseInput()

	orbits := 0
	for object := range objects {
		for parent, parentExists := objects[object]; parentExists; parent, parentExists = objects[parent] {
			orbits++
		}
	}

	utils.Out(orbits)
}

func part2() {
	objects := parseInput()

	findOrbits := func(object string) []string {
		orbits := []string{}
		for parent, parentExists := objects[object]; parentExists; parent, parentExists = objects[parent] {
			orbits = append(orbits, parent)
		}
		return orbits
	}

	myOrbits := findOrbits("YOU")
	santasOrbits := findOrbits("SAN")

search:
	for myIndex, myOrbit := range myOrbits {

		for santasIndex, santasOrbit := range santasOrbits {
			if myOrbit == santasOrbit {
				utils.Out(myIndex + santasIndex)
				break search
			}
		}
	}
}
