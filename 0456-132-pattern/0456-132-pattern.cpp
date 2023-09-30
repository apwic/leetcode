class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> s;
        int mx_j = INT_MIN;
        int n = nums.size();
        
        if (n < 3){
            return false;
        }
        
        for(int i = n - 1; i >= 0; i--){
            int cur = nums[i];
                
            if (cur < mx_j){
                return true;
            }
            
            while (!s.empty() && s.top() < cur){
                mx_j = s.top();
                s.pop();
            }
            
            s.push(cur);
        }
        
        return false;
    }
};