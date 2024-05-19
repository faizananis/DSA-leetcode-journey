class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str;
        int i=0;
        int n=0;
        while(word1[i]!='\0'&&word2[i]!='\0')
        {
            str.push_back(word1[i]);
            str.push_back(word2[i]);
            i++;
        }
        if(word1[i]!='\0')
        {
            while(word1[i]!='\0')
            {
                str.push_back(word1[i]);
                i++;
            }
            return str;
        }
        if(word2[i]!='\0')
        {
            while(word2[i]!='\0')
            {
                str.push_back(word2[i]);
                i++;
            }
            return str;
        }
        return str;
    }
};