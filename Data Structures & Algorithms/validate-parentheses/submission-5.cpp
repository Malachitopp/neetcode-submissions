class Solution {
public:
    bool isValid(string s) {
        std::vector<char> stack;
        std::unordered_map<char, char> closed = {
            {']', '['},
            {')', '('},
            {'}', '{'}
        };

        for (char ch : s)
        {
            if (closed.contains(ch))
            {
                if (!stack.empty() && stack.back() == closed[ch])
                {
                    stack.pop_back();

                }
                else{
                    return false;
                }

            }
            else{
                stack.push_back(ch);
            }
        }
        return stack.empty();
    }
};
