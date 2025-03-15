// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left=1;
        int right=n;
        int mid=0;
        while(left<right)
        {
            mid=(left/2)+(right/2);
            if(isBadVersion(mid)==false)
            {
                left=mid+1;
            }
            else
            {
                right=mid;
            }
        }
        return left;
    }
};