class Solution {
public:
    bool parseBoolExpr(string expression) {
        bool ans=false;
        stack<char> st;
        string str;
        int size=expression.size();
        bool temp=false;
        int i=0;
        for(i=0;i<size;i++)
        {
            if(expression[i]=='|'||expression[i]=='&'||expression[i]=='!')
            {
                st.push(expression[i]);
            }
            else if(expression[i]=='f'||expression[i]=='t')
            {
                str+=expression[i];
            }
        }
        while(st.empty()==0)
        {
            if(st.top()=='&')
            {
                for(i=0;i<str.size();i++)
                {
                    if(str[i]=='f')
                    {
                        break;
                    }
                }
                if(i==str.size())
                {
                    temp=true;
                }
                else
                {
                    temp=false;
                }
            }
            else if(st.top()=='|')
            {
                for(i=0;i<str.size();i++)
                {
                    if(str[i]=='t')
                    {
                        break;
                    }
                }
                if(i==str.size())
                {
                    temp=false;
                }
                else
                {
                    temp=true;
                }
            }
            else
            {
                if(ans==true)
                {
                    ans=false;
                }
                else
                {
                    ans=true;
                }
            }
            if(st.top()=='&'||st.top()=='|')
            {
                ans=temp;
            }
            st.pop();
        }
        return ans;
    }
};