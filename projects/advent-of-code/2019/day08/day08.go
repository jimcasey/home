package day08

import (
	"fmt"
	"jimcasey/aoc/utils"
	"math"
)

func init() {
	utils.Register(8, part1, part2)
}

func parseLayers() [][][]rune {
	input := utils.Read()[0]
	layers := [][][]rune{}

	width := 25
	height := 6
	area := width * height

	for index := 0; index < len(input); index += area {
		pixelIndex := index
		layer := [][]rune{}
		for y := 0; y < height; y++ {
			row := []rune{}
			for x := 0; x < width; x++ {
				row = append(row, rune(input[pixelIndex]))
				pixelIndex++
			}
			layer = append(layer, row)
		}
		layers = append(layers, layer)
	}

	return layers
}

func part1() {
	layers := parseLayers()

	countPixels := func(layer [][]rune, pixel rune) int {
		count := 0
		for _, row := range layer {
			for _, p := range row {
				if p == pixel {
					count++
				}
			}
		}
		return count
	}

	var minIndex int
	minZeros := math.MaxInt
	for index, layer := range layers {
		zeros := countPixels(layer, '0')
		if zeros < minZeros {
			minZeros = zeros
			minIndex = index
		}
	}

	utils.Out(countPixels(layers[minIndex], '1') * countPixels(layers[minIndex], '2'))
}

func part2() {
	layers := parseLayers()

	var output [][]rune
	for index, layer := range layers {
		if index == 0 {
			output = make([][]rune, len(layer))
			for y, row := range layer {
				output[y] = make([]rune, len(row))
				copy(output[y], row)
			}
			continue
		}

		for y, row := range layer {
			for x, pixel := range row {
				if pixel != '2' && output[y][x] == '2' {
					output[y][x] = pixel
				}
			}
		}
	}

	for _, row := range output {
		for _, pixel := range row {
			if pixel == '1' {
				fmt.Print("#")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}
