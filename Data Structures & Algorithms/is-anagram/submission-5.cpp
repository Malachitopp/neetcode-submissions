class Solution {
public:
    bool isAnagram(string s, string t) {
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
            
            if (!wordMap.contains(ch) || wordMap[ch] == 0)
                {
                    return false;
                }
            wordMap[ch]--;

        }
        return true;
       


    }
};
