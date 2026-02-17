class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";

        for(int i = 0; i < strs[0].length(); ++i) {
            for(string n : strs) {
                if(i == n.length() or n[i] != strs[0][i]) return res;
            }
            res.push_back(strs[0][i]);
        }

        return res;
    }
};