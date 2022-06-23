import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


# data에서 전체(소계), 남성, 여성 순으로 book, internet, personal, group 선호도 %를 list로 보내줌
def find_total_info(data):
    book_prefer, internet_prefer = [], []
    personal_prefer, group_perfer = [], []
    
    header2 = data.pop(0)
    for row in data:
        if(row[1] == '소계'):
            book_prefer.append(float(row[2]))
            internet_prefer.append(float(row[3]))
            personal_prefer.append(float(row[4]))
            group_perfer.append(float(row[5]))
        elif(row[1] == '남성'):
            book_prefer.append(float(row[2]))
            internet_prefer.append(float(row[3]))
            personal_prefer.append(float(row[4]))
            group_perfer.append(float(row[5]))
        elif(row[1] == '여성'):
            book_prefer.append(float(row[2]))
            internet_prefer.append(float(row[3]))
            personal_prefer.append(float(row[4]))
            group_perfer.append(float(row[5]))
        else:
            pass
    return book_prefer, internet_prefer, personal_prefer, group_perfer

# file open 및 처리
f = open(r'data_analyze\3_learning_method_20220607161659.csv')
data = csv.reader(f)
header = next(data) # csv 파일상 1번 줄 제거

data = list(data) # data의 list화

# 전체, 남성, 여성 순
data_name = ['전체','남성','여성']
book, internet, personal, group = find_total_info(data)

df = pd.DataFrame({'책': book, '인터넷':internet, '개인':personal, '그룹':group}, index=data_name)
fig, ax = plt.subplots()
plt.title('학습 방법 선호도', family = 'Malgun Gothic', fontweight = 'bold', fontsize =15)
plt.rc('font',family = 'Malgun Gothic')

#matplotlib.style.use('ggplot')
df[['책', '인터넷']].plot.bar(stacked=True, width=0.1, position=1.5, colormap="bwr", ax=ax, alpha=0.7)
df[['개인', '그룹']].plot.bar(stacked=True, width=0.1, position=-0.5, colormap="RdGy", ax=ax, alpha=0.7)

plt.ylabel("퍼센트", fontweight = 'bold', fontsize = 15,family = 'Malgun Gothic')
plt.xticks(family = 'Malgun Gothic')

plt.legend()
plt.show()