# import matplotlib.pyplot as plt
# fruits= ["apple","banana","cherry","orange"]
# counts=[4,7,6,9]
# figure,axes=plt.subplots(1,2)
# axes[0].plot([5,0],[0,5])
# axes[1].plot([0,5],[0,5])
# plt.show()
import matplotlib.pyplot as plt
subjects=["math","scient","english"]
counts=[70,90,40]
figure,axes=plt.subplots(3,1)
axes[0].plot([10,0],[0,7])
axes[1].bar(subjects,counts)
axes[2].plot([])
plt.show()