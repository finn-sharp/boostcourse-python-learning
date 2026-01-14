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

class chapter2:
    def __init__(self, case):
        self.hand = open('./data/mbox-short.txt')
        self.case = case

    def findall_list(self):
        """
            Description : re.findall() 활용 - 리스트 반환
            [] : 한 문자
            [0-9] : 0부터 9까지의 숫자
            [AEIOU] : 대문자 모음
            [a-zA-Z0-9] : 대소문자 알파벳과 숫자
            + : 1개 이상 반복
        """
        for line in self.hand: # line단위로 순회
            line = line.rstrip()

            if self.case == 'numbers':
                if re.findall('[0-9]+', line): 
                    print(line)
                    break
            
            if self.case == 'uppercase':
                if re.findall('[A-Z]+', line): 
                    print(line)
                    break

    def greedy_exp(self):
        """
            Description : re.findall() 활용 - 탐욕적 표현 vs 비탐욕적 표현
            .* : 0개 이상의 문자 (탐욕적)
            .*? : 0개 이상의 문자 (비탐욕적)
        """
        for line in self.hand: # line단위로 순회
            line = line.rstrip()

            if self.case == 'greedy':
                y = re.findall('^F.*:', line) 
                if len(y) > 0:
                    print(y)
                    break
            
            if self.case == 'non-greedy':
                y = re.findall('^F.*?:', line) 
                if len(y) > 0:
                    print(y)
                    break

    def extraction_skill(self):
        """
            Description : re.findall() 활용 - 추출 스킬
            () : 추출 시작과 끝 지정
        """
        for line in self.hand: # line단위로 순회
            line = line.rstrip()

            if self.case == 'extract': # extract 적용 + @의 좌우로 Greedy 적용
                y = re.findall('^From: (\S+@\S+)', line) 
                if len(y) > 0:
                    print(y)
                    break

            if self.case == 'non-extract': # extract 없이 전체 매칭 + @의 좌우로 Greedy 적용
                y = re.findall('^From: \S+@\S+', line) 
                if len(y) > 0:
                    print(y)
                    break

if __name__ == "__main__":
    chapter1_1 = Chapter1(case='find')
    chapter1_1.inner_func_search()
    
    chapter1_2 = Chapter1(case='startswith')
    chapter1_2.inner_func_search()

    chapter1_3 = Chapter1(case='.*')
    chapter1_3.whitespace_exp()

    chapter1_4 = Chapter1(case='\S+')
    chapter1_4.whitespace_exp()
    
    chapter2_1 = chapter2(case='numbers')
    chapter2_1.findall_list()

    chapter2_2 = chapter2(case='uppercase')
    chapter2_2.findall_list()

    chapter2_3 = chapter2(case='greedy')
    chapter2_3.greedy_exp() 

    chapter2_4 = chapter2(case='non-greedy')
    chapter2_4.greedy_exp()

    chapter2_5 = chapter2(case='extract')
    chapter2_5.extraction_skill()

    chapter2_6 = chapter2(case='non-extract')
    chapter2_6.extraction_skill()