class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n=digits.size()-1;
        int num=0;
        for(int i=0;i<=n;i++)
        {
            num=num*10+digits[i];
        }
        num+=1;
        digits.clear();
        for(int i=0;num!=0;i++)
        {
            digits.push_back(num%10);
            num=num/10;
        }
        reverse(digits.begin(),digits.end());
        return digits;
    }
};