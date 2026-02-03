import matplotlib.pyplot as plt
import numpy as np
"""x=np.arange(0,5)
y=x**2
y1=[4,8,16,32,64]
y2=[20,30,40,50,60]
y3=[2,3,4,5,6]
plt.suptitle("Mata")

plt.subplot(1,2,1)
plt.plot(x,y)
plt.grid(True,which='major',linestyle='-',linewidth='0.5',color='k')
f1={'family':'Arial','size':20,'color':'darkred','fontweight':'bold'}
f2={'family':'serif','size':12,'color':'blue','fontweight':'bold'}
plt.xlabel('x-axis',fontdict=f2)
plt.ylabel('y-axis',fontdict=f2)
plt.title('1_plot',fontdict=f1)

plt.subplot(1,2,2)
plt.plot(x,y1)
plt.grid(True,which='major',linestyle='-',linewidth='0.5',color='k')
f1={'family':'Arial','size':20,'color':'darkred','fontweight':'bold'}
f2={'family':'serif','size':12,'color':'blue','fontweight':'bold'}
plt.xlabel('x-axis',fontdict=f2)
plt.ylabel('y-axis',fontdict=f2)
plt.title('2_plot',fontdict=f1)

plt.subplot(2,2,3)
plt.plot(x,y2)
plt.grid(True,which='major',linestyle='-',linewidth='0.5',color='k')
f1={'family':'Arial','size':20,'color':'darkred','fontweight':'bold'}
f2={'family':'serif','size':12,'color':'blue','fontweight':'bold'}
plt.xlabel('x-axis',fontdict=f2)
plt.ylabel('y-axis',fontdict=f2)
plt.title('3_plot',fontdict=f1)


plt.subplot(2,2,4)
plt.plot(x,y2,marker='s',mfc='w',mec='r',mew=2,ms=8,ls='dotted',lw="2",c='g')


plt.grid(True,which='major',linestyle='-',linewidth='0.5',color='k')
f1={'family':'Arial','size':20,'color':'darkred','fontweight':'bold'}
f2={'family':'serif','size':12,'color':'blue','fontweight':'bold'}
plt.xlabel('x-axis',fontdict=f2)
plt.ylabel('y-axis',fontdict=f2)
plt.title('Line_Graph',fontdict=f1)
plt.show()"""
"""x=np.arange(0,5)
y=x**2
y1=[4,8,16,32,64]
y2=[20,30,40,50,60]
y3=[2,3,4,5,6]


plt.suptitle("Mata")

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title('one')


plt.subplot(2,2,2)
plt.plot(x,y1)
plt.title('Two')



plt.subplot(2,2,3)
plt.plot(x,y)
plt.title('three')



plt.subplot(2,2,4)
plt.plot(x,y)
plt.title('four')


plt.show()
"""
x=np.arange(0,5)
y=x**2
y1=x**3
plt.title("plot")
plt.plot(x,y,label="squers",marker='o')
plt.plot(x,y1,label="cubes",marker='o')
plt.legend(loc="best",framealpha=1,facecolor="yellow",fancybox=True,shadow=True,edgecolor="red")
plt.grid(True,which='major',linestyle='-',linewidth='0.5',color='k')
plt.show()







