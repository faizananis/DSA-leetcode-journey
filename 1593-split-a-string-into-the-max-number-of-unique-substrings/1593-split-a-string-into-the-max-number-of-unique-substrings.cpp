class Solution {
public:
    int maxUniqueSplit(string s) 
    {
        unordered_set<string> u_set;
        return recurse(0, s, u_set);
    }
private:
    int recurse(int start, const string& s, unordered_set<string>& u_set) {
        if (start == s.size()) {
            return 0;
        }
        int maxCount = 0;
        for (int end = start + 1; end <= s.size(); ++end) 
        {
            string substring = s.substr(start, end - start);
            if (u_set.find(substring) == u_set.end()) 
            {
                u_set.insert(substring);
                maxCount = max(maxCount, 1 + recurse(end, s, u_set));
                u_set.erase(substring);
            }
        }
        return maxCount;
    }
};