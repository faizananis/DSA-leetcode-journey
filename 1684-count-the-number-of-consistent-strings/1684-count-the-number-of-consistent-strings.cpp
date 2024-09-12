class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int arr[26]={0};
        int n=allowed.size();
        int count=0;
        int i=0;
        int j=0;
        for(i=0;i<n;i++)
        {
            arr[allowed[i]-97]=1;
        }
        for(i=0;i<words.size();i++)
        {
            for(j=0;j<words[i].size();j++)
            {
                if(arr[words[i][j]-97]==0)
                {
                    break;
                }
            }
            if(j==words[i].size())
            {
                count++;
            }
        }
        return count;
    }
};