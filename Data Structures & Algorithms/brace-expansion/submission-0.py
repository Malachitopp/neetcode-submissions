class Solution:
    def expand(self, s: str) -> List[str]:
        all_options = [] 

        def store_all_options():
            pos = 0 
            while pos < len(s):
                curr_options = []
                if s[pos] != ("{"):
                    curr_options.append(s[pos]) 
                else:
                    while s[pos] != "}":
                        if "a" <= s[pos] <= "z":
                            curr_options.append(s[pos]) 
                        pos += 1 
                    curr_options.sort() 
                all_options.append(curr_options) 
                pos +=1 
            
        
        def generate_words(curr_string, expanded_words):
            if len(curr_string) == len(all_options):
                expanded_words.append("".join(curr_string)) 
                return 
            curr_options = all_options[len(curr_string)] 

            for c in curr_options:
                curr_string.append(c) 
                generate_words(curr_string, expanded_words) 

                curr_string.pop() 
            
        
        store_all_options() 
        expanded_words = [] 
        generate_words([], expanded_words) 
        return expanded_words  