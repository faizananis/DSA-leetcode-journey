class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<char> st;
        int size=s.size();
        for(int i=0;i<size;i++)
        {
            if(st.empty()==0)
            {
                if(st.top()=='('&&s[i]==')')
                {
                    st.pop();
                    continue;
                }
            }
            st.push(s[i]);
        }
        return st.size();
    }
};