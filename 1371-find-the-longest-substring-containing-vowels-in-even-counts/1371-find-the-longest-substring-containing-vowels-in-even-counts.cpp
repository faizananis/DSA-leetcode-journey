class Solution {
public:
    int findTheLongestSubstring(string s) {
        vector<int> arr(32, -2);
        arr[0] = -1;

        int maxlength = 0;
        int mask = 0;
        int back=0;
        char c=0;
        int i=0;

        for (i = 0; i < s.size(); ++i) {
            c = s[i];

            switch (c) {
                case 'a':
                    mask ^= 1;
                    break;
                case 'e':
                    mask ^= 2;
                    break;
                case 'i':
                    mask ^= 4;
                    break;
                case 'o':
                    mask ^= 8;
                    break;
                case 'u':
                    mask ^= 16;
                    break;
            }

            back = arr[mask];
            if (back == -2) {
                arr[mask] = i;
            } else {
                maxlength = max(maxlength, i - back);
            }
        }
        return maxlength;
    }
};

// class Solution {
// public:
//     int findTheLongestSubstring(string s) {
//         unordered_map<char,bool> umap;
//         umap['a']=1;
//         umap['e']=2;
//         umap['i']=4;
//         umap['o']=8;
//         umap['u']=16;
//         int mask=0;
//         int maxlength=0;
//         int seen[32]={0};
//         int i=0;
//         for(i=0;i<s.size();i++)
//         {
//             mask=mask^umap[s[i]-'a'];
//             if(mask!=0&&seen[mask]==-1)
//             {
//                 seen[mask]=i;
//             }
//             maxlength=max(maxlength,i-seen[mask]);
//         }
//         return maxlength;
//     }
// };