class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> letters(26, 0);
        vector<int> in_res(26, false);
        string res;
        
        for (char c:s){
            letters[c - 'a']++;
        }
        
        for (char c:s){
            // decrement while moving
            letters[c -'a']--;
            
            // skip if already in res
            if (in_res[c - 'a']){
                continue;
            }
                
            while (!res.empty() &&                  // check top of the stack
                  res.back() > c &&                 // remove if smaller
                  letters[res.back() - 'a'] > 0)    // need to check the occurence
            {
                in_res[res.back() - 'a'] = false;
                res.pop_back();
            }
            
            res.push_back(c);
            in_res[c - 'a'] = true;
        }
    
        return res;
    }
};