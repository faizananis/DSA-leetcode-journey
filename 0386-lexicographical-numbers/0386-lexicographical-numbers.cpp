class Solution {
public:
    int getNextVal(int val, int n)
    {
        if(val*10<=n)
        {
            return val*10;
        }
        if(val>=n)
        {
            val/=10;
        }
        val+=1;
        while(val%10==0)
        {
            val/=10;
        }
        return val;
    }
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int i=0;
        int val=1;
        for(i=0;i<n;i++)
        {
            ans.push_back(val);
            val=getNextVal(val,n);
        }
        return ans;
    }
};