class Solution {
public:
    int minSwaps(string s) {
        stack<char> st;
        int n=s.size();
        for(int i=0;i<n;i++)
        {
            if(!st.empty())
            {
                if(st.top()=='[')
                {
                    st.pop();
                    continue;
                }
            }
            st.push(s[i]);
        }
        return st.size()/2;
    }
};