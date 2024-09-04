class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        vector<int> freq(101,0);
        for(int i=0;i<nums.size();i++){
            freq[nums[i]]++;
        }
        int ans=0;
        for(auto i:freq){
            if(i!=0)
            ans+=((i*(i-1)))/2;
        }
        return ans;
    }
};