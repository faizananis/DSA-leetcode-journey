class Solution {
public:
    string removeStars(string s) {
        int i=0;
        string str;
        int n=s.length();
        while(i<n)
        {
            if(s[i]=='*')
            {
                //if(!str.empty())
                //{
                    str.pop_back();
                //}
            }
            else
            {
                str.push_back(s[i]);
            }
            i++;
        }
        return str;
    }
};