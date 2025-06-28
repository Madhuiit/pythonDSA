# dint get the  intuation behind this approach

def lengethOfLongestString(s):
    char_map = {}
    max_len = {}
    max_len = 0
    start = 0 
    for end , char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char]+1
        else:
            max_len = max(max_len ,end-start+1)
        char_map[char] = end
    return max_len
s = "abcabcbb"
print(lengethOfLongestString(s))
