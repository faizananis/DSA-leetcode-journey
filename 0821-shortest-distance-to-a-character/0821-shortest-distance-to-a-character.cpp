class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> res;
        int size=s.size();
        int position=size+1;
        for(int i=0;i<size;i++)
        {
            if(s[i]==c)
            {
                position=i;
            }
            res.push_back(abs(position-i));
        }
        for(int i=position;i>=0;i--)
        {
            if(s[i]==c)
            {
                position=i;
            }
            res[i]=min(abs(position-i),res[i]);
        }
        return res;
    }
};