class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str;
        int i=0;
        while(word1[i]!='\0'||word2[i]!='\0')
        {
            if(word1[i]!='\0')
            {
                str.push_back(word1[i]);
            }
            if(word2[i]!='\0')
            {
                str.push_back(word2[i]);
            }
            i++;
        }
        return str;
    }
};