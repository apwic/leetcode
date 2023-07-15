class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() > haystack.size()){
            return - 1;
        }
        
        for (int i=0; i<haystack.size()-needle.size()+1; i++){
            if (haystack[i] == needle[0]){
                int j = i;
                int k = 1;
                while (haystack[j+k] == needle[k] && k < needle.size()){
                    k++;
                }

                if (k == needle.size()){
                    return i;
                }
            }
        }

        return -1;
    }
};