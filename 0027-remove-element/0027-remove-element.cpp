class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int out;
        int size = nums.size();
        for (int i = 0; i<size; i++){
            if (nums[i] == val){
                nums.erase(nums.begin() + i);
                i--;
                size--;
            } else {
                out++;
            }

            for (int j=0; j<nums.size();j++){
                cout << nums[j] << ' ';
            }
            cout << endl;
        }
        return out;
    }
};