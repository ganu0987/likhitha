import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAGG')
def bubblesort(a):
    n=len(a)
    for i in range(n-2):
        for j in range(n-2-i):
           if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
a=[34,46,43,27,57,41,45,21,70]
print("before sorting:",a)
bubblesort(a)
print("after sorting:",a)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x],label="o(n^2)")
plt.plot(x,x,label="actual time")
plt.title("bubblesort-time complexity is(n^2)")
plt.xlabel("input")
plt.ylabel("time")
plt.legend()
plt.show()
                