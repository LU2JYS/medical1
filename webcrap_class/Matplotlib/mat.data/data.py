import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 표시 해결
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows 사용자
matplotlib.rcParams['font.size'] = '10' # 글자크기

x=[1,2,3]
y=[2,4,8]

plt.plot(x,y,linewidth=3,color='blue', label='국어',marker='o',
        markeredgecolor='blue',markerfacecolor='red',ms=15,alpha=0.5,ls=':')
#-------------------------------------------------------------------------------------
#상단 제목넣기
plt.title('막대그래프')

#마이너스 표시 해결
matplotlib.rcParams['axes.unicode_minus']=False 

# x,y축에 있는 설명, 위치 , 색깔
plt.xlabel('국어',loc='right',color='blue') #왼쪽,가운데,오른쪽
plt.ylabel('이름',loc='top',color='red') #top,center,bottom

# 그래프 선의 의미를 알려준다
plt.plot(x,y,label='국어점수')
plt.legend(loc=1,ncol=3) #오른쪽 상단위치(번호로 위치값저장),3가지로 세로로 나워짐

markersize -> ms 마커크기
markedgecolor -> mec 마커 테두리 색상
markerfacecolor -> mfc 마커 색상
linestyle -> ls 선 스타일
alpha 투명도
>> marker='o' 마커 종류가 다양하다(인터넷 참조)

# y축의 범위를 설정 가능
plt.yticks([5,7,8,9,11,13,15])
plt.yticks([x for x in range(0,11)]) # for문 이용해서 0~10까지
# x축의 범위를 설정 가능
plt.xticks([1,2,3])          

#파일 저장, dpi는 사이즈 크기 조절
plt.savefig('g.png',dpi=400)
plt.figure(dpi=200) 

#원형 그래프
values=[30,25,20,13,10,2] #100
# values=[60,150,1,15,13,0] #100% 꼭 맞춰들어가지않아도됨..
title=['python','Java','javascript','C#','C','ETC']
explode=[0.15,0,0.15,0,0,0] #사이간격 중요도 표시

# 시작위치 startangle=90
# 시계방향 정렬 counterclock=False
# 데이터 표시 autopct='%.1f%%'
# 데이터 쪼개서 보여주기 explode=explode
plt.pie(values,labels=title,autopct='%.1f%%',explode=explode,
        startangle=90,counterclock=False) 
plt.show()

#가운데 뚫리게하고 사이간격 넓히기
wedgeprops={'width':0.6 ,'edgecolor':'w','linewidth':2}
(wedgeprops=wedgeprops)

# values : 값
# labels : 표시(글자)
# autopct : 파이내 글자표시 및 퍼센트 표시
# startangle : 원형이 시작하는 위치
# counterclock : 그래프 내 데이터 배치 -시계방향
# wedgeprops : 도넛형태,그래프 테두리색상

plt.grid(axis='y',alpha=0.7,linestyle='--',linewidth=2) #그래프에 밑줄이 그어진다

#위에 점수표시 방법
for i,txt in enumerate(y): 
        plt.text(x[i],y[i]+0.1,txt,ha='center',color='blue')
