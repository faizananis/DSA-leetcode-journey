class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> result;
        int i=0;
        int j=0;
        int n=nums.size();
        //stack<int> st;
        reverse(nums.begin(),nums.end());
        // for(i=0;i<n;i++)
        // {
        //     nums.push_back(nums[i]);
        // }
        for(i=0;i<n*2;i++)
        {
            // if(st.empty())
            // {
            //     result.push_back(-1);
            //     st.push(nums[i]);
            // }
            // else
            // {
            //     if(st.top()<nums[i])
            //     {
            //         st.pop();
            //         while(st.top()<nums[i]&&!st.empty())
            //         {
            //             st.pop();
            //         }
            //         st.push(nums[i]);
            //         result.push_back(nums[i]);
            //     }
            //     else
            //     {
            //         st.push(nums[i]);
            //         result.push_back(nums[i]);
            //     }
            // }
            j=i;
            while(j>0)
            {
                if(nums[i%n]<nums[j%n])
                {
                    result.push_back(nums[j%n]);
                    break;
                }
                j--;
            }
            if(j==0)
            {
                result.push_back(-1);
            }
        }
        reverse(result.begin(),result.end());
        for(i=0;i<n;i++)
        {
            result.pop_back();
        }
        return result;
    }
};