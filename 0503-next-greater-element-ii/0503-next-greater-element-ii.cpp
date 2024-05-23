class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int i=0;
        int n=nums.size();
        vector<int> result(n,-1);
        stack<int> st;
        for(i=n*2-1;i>=0;i--)
        {
            while(!st.empty()&&st.top()<=nums[i%n])
            {
                st.pop();
            }
            if(i<n)
            {
                if(!st.empty())
                {
                    result[i]=st.top();
                }
            }
            st.push(nums[i%n]);
        }
        return result;
    }
};