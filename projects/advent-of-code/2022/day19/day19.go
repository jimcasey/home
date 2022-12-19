package day19

import (
	"jimcasey/aoc/utils"
	"regexp"
)

func init() {
	utils.Register(19, part1, part2)
}

type Blueprint struct {
	id       int
	ore      struct{ ore int }
	clay     struct{ ore int }
	obsidian struct{ ore, clay int }
	geode    struct{ ore, obsidian int }
}
type Robots struct{ ore, clay, obsidian, geode int }
type Resources struct{ ore, clay, obsidian, geode int }
type Max struct{ geodeCount int }

type State struct {
	minutes                                            int
	oreCount, clayCount, obsidianCount, geodeCount     int
	oreRobots, clayRobots, obsidianRobots, geodeRobots int
	max                                                *Max
}

func NewState(minutes int) State {
	return State{minutes, 0, 0, 0, 0, 0, 0, 0, 0, &Max{0}}
}

func parseInput() []Blueprint {
	var blueprints []Blueprint
	re := regexp.MustCompile(`-?\d+`)
	for _, line := range utils.Read() {
		matches := re.FindAllString(line, -1)
		blueprints = append(blueprints, Blueprint{
			utils.ToInt(matches[0]),
			struct{ ore int }{utils.ToInt(matches[1])},
			struct{ ore int }{utils.ToInt(matches[2])},
			struct{ ore, clay int }{utils.ToInt(matches[3]), utils.ToInt(matches[4])},
			struct{ ore, obsidian int }{utils.ToInt(matches[5]), utils.ToInt(matches[6])},
		})
	}
	return blueprints
}

func find(blueprint Blueprint, minutes int, robotType string, resources Resources, robots Robots, max *Max) {
	robotTypes := []string{"geode", "obsidian", "clay", "ore"}

	iterate := func() {
		resources.ore += robots.ore
		resources.clay += robots.clay
		resources.obsidian += robots.obsidian
		resources.geode += robots.geode
		max.geodeCount = utils.Max(max.geodeCount, resources.geode)
		minutes--
	}

	next := func() {
		for _, nextType := range robotTypes {
			find(blueprint, minutes, nextType, resources, robots, max)
		}
	}

	if robotType == "" {
		next()
		return
	}

	if resources.geode+robots.geode*minutes+(minutes*(minutes+1))/2 <= max.geodeCount {
		return
	}

	for minutes > 0 {
		switch robotType {
		case "ore":
			if resources.ore >= blueprint.ore.ore {
				resources.ore -= blueprint.ore.ore
				iterate()
				robots.ore += 1
				next()
				return
			}

		case "clay":
			if resources.ore >= blueprint.clay.ore {
				resources.ore -= blueprint.clay.ore
				iterate()
				robots.clay += 1
				next()
				return
			}

		case "obsidian":
			if robots.clay > 0 && resources.ore >= blueprint.obsidian.ore && resources.clay >= blueprint.obsidian.clay {
				resources.ore -= blueprint.obsidian.ore
				resources.clay -= blueprint.obsidian.clay
				iterate()
				robots.obsidian += 1
				next()
				return
			}

		case "geode":
			if robots.obsidian > 0 && resources.ore >= blueprint.geode.ore && resources.obsidian >= blueprint.geode.obsidian {
				resources.ore -= blueprint.geode.ore
				resources.obsidian -= blueprint.geode.obsidian
				iterate()
				robots.geode += 1
				next()
				return
			}
		}

		iterate()
	}
}

func part1() {
	blueprints := parseInput()

	qualityLevel := 0
	for _, blueprint := range blueprints {
		max := Max{0}
		find(blueprint, 24, "", Resources{0, 0, 0, 0}, Robots{1, 0, 0, 0}, &max)
		qualityLevel += blueprint.id * max.geodeCount
	}
	utils.Out(qualityLevel)
}

func part2() {
	blueprints := parseInput()

	multiple := 1
	for i := 0; i < 3; i++ {
		blueprint := blueprints[i]
		max := Max{0}
		find(blueprint, 32, "", Resources{0, 0, 0, 0}, Robots{1, 0, 0, 0}, &max)
		multiple *= max.geodeCount
	}
	utils.Out(multiple)
}
