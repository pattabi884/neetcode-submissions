class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
    
        let max = -Infinity
        let res = []
        for (let start = 0; start <= nums.length - k; start++) {
        let max = -Infinity;

        for (let i = start; i < start + k; i++) {
            if(nums[i] > max){
                max = nums[i]
            }
            
        // update max
        }
    res.push(max)
    // push max
}
return res

    }
}