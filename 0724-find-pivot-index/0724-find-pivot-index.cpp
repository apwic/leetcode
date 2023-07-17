class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> sums(n + 1);
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += nums[i];
            sums[i + 1] = sum;
        }

        for (int i = 0; i < n; i++) {
            if (sums[i] == sums[n] - sums[i + 1]) {
                return i;
            }
        }

        return -1;
    }
};