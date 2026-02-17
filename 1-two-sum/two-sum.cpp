class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> passed;

        for(int i = 0; i < nums.size(); ++i) {
            int curr = target - nums[i];
            if(passed.contains(curr)) {
                vector<int> res = {passed[curr], i};
                return res;
            } else passed.insert({nums[i], i});
        }
        
        return {};
    }
};