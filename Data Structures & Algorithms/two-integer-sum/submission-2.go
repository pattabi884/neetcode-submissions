func twoSum(nums []int, target int) []int {
	hashMap := make(map[int]int)

	for i, num := range nums {
		diff := target - num

		if val, exists := hashMap[diff]; exists {
			return []int{val, i}
		}

		hashMap[num] = i
	}

	return []int{}
}