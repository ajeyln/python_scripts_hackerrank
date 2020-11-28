''' A new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number,M and  is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters. '''

N, M = map(int,input().split())
for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))