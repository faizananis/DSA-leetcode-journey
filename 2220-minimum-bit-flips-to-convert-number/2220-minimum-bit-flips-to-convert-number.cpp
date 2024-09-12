class Solution {
public:
    int minBitFlips(int start, int goal) {
        int x=start^goal;
        int step=0;

        while(x>0)
        {
            step=step+(x&1);
            x=x>>1;
        }
        return step;
    }
};