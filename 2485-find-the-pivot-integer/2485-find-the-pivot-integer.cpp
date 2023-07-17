class Solution {
public:
    int pivotInteger(int n) {
        vector<int> sums(n+1);
        int sum = 0;

        for (int i = 0; i <= n; i++){
            sum += i;
            sums[i] = sum;
        }

        for (int i = 1; i <= n; i++){
            if (sums[i] == sums[n] - sums[i-1]){
                return i;
            }
        }

        return -1;
    }
};