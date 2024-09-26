class MyCalendar {
public:
    vector<pair<int,int>> ranges;

    MyCalendar() {}
    
    bool book(int start, int end) 
    {
        int r_start=0;
        int r_end=0;
        for(int i=0;i<ranges.size();i++)
        {
            r_start=ranges[i].first;
            r_end=ranges[i].second;
            if(start<r_end && end>r_start)
            {
                return false;
            }
        }
        ranges.push_back(make_pair(start,end));
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */