class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int num=0;
        long long int sum=0;
        int i=0;
        for(i=0;i<chalk.size();i++)
        {
            sum+=chalk[i];
        }
        num=k%sum;
        for(i=0;i<chalk.size();i++)
        {
            num-=chalk[i];
            if(num<0)
            {
                break;
            }
        }
        return i;
        
    }
};