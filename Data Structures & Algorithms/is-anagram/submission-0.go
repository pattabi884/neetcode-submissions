func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false 
	}
	count := make(map[rune]int)
	for _, char := range s {
		count[char]++
	}
	for _, char := range t {
		count[char]--
	}

	for _, c := range count {
		if c != 0 {
			return false 
		}
	}
	return true 
	

}

