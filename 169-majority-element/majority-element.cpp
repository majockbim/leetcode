class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count;

        for(int i = 0; i < nums.size(); ++i) {
            count[nums[i]]++;
        }

        int max = 0;
        int res = 0;
        for(auto &pair : count) {
            if(pair.second > max) {
                max = pair.second;
                res = pair.first;
            }
        }
        return res;
    }
};