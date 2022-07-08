
import os
import sys
import csv


lines = []
with open('../extra_feature/pre_procesado/labels.csv') as f :
    csv_reader = csv.reader(f)
    lines = [x for x in csv_reader if x!=[]]


# lines=list(dict.fromkeys(ids))
# lines=[x for x in lines ]
print(lines[1])


with open('../extra_feature/pre_procesado/processed_label_1.txt', 'w') as f:
    
    with open('../extra_feature/pre_procesado/processed_ids.txt', 'w') as f2:
    
        for line in lines:
            if line[1] == 'ang':
                f.write('0\n')
                f2.write(line[0]+'\n')
            elif line[1] == 'hap':
                f.write('1\n')
                f2.write(line[0]+'\n')
            elif line[1] == 'exc':
                f.write('1\n')
                f2.write(line[0]+'\n')
            elif line[1] == 'sad':
                f.write('2\n')
                f2.write(line[0]+'\n')
            elif line[1] == 'neu':
                f.write('3\n')
                f2.write(line[0]+'\n')
            else :
                f.write('-1\n')

lines = []
with open('../extra_feature/pre_procesado/processed_label_1.txt') as f :
    lines = f.readlines()
lines = [x.strip() for x in lines]

print(len([x for x in lines if x=='0']))
print(len([x for x in lines if x=='1']))
print(len([x for x in lines if x=='2']))
print(len([x for x in lines if x=='3']))