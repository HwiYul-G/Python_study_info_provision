import csv
import matplotlib.pyplot as plt
import numpy as np

# 큰수와 index 번호를 담은 list를 세개 반환(가장 큰거 처음 나옴)
def find_top3_largest(row):
    first_list = [] # 큰수, index 번호를 담음
    second_list = []
    thrid_list = []
    
    first_larger = 0;
    second_larger = 0;
    third_larger = 0;
    
    first_larger_idx, second_larger_idx, third_larger_idx = None, None, None
    for i in range(3,14):
        if first_larger == 0:
            first_larger = float(row[i])
            first_larger_idx = i
        else:
            if i > first_larger:
                second_larger = first_larger
                second_larger_idx = first_larger_idx
                first_larger = float(row[i])
                first_larger = i
            else:
                if i> second_larger:
                    third_larger = second_larger
                    third_larger_idx = second_larger_idx
                    second_larger = float(row[i])
                    second_larger_idx = i
                else:
                    if i > third_larger:
                        third_larger = float(row[i])
                        third_larger_idx = i
        
    first_list.append(first_larger)
    first_list.append(first_larger_idx)
    second_list.append(second_larger)
    second_list.append(second_larger_idx)
    thrid_list.append(third_larger)
    thrid_list.append(third_larger_idx)    
    
    return first_list, second_list, thrid_list


f = open(r'data_analyze\2_non_attendance_20220607161957.csv','r',encoding='cp949') # relative path, enconding = window encoding.
data = csv.reader(f, delimiter = ',' )

header = next(data)
print(header) # []은 list 타입이고 ''은 str을 의미함.

total_reason_top3 = [] # 전체 종합 이유 
men_reason_top3 = [] # 남성
women_reason_top3 = [] # 여성
for row in data:
    if(row[0] == '전체'):
        total_top1, total_top2, total_top3 = find_top3_largest(row)
        # print(total_top1, total_top2, total_top3)
        total_reason_top3.append([header[total_top1[1]] ,float(total_top1[0])])
        total_reason_top3.append([header[total_top2[1]] ,float(total_top2[0])])
        total_reason_top3.append([header[total_top3[1]] ,float(total_top3[0])])
    elif(row[1] == '남성'):
        total_top1, total_top2, total_top3 = find_top3_largest(row)
        
        men_reason_top3.append([header[total_top1[1]] ,float(total_top1[0])])
        men_reason_top3.append([header[total_top2[1]] ,float(total_top2[0])])
        men_reason_top3.append([header[total_top3[1]] ,float(total_top3[0])])
    elif(row[1] == '여성'):
        total_top1, total_top2, total_top3 = find_top3_largest(row)
        
        women_reason_top3.append([header[total_top1[1]] ,float(total_top1[0])])
        women_reason_top3.append([header[total_top2[1]] ,float(total_top2[0])])
        women_reason_top3.append([header[total_top3[1]] ,float(total_top3[0])])
        
print(total_reason_top3)
print(men_reason_top3)
print(women_reason_top3)

f.close()

# ============== Graph로 표현하기 ===================
#total_reason_top3 = [] # 전체 종합 이유 
#men_reason_top3 = [] # 남성
#women_reason_top3 = [] # 여성
# 이름 모음 [total_reason_top3[0][0], total_reason_top3[1][0], total_reason_top3[2][0]]
plt.title('평생학습 불참 요인', family = 'Malgun Gothic')
barWidth = 0.2
plt.plot(figsize=(15,10))
plt.rc('font',family = 'Malgun Gothic')

total_data = [total_reason_top3[0][1], total_reason_top3[1][1], total_reason_top3[2][1]]
women_data = [women_reason_top3[0][1], women_reason_top3[1][1], women_reason_top3[2][1]]
men_data = [men_reason_top3[0][1], men_reason_top3[1][1], men_reason_top3[2][1]]

# set position of bar on X axis
br1 = np.arange(3)
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, total_data, width = barWidth, label='전체', color='green')
plt.bar(br2, women_data, width = barWidth, label = '여성', color = 'hotpink')
plt.bar(br3, men_data, width = barWidth, label = '남성', color = 'blue')

plt.xlabel("3가지 상위 항목",fontweight = 'bold', fontsize = 15,family = 'Malgun Gothic')
plt.ylabel("퍼센트", fontweight = 'bold', fontsize = 15,family = 'Malgun Gothic')
# luck.. 3가지 상위 항목이 동일함.
plt.xticks([r + barWidth for r in range(3)], ['시간부족','코로나 영향','근처에 교육기관이 없어서'], family = 'Malgun Gothic')

plt.legend()
plt.show()