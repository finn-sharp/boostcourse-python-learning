# Regular Expression Quick Guide

# ^ : Matches the beginning of a line
# $ : Matches the end of the line
# . : Matches any character
# \s : Matches whitespace
# \S : Matches any non-whitespace character
# * : Repeats a character zero or more times
# *? : Repeats a character zero or more times (non-greedy)
# + : Repeats a character one or more times
# +? : Repeats a character one or more times (non-greedy)
# [aeiou] : Matches a single character in the listed set
# [^XYZ] : Matches a single character not in the listed set
# [a-20-9] : The set of characters can include a range
# ( : Indicates where string extraction is to start
# ) : Indicates where string extraction extraction is to end


import re
from unittest import case
# re.search()  # Search for a pattern in a string
# re.findall() # Find all occurrences of a pattern in a string

class Chapter1:
    def __init__(self, case):
        self.hand = open('./data/mbox-short.txt')
        self.case = case
    
    def inner_func_search(self):
        """
            Description : 내장 함수를 활용해서 이메일 추출
        """
        for line in self.hand: # line단위로 순회
            line = line.rstrip()
            
            if self.case == 'find':
                if line.find('From:') >=0: # includes 'From:'
                    print(line)

            if self.case == 'startswith': # starts with 'From:'
                if line.startswith('From:'): 
                    print(line)

    def re_search(self):
        """
            Description : re.search() 활용
        """
        for line in self.hand: # line단위로 순회
            line = line.rstrip()

            if self.case == 'find':
                if re.search('From:', line): # includes 'From:'
                    print(line)
            
            if self.case == 'startswith': # starts with 'From:'
                if re.search('^From:', line): 
                    print(line)

    def whitespace_exp(self):
        """
            Description : re.search() 활용 - 미세조정

            P.s : 이 실험에서 재미있는 점은 '처음[X-]'과 '끝[:]'을 정하고 그 중간에 뭐가 올지를 정하는 것이다.
        """
        for line in self.hand: # line단위로 순회
            line = line.rstrip()

            if self.case == '.*': # any character 0 or more times
                if re.search('^X-*:', line): # includes 'From:' and '@'
                    print(line)

            if self.case == '\S+': # non-whitespace character 1 or more times
                if re.search('^X-\S+:', line): # includes 'From:' and '@'
                    print(line)



if __name__ == "__main__":
    chapter1_1 = Chapter1(case='find')
    chapter1_1.inner_func_search()
    
    chapter1_2 = Chapter1(case='startswith')
    chapter1_2.inner_func_search()

    chapter1_3 = Chapter1(case='.*')
    chapter1_3.whitespace_exp()

    chapter1_4 = Chapter1(case='\S+')
    chapter1_4.whitespace_exp()
    
