class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map = {};

        for (int i = 0; i < nums.size(); ++i) {
            int curr = target - nums[i];
            if(map.contains(curr)) {
                vector<int> res = {map[curr], i};
                return res;
            } else {
                map.insert({nums[i], i});
            }
            
        }
        
        vector<int> re = {0};
        return re;
    }
};