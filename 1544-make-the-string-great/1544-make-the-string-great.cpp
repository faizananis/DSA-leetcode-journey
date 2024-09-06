class Solution {
public:
    string makeGood(string s) {
        stack<char> st;
        string str="";
        int size=s.size();
        for(int i=0;i<size;i++)
        {
            if(st.empty()==0)
            {
                if(st.top()==s[i]+32||st.top()==s[i]-32)
                    st.pop();
                else
                {
                    st.push(s[i]);
                }
            }
            else 
            {
                st.push(s[i]);
            }
        }
        while(st.empty()==0)
        {
            str=str+st.top();
            st.pop();
        }
        reverse(str.begin(),str.end());
        return str;
    }
};