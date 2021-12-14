import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Happiness/2021-2/test212021/2021-2-prac/boxoffice.csv')
print(df.shape)

df.info() # 총 데이터 건수와 타입, null 건수
df.describe()

df.drop(["대표국적"], axis = 1, inplace=True)

df.loc[df["개봉일"]<20210401, "영화명"] #4월 1일 이전에 개봉한 영화, 2021년 1분기 개봉.

df.groupby("국적")["매출액"].mean()

ax = plt.gca()

df.groupby('국적')['영화명'].nunique().plot(kind='bar')
plt.show()
