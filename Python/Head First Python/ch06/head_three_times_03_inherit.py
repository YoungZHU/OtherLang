# -*- coding: gbk -*-
def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return(time_str)
    
    (mins, secs) = time_str.split(splitter)
    return(mins + '.' + secs)
"""
�����������һЩ�Ĵ������ϵ�������
�ø÷���ֱ�ӷ���һ�� �ֵ�
"""
def get_coach_data(filename):
    
    try:
        with open(filename) as f:
            data = f.readline()

        data_list = data.strip().split(',')
        
        name = data_list.pop(0)
        dob = data_list.pop(0)
        times = data_list

        return(Athlete(name, dob, times))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

"""
������ class , �̳� list
"""
class Athlete(list):
    def __init__(self, name, dob, times):
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        print(self.name + "'s fastest times are: " 
		+ str(sorted(set([sanitize(t) for t in self]))[0:3]))

        
sarah = get_coach_data('sarah2.txt')
#print(sarah)
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
james = get_coach_data('james2.txt')

sarah.top3()

julie.top3()
mikey.top3()
james.top3()
