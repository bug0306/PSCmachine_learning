

import matplotlib.pyplot as plt
import numpy as np
x1 = np.random.rand(30) * 10
y1 = x1 + np.random.rand(30) * 2
x2 = np.random.rand(30) * 10
y2 = -x2 + np.random.rand(30) * 5 + 10
x3 = np.random.rand(50) * 10
y3 = np.random.rand(50) * 10

plt.figure(figsize=(9, 3))

plt.subplot(1, 3, 1)
plt.scatter(x1, y1, marker='x', color='darkblue')
plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)), color='teal')

plt.title('正相关', fontproperties='SimHei')
plt.xticks([])
plt.yticks([])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.subplot(1, 3, 2)
plt.scatter(x3, y3, marker='x', color='darkblue')
plt.title('不相关', fontproperties='SimHei')
plt.xticks([])
plt.yticks([])

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.subplot(1, 3, 3)
plt.scatter(x2, y2, marker='x', color='darkblue')
plt.plot(np.unique(x2), np.poly1d(np.polyfit(x2, y2, 1))(np.unique(x2)), color='teal')

plt.title('负相关', fontproperties='SimHei')
plt.xticks([])
plt.yticks([])


ax = plt.gca()  
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.subplots_adjust(wspace=0.3)

plt.show()