class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        
        vector<string> res(numRows);
        int n = s.size();
        int row = 0;
        int turn = -1;
        
        for (int i = 0; i < n; ++i){
            if (i % (numRows - 1) == 0){
                turn *= -1;
            }
            
            res[row].push_back(s[i]);
            row += turn;
        }
        
        string zigzag;
        for (auto& str:res){
            zigzag += str;
        }
        
        return zigzag;
    }
};