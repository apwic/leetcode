class Solution {
public:
    string smallestSubsequence(string s) {
        vector<int> letters(26, 0);
        vector<int> occur(26, false);
        string res;
        
        for (char c:s)
        {
            // incerement each occurence
            letters[c - 'a']++;
        }
        
        for (char c:s)
        {
            // decrement
            letters[c - 'a']--;
            
            if (occur[c - 'a']){
                continue;
            }
            
            while (!res.empty() &&
                  res.back() > c &&
                  letters[res.back() - 'a'] > 0)
            {
                occur[res.back() - 'a'] = false;
                res.pop_back(); // remove from result
            }
            
            res.push_back(c);
            occur[c - 'a'] = true;
        }
        
        return res;
    }
};