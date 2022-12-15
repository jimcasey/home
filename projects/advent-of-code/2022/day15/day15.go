package day15

import (
	"jimcasey/aoc/utils"
	"strings"
)

func init() {
	utils.Register(15, part1, part2)
}

type Coord struct {
	x int
	y int
}

func (coord *Coord) abs() Coord {
	return Coord{utils.Abs(coord.x), utils.Abs(coord.y)}
}
func (a *Coord) add(b Coord) Coord {
	return Coord{a.x + b.x, a.y + b.y}
}
func (a *Coord) subtract(b Coord) Coord {
	return Coord{a.x - b.x, a.y - b.y}
}
func (a *Coord) distance(b Coord) int {
	offset := Coord{a.x - b.x, a.y - b.y}
	offset = offset.abs()
	return offset.x + offset.y
}
func (a *Coord) inRange(min Coord, max Coord) bool {
	return min.x <= a.x && a.x <= max.x && min.y <= a.y && a.y <= max.y
}

func parseInput() (map[Coord]int, map[Coord]struct{}) {
	sensors := make(map[Coord]int)
	beacons := make(map[Coord]struct{})
	for _, line := range utils.Read() {
		line = strings.Replace(line, "Sensor at x=", "", -1)
		line = strings.Replace(line, ": closest beacon is at x=", ",", -1)
		line = strings.Replace(line, " y=", "", -1)
		split := strings.Split(line, ",")

		sensor := Coord{utils.ToInt(split[0]), utils.ToInt(split[1])}
		beacon := Coord{utils.ToInt(split[2]), utils.ToInt(split[3])}

		sensors[sensor] = sensor.distance(beacon)
		beacons[beacon] = struct{}{}
	}

	return sensors, beacons
}

func part1() {
	sensors, beacons := parseInput()

	findY := 2000000
	empty := make(map[Coord]struct{})
	for sensor, distance := range sensors {
		if sensor.y+distance < findY || findY < sensor.y-distance {
			continue
		}
		for x := sensor.x - distance; x <= sensor.x+distance; x++ {
			coord := Coord{x, findY}
			if sensor.distance(coord) <= distance {
				_, sensorExists := sensors[coord]
				_, beaconExists := beacons[coord]
				if !sensorExists && !beaconExists {
					empty[coord] = struct{}{}
				}
			}
		}
	}

	utils.Out(len(empty)) // 5112034
}

func part2() {
	sensors, _ := parseInput()
	perimiters := []Coord{}

	offsets := []Coord{{1, 1}, {-1, 1}, {-1, -1}, {1, -1}}

	for sensor, distance := range sensors {
		min := Coord{sensor.x - distance - 1, sensor.y - distance - 1}
		max := Coord{sensor.x + distance + 1, sensor.y + distance + 1}

		start := Coord{sensor.x, min.y}
		perimiters = append(perimiters, start)
		index := 0
		for coord := start.add(offsets[index]); coord != start; coord = coord.add(offsets[index]) {
			if !coord.inRange(min, max) {
				coord = coord.subtract(offsets[index])
				index++
				continue
			}
			perimiters = append(perimiters, coord)
		}
	}

	size := 4000000

search:
	for _, coord := range perimiters {
		if !coord.inRange(Coord{0, 0}, Coord{size, size}) {
			continue
		}
		for sensor, distance := range sensors {
			if coord.distance(sensor) <= distance {
				continue search
			}
		}
		utils.Out(coord, (coord.x*4000000)+coord.y) // 13172087230812
		break search
	}
}
