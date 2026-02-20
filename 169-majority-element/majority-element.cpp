class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int curr = 0;
        int count = 0;
        for(int n : nums) {

            if(count == 0) {
                curr = n;
            }

            if(n == curr) count++;
            else count--;
        }
        return curr;
    }
};