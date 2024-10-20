class Solution {
public:
    char findKthBit(int n, int k) {
        vector<char> ans;
        int i=0;
        ans.push_back('0');
        vector<char> temp;
        temp.push_back('0');
        for(i=1;i<n;i++)
        {
            for(int j=0;j<temp.size();j++)
            {
                if(temp[j]=='0')
                {
                    temp[j]='1';
                }
                else
                {
                    temp[j]='0';
                }
            }
            reverse(temp.begin(),temp.end());
            ans.push_back('1');
            ans.insert(ans.end(),temp.begin(),temp.end());
            temp.clear();
            temp=ans;
        }
        return ans[k-1];
    }
};