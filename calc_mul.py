#!/usr/bin/python3

import re
                
def calc(A, B):
    # 型チェック（整数以外は不正）
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    # 範囲チェック（1〜999）
    if 0 < A < 1000 and 0 < B < 1000:
        ans = A*B
        return ans
    else:
        return -1

        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
