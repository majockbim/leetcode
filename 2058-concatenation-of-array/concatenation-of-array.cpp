class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();

        vector<int> res;

        // prevent reallocation of memory
        res.reserve(2*n);

        for(int i=0; i<2*n; ++i) {
            res.push_back(nums[i % n]);
        }

        return res;

    }
};