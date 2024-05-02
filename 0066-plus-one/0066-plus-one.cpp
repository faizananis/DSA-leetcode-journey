class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n=digits.size()-1;
        int num=0;
        while(n>=0)
        {
            if(digits[n]!=9)
            {
                digits[n]+=1;
                return digits;
            }
            //If digit[n] = 9 then,
            digits[n]=0;
            n--;
        }
        //If all digits are 9 then,
        digits.insert(digits.begin(),1);
        return digits;
    }
};