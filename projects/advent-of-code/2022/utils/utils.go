package utils

import (
	"bufio"
	"flag"
	"fmt"
	"math"
	"os"
	"strconv"
)

var registry map[int][]func()
var selectedDay *int
var selectedPart *int
var IsTest *bool

func init() {
	IsTest = flag.Bool("test", false, "Run test input")
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
	if *IsTest {
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

func ToInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func Max(x int, y int) int {
	return int(math.Max(float64(x), float64(y)))
}

func Min(x int, y int) int {
	return int(math.Min(float64(x), float64(y)))
}

func Abs(x int) int {
	return int(math.Abs(float64(x)))
}

func Copy[T any](arr []T) []T {
	tmp := make([]T, len(arr))
	copy(tmp, arr)
	return tmp
}

func Permutations(phases []int) [][]int {
	var result [][]int
	var helper func([]int, int)
	helper = func(arr []int, n int) {
		if n == 1 {
			result = append(result, Copy(arr))
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(phases, len(phases))
	return result
}
