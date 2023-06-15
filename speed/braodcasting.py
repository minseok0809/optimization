import numpy as np

test1 = np.random.randint(0, 10, 100)
test2 = np.random.randint(0, 10, 100)
result = np.empty((100, 100))

#braodcasting
result = test1.reshape(100, 1) + test2.reshape(1, 100)

#for-loop
for i in range(100):
	for j in range(100):
    		result[i,j] = test1[i] + test2[j]

# Reference
# 파이썬 속도를 빠르게 numpy 브로드캐스트를 사용하기 (Tistory Blog 팁뚠이의 신비한 팁사전)
# https://newly0513.tistory.com/183