class Solution {
public:
    bool isAnagram(const std::string& s, const std::string& t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::unordered_map<char, int> wordMap;

        for(char ch : s)
        {
           wordMap[ch]++;
        }
        for(char ch:t)
        {
            int& c = wordMap[ch];
            if (c == 0 ) return false;
            --c;

        }
        return true;
       


    }
};
