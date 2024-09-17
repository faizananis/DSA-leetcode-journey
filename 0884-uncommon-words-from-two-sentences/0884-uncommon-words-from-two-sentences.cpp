class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        vector<string> words;
        unordered_map<string,int> map;
        string word="";
        for(char c : s1)
        {
            if(c==' ')
            {
                map[word]++;
                word="";
            }
            else
            {
                word+=c;
            }
        }
        if(!word.empty())
        {
            map[word]++;
        }
        word="";
        for(char c:s2)
        {
            if(c==' ')
            {
                if(map.find(word)==map.end())
                {
                    map[word]++;
                }
                else
                {
                    map[word]++;
                }
                word="";
            }
            else
            {
                word+=c;
            }
        }
        if(!word.empty())
        {
            if(map.find(word)==map.end())
            {
                map[word]++;
            }
        }
        unordered_map<string,int>::iterator it;
        for(it=map.begin();it!=map.end();it++)
        {
            if(it->second==1)
            {
                words.push_back(it->first);
            }
        }
        return words;

    }
};