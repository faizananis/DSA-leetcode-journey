class Solution {
public:
    bool isAnagram(string s, string t) {
        int arr[26]={0};
        for(char c:s)
        {
            arr[c-97]++;
        }
        for(char c:t)
        {
            arr[c-97]--;
            if(arr[c-97]==-1)
            {
                return false;
            }
        }
        for(int value:arr)
        {
            if(value!=0)
            {
                return false;
            }
        }
        return true;
    }
};