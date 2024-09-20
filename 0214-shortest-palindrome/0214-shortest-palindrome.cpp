class Solution {
public:
    string shortestPalindrome(string s) {
        string rev(s.rbegin(),s.rend());
        for(int i=0;i<s.size();i++)
        {
            if(s.starts_with(rev.substr(i)))
            {
                return rev.substr(0,i)+s;
            }
        }
        return s;
    }
};