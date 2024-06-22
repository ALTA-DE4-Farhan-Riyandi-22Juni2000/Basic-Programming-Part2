"""
Nama Soal: Print Function
Link: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
      # Print each number with end parameter set to an empty string
      print(i, end='')