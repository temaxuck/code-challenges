package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const divisor = 2023

func printSequence(sequence []int) {
	for _, value := range sequence {
		fmt.Print(value, " ")
	}
	fmt.Println("")

}

func solution(n int, k int, b []int) []int {
	bProduct := 1 
	missingValues := make([]int, 0)
	
	for _, value := range b {
		bProduct *= value
	}

	if divisor % bProduct != 0  {
		return nil
	}

	if divisor == bProduct {
		for i := 0; i < k; i++ {
			missingValues = append(missingValues, 1)
		}
		return missingValues
	} else {
		missingValues = append(missingValues, divisor / bProduct)
		for i := 0; i < k - 1; i++ {
			missingValues = append(missingValues, 1)
		}
		return missingValues
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var t, n, k int

	fmt.Scanln(&t) // number of tests 

	for i := 0; i < t; i++ {
		fmt.Scanln(&n, &k) // size of the sequence, number of missing items
		
		b := make([]int, 0)

		scanner.Scan()
		input := scanner.Text()
	
		strValues := strings.Fields(input)
	
		for _, strValue := range strValues {
			val, _ := strconv.Atoi(strValue)
			b = append(b, val)
		}

		result := solution(n, k, b)
		
		if result == nil {
			fmt.Println("NO")
		} else {
			fmt.Println("YES")
			printSequence(result)
		}

		b = nil
	}

}