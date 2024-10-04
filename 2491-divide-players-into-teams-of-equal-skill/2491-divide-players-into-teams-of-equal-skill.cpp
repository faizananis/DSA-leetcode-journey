class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        long long sum=0;
        int value=-1;
        int n=skill.size();
        sort(skill.begin(),skill.end());
        int left=0;
        int right=n-1;
        sum=0;
        while(left<right)
        {
            if(value!=-1)
            {
                if(value!=skill[left]+skill[right])
                    return -1;
            }
            value=skill[left]+skill[right];
            sum+=skill[left]*skill[right];
            left++;
            right--;
        }
        return sum;
    }
};