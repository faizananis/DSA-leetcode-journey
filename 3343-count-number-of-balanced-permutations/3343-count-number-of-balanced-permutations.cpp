class Solution {
public:
    int countBalancedPermutations(string num) {
        sort(num.begin(), num.end()); //Sorting helps next_permutation to find all permutation, so we need to start from smallest (hence sorted)
        unordered_set<string> seen;
        int count = 0;

        do {
            if (seen.count(num)) 
                continue;
            seen.insert(num);
            int evenSum = 0, oddSum = 0;
            for (int i = 0; i < num.size(); ++i) {
                int digit = num[i] - '0';
                if (i % 2 == 0) evenSum += digit;
                else oddSum += digit;
            }
            if (evenSum == oddSum) {
                count++;
            }
        } while (next_permutation(num.begin(), num.end()));

        return count;
    }
};