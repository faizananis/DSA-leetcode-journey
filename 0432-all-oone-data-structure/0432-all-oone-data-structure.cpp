class AllOne {
public:
    unordered_map<string,int> umap;
    set<pair<int,string>> s;
    AllOne() {
        umap.clear();
    }
    void inc(string key) {
        int n=0;
        if(umap.find(key)!=umap.end())
        {
            n=umap[key]++;
            s.erase({n,key});
        }
        else
        {
            umap[key]=1;
        }
        s.insert({n+1, key});
    }
    void dec(string key) {
        int n=umap[key]--;
        s.erase({n,key});
        if(umap[key]==0)
        {
            umap.erase(key);
        }
        else
        {
            s.insert({n-1,key});
        }
    }
    string getMaxKey() {
        if(s.empty())
        {
            return "";
        }
        return s.rbegin()->second;
    }
    string getMinKey() {
        if(s.empty())
        {
            return "";
        }
        return s.begin()->second;
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */