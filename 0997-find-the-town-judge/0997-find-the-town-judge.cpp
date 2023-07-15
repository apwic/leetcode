#include <iostream>
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        int numOfTrust[n];

        for (int i = 0; i < n; i++){
            numOfTrust[i] = 0;
        }

        for (vector<int> i : trust) {
            numOfTrust[i[0]-1]--;
            numOfTrust[i[1]-1]++;
        }
        
        for (int i = 0; i < n; i++){
            if (numOfTrust[i] == n - 1) {
                return i+1;
            }
        }

        return -1;
    }
};