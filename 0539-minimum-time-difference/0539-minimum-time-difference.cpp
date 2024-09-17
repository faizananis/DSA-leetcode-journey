class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int size=timePoints.size();
        int minimum=1450;
        vector<int> arr(size);
        vector<int> minutes(size,0);
        int i=0;
        for(string str:timePoints)
        {
            minutes[i]=60*(minutes[i]*10+(str[0]-48)*10+(str[1]-48));
            minutes[i]+=(str[3]-48)*10+str[4]-48;
            cout<<minutes[i]<<' ';
            i++;
        }
        sort(minutes.begin(),minutes.end());
        int j=0;
        for(j=size-1;j>0;j--)
        {
            minimum=min(minimum,abs(minutes[j]-minutes[j-1]));
            minimum=min(minimum,abs(minutes[j]+minutes[j-1]-1438));
        }
        minimum=min(minimum,abs(minutes[0]-minutes[size-1]));
        minimum=min(minimum,abs(minutes[0]+minutes[size-1]-1438));
        return minimum;
    }
};