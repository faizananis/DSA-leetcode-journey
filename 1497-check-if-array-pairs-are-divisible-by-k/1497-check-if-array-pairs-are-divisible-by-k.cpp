class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> freq(k,0);
        int remainder=0;
        for(int number : arr)
        {
            remainder=number%k;
            if(remainder<0)
            {
                remainder+=k;
            }
            freq[remainder]++;
        }
        if(freq[0] % 2 != 0)
        {
            return false;
        }
        for(int i=1; i<=k/2; i++)
        {
            if(freq[i] != freq[k-i])
            {
                return false;
            }
        }
        return true;
        // unordered_set<int> s;
        // int n=arr.size();
        // int size=n/2;
        // int i=0;
        // int j=0;
        // for(i=0;i<n;i++)
        // {
        //     for(j=i+1;j<n;j++)
        //     {
        //         if((arr[i]+arr[j])%k==0)
        //         {
        //             if(s.find(i)==s.end()&&s.find(j)==s.end())
        //             {
        //                 s.insert(i);
        //                 s.insert(j);
        //                 size--;
        //                 break;
        //             }
        //         }
        //     }
        // }
        // if(size==0)
        // {
        //     return true;
        // }
        // return false;
    }
};