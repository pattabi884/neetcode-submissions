func topKFrequent(nums []int, k int) []int { 
seen := make(map[int]int)
for _, num := range nums {
	seen[num]++
	}

buckets := make([][]int, len(nums)+1)
for num, freq := range seen {
    buckets[freq] = append(buckets[freq], num)
}
var res []int
for i := len(buckets) - 1; i >= 0; i--{
	for _, num := range buckets[i]{
		res = append(res, num)
	
	if len(res) == k{
		return res
	}
	}
 }
return res
}
