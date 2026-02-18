class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> check;
        vector<vector<string>> res;

        for(int i = 0; i < strs.size(); ++i) {
            string curr = strs[i];
            sort(curr.begin(), curr.end());

            check[curr].push_back(strs[i]);
        }
        
        for(auto& pair : check) {
            res.push_back(move(pair.second));
        }
         return res;
    }
};