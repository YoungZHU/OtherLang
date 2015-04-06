# -*- coding: gbk -*-
from random import randint

name = raw_input('����������������')
f = open('D:\Python27_Space\GameScore.txt')
lines = f.readlines()
f.close()

scores = {}

for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
    
score = scores.get(name)

if score is None:
    score = [0, 0, 0]

# ��Ϸ�ܴ���
game_times = int(score[0])
# ���¶ԵĴ���
min_times = int(score[1])
# �������ܴ���
total_times = int(score[2])

# ƽ���¶ԵĴ���
avg_times = 0
if game_times > 0:
    avg_times = float(total_times) / game_times

print '���Ѿ����� %d �Σ���� %d �ֲ³��𰸣�ƽ�� %.2f �ֲ³���' %(game_times, min_times, avg_times)


system_num=randint(1, 100)
print "Guess What!!"
times = 0
type_num=input()
while system_num != type_num:
    times += 1
    if system_num > type_num:
        print "%d is too small" %type_num
        type_num=input()
    else :
        print "%d is too large" %type_num
        type_num=input()
print "Bingo!!! %d is right!!" %type_num

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1

scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line

f = open('D:\Python27_Space\GameScore.txt', 'w')
f.write(result)
f.close()

