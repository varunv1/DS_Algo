# link to question: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13
from collections import Counter
def minSteps(s:str,t:str)-> int:
    s = s.lower()
    t = t.lower()
    s_dict = Counter(s)
    t_dict = Counter(t)
    changes = sum(s_dict.values())
    for key, value in t_dict.items():
        if s_dict.get(key, None):
            temp = s_dict.get(key)-value
            if temp >=0:
                changes -= value
            elif temp < 0:
                changes -= s_dict.get(key)



if __name__=="__main__":
    s = "anagram"
    t = "mangaar"
    print(minSteps(s,t))