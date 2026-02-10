class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> res = nums;
        for(int n : nums) {
            res.push_back(n);
        }
        return res;
    }
};