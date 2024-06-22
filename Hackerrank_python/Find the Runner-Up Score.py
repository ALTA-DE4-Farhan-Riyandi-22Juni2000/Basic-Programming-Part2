"""
Nama Soal: Find the Runner-Up Score!
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])