# Oct 23, 2024
# Solution accepted!
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    #def longestCommonPrefix(strs: list[str]) -> str:
        #print("IN FUNCTION")
        # guardian (no guardian for now)

        # function to use later
        def check_values(s: str, l: list[str]):
            #print("IN VALUES FUNCTION")
            match = True
            for val in l:
                if not val.startswith(s):
                    match = False

                if match == False:
                    break

            return match

        # catch trivial cases
        if len(strs) == 1:
            return strs[0]

        # initialize varaibles
        return_string = ""
        check_val = ""
        local_bool = False
        # for i, val in enumerate(strs):
        for i in range(200):
            if i + 1 < len(strs[0]) + 1:
                check_val = strs[0][:i+1]

            local_bool = check_values(check_val, strs)
            if local_bool == True:
                return_string = check_val
            else:
                break

        #print("return_string: ", return_string)
        return return_string


# 03.28.2025
# Solution accepted!
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_word = sorted(strs, key=len)[0]
        idx = len(smallest_word)
        while idx > 0:
            if all(val.startswith(smallest_word[:idx]) for val in strs):
                break
            else:
                idx -= 1
        
        return smallest_word[:idx]
        
