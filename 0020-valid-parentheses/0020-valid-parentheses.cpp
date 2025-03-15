class Solution {
public:
    bool isValid(string s) {
        int i=0;
        stack<char> str;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='('||s[i]=='{'||s[i]=='[')
            {
                str.push(s[i]);
            }
            else
            {
                if(str.empty())
                {
                    return false;
                }
                if(str.top()=='('&&s[i]==')')
                {
                    str.pop();
                }
                else if(str.top()=='{'&&s[i]=='}')
                {
                    str.pop();
                }
                else if(str.top()=='['&&s[i]==']')
                {
                    str.pop();
                }
                else
                {
                    return false;
                }
            }
        }
        if(str.empty()==0)
        {
            return false;
        }
        return true;
    }
};