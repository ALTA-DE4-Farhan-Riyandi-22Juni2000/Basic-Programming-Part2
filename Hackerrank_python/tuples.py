"""
Nama Soal: Tuples
Link: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    x = tuple(integer_list)
    print(hash(x))
    