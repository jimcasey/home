package utils

import (
	"bufio"
	"flag"
	"fmt"
	"math"
	"os"
)

var registry map[int][]func()
var selectedDay *int
var selectedPart *int
var isTest *bool

func init() {
	isTest = flag.Bool("test", false, "Run test input")
	selectedDay = flag.Int("day", -1, "Day (defaults to latest)")
	selectedPart = flag.Int("part", -1, "Part (defaults to latest)")
	flag.Parse()
}

func Register(day int, parts ...func()) {
	if registry == nil {
		registry = make(map[int][]func())
	}
	registry[day] = parts
}

func Run() {
	if *selectedDay == -1 {
		for day := range registry {
			*selectedDay = int(math.Max(float64(*selectedDay), float64(day)))
		}
	}
	day := registry[*selectedDay]

	if *selectedPart == -1 {
		*selectedPart = len(day)
	}
	day[*selectedPart-1]()
}

func Read() []string {
	var packageName = "day" + fmt.Sprintf("%02d", *selectedDay)
	var inputName string
	if *isTest {
		inputName = "test.txt"
	} else {
		inputName = "input.txt"
	}

	file, _ := os.Open(packageName + "/" + inputName)
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func Out(a ...any) (n int, err error) {
	return fmt.Println(a...)
}

func Max(x int, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func Min(x int, y int) int {
	return int(math.Min(float64(x), float64(y)))
}
