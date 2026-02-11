class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> check;
        int lim = nums.size();

        for(int n=0; n<lim; ++n) {
            if(check.find(nums[n]) != check.end()) return true;
            check.insert({nums[n], n});
        }

        return false;
    }
};