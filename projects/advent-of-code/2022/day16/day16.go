// https://github.com/vinnymaker18/adventofcode/blob/main/2022/day16/program.py

package day16

import (
	c "jimcasey/aoc/collections"
	u "jimcasey/aoc/utils"
	"math"
	"regexp"
	"strings"
)

func init() {
	u.Register(16, part1, part2)
}

type Valve struct {
	node  string
	rate  int
	edges []string
}

type StateIndex struct {
	index  int
	opened int
	time   int
}

type State struct {
	StateIndex
	released int
}

func run(totalTime int) (map[StateIndex]int, int) {
	lines := u.Read()
	re := regexp.MustCompile("Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? ([A-Z, ]+)")

	valves := []Valve{}
	indexes := make(map[string]int)
	nodes := []int{}

	count := len(lines)
	distances := make([][]int, count)
	for i := 0; i < count; i++ {
		distances[i] = make([]int, count)
		for j := 0; j < count; j++ {
			distances[i][j] = math.MaxInt32
		}
		distances[i][i] = 0
	}

	for index, line := range lines {
		matches := re.FindAllStringSubmatch(line, -1)[0]
		node := matches[1]
		valve := Valve{
			node,
			u.ToInt(matches[2]),
			strings.Split(matches[3], ", "),
		}

		valves = append(valves, valve)
		indexes[node] = index
		if node == "AA" || valve.rate > 0 {
			nodes = append(nodes, index)
		}

		distances = append(distances, make([]int, len(lines)))
	}
	for index, valve := range valves {
		for _, edge := range valve.edges {
			distances[index][indexes[edge]] = u.Min(distances[index][indexes[edge]], 1)
		}
	}

	for k := 0; k < count; k++ {
		for i := 0; i < count; i++ {
			for j := 0; j < count; j++ {
				distances[i][j] = u.Min(distances[i][j], distances[i][k]+distances[k][j])
			}
		}
	}

	queue := c.NewQueue[State]()
	releasedMap := make(map[StateIndex]int)

	add := func(index int, opened int, released int, time int) {
		stateIndex := StateIndex{index, opened, time}
		releasedMax, releasedExists := releasedMap[stateIndex]
		if !releasedExists {
			releasedMax = -1
		}
		if time >= 0 && releasedMax < released {
			releasedMap[stateIndex] = released
			queue.Add(State{stateIndex, released})
		}
	}

	var aaIndex int
	for i, index := range nodes {
		if index == indexes["AA"] {
			aaIndex = i
			break
		}
	}
	add(aaIndex, 0, 0, totalTime)

	for len(queue) > 0 {
		state := queue.Pop()
		if (state.opened&(1<<state.index)) == 0 && state.time >= 1 {
			flow := (state.time - 1) * valves[nodes[state.index]].rate
			add(state.index, state.opened|(1<<state.index), state.released+flow, state.time-1)
		}

		for index := range nodes {
			distance := distances[nodes[state.index]][nodes[index]]
			if distance <= state.time {
				add(index, state.opened, state.released, state.time-distance)
			}
		}
	}

	return releasedMap, len(nodes)
}

func part1() {
	releasedMap, _ := run(30)
	releasedMax := 0
	for _, released := range releasedMap {
		releasedMax = u.Max(releasedMax, released)
	}
	u.Out(releasedMax) // 1651, 1580
}

func part2() {
	releasedMap, count := run(26)

	table := make([]int, 1<<count)
	for stateIndex, released := range releasedMap {
		table[stateIndex.opened] = u.Max(table[stateIndex.opened], released)
	}

	releasedMax := 0
	for mask := 0; mask < (1 << count); mask++ {
		mask3 := ((1 << count) - 1) ^ mask
		releasedMax = u.Max(releasedMax, table[mask3])
		mask2 := mask
		for mask2 > 0 {
			releasedMax = u.Max(releasedMax, table[mask3]+table[mask2])
			mask2 = (mask2 - 1) & mask
		}
	}
	u.Out(releasedMax) // 1707
}
