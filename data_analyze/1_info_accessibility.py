import csv
import matplotlib.pyplot as plt

def info_by_age(data):
    info_access = []
    header2 = data.pop(0)
    
    for row in data:
        if(row[1] == '20대'):
            info_access.append(float(row[2]))
        elif(row[1] == '30대'):
            info_access.append(float(row[2]))
        elif(row[1] == '40대') :
            info_access.append(float(row[2]))
        elif(row[1] == '50대'):
            info_access.append(float(row[2]))
        elif(row[1] == '60대'):
            info_access.append(float(row[2]))
        else:
            pass
    return info_access


# FILE 
f = open(r'C:\Users\Y\Desktop\my_worksapce\MyPython\data_analyze\1_info_accessibility.csv','r',encoding='cp949')
data = csv.reader(f)
header1 = next(data) # 특성별(1), 특성별(2), 2021, ...
data = list(data)

print(data)

info_access = info_by_age(data)
age = [20, 30, 40, 50, 60]



f.close()

# GRAPH

plt.scatter(age, info_access, s = [200], c=['red','blue','green','gold','magenta'])
plt.title("연령별 학습 정보 접근율",family = 'Malgun Gothic', fontweight = 'bold', fontsize = 12)
plt.rc('font', family = 'Malgun Gothic')


plt.xlabel('연령(20대-60대)',family = 'Malgun Gothic', fontweight = 'bold', fontsize = 12)
plt.ylabel('학습 정보 접근성(%)', family = 'Malgun Gothic', fontweight = 'bold', fontsize = 12)

plt.xticks(age)
plt.yticks(range(20,51,10))

plt.plot(age,range(40,19,-5), label = '예상 추세선')

plt.legend()
plt.show()