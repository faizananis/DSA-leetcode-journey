class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        map<int,int> mp;
        int n=arr.size();
        int rank=1;
        vector<int> vect(n,0);
        for(int i=0;i<n;i++)
        {
            mp[arr[i]]=0;
        }
        int sizeUnique=mp.size();
        map<int,int>::iterator it;
        for(it=mp.begin();it!=mp.end();it++)
        {
            it->second=rank;
            rank++;
        }
        for(int i=0;i<n;i++)
        {
            it=mp.find(arr[i]);
            vect[i]=it->second;
        }
        return vect;
    }
};