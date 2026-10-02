class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        if(nums?.length==0)
        return false

        // brute force solution with 
        let duplication = new Set();
        for(const num of nums){
            if(!duplication.has(num)){
                duplication.add(num);
            }else{
                return true;
            }
        }

        return false;

    }
}
