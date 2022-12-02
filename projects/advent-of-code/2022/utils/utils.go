package utils

import (
	"bufio"
	"flag"
	"fmt"
	"os"
)

var isTest *bool

func InitState() {
	isTest = flag.Bool("test", false, "Run test input")
	flag.Parse()
}

func Out(a ...any) (n int, err error) {
	return fmt.Println(a...)
}

func Read(day string) []string {
	var name string
	if *isTest {
		name = "test.txt"
	} else {
		name = "input.txt"
	}

	file, _ := os.Open(day + "/" + name)
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}
