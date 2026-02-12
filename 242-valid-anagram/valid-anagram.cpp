class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(t.begin(), t.end()); // <algorithm>
        sort(s.begin(), s.end());
        if(s == t) return true;
        return false;
    }
};