class Solution {

private:
    std::vector<std::string> output; 

public:
    string getHappyString(int n, int k) {
        happyString(0, n, "");
        if (output.size() < k) return ""; 
        return output[k-1];
    }  

    void happyString(int i, int n, std::string current)
    {
        if ( i >= n )
        {
            output.push_back(current);
            return;    
        }
        if (current.empty() || current.back() != 'a')
        {
            current.push_back('a');
            happyString(i+ 1, n, current);  
            current.pop_back();
        }
         
        if (current.empty() || current.back() != 'b')
        {
            current.push_back('b');
            happyString(i+  1, n, current);  
            current.pop_back();
        }

        if (current.empty() || current.back() != 'c')
        {
            current.push_back('c');
            happyString(i + 1 , n, current);
            current.pop_back();
        }

    }
};
