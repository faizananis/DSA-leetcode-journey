class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int n = nums.size();
        vector<int> result;
        
        // Create the mask with 'maximumBit' bits set to 1
        int mask = (1 << maximumBit) - 1; 
        
        for (int x : nums) {
            result.push_back(mask ^ x);  // XOR the current number with the mask
            mask ^= x;                   // Update the mask with the cumulative XOR
        }
        
        reverse(result.begin(), result.end());  // Reverse the array to meet descending order requirement
        return result;                          // Return the final result
    }
};