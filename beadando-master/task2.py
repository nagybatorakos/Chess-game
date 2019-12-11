import matplotlib.pyplot as plt

try:
    n1 = int(input("n1 = "))
    n2 = int(input("n2 = "))
    def pascal_triangle(n1,n2):
        ls=[]
        for i in range(n1):
            if n1 < n2:
                print('The given n2 is either greater or equal to n1.')
                return
            ls.append([])
            ls[i].append(1)
            for j in range(1,i):
                ls[i].append(ls[i-1][j-1]+ls[i-1][j])
            if(n1!=0):
                ls[i].append(1)
        for i in range(n1):
            print("   "*(n1-i),end=" ",sep=" ")
            for j in range(0,i+1):
                print('{0:6}'.format(ls[i][j]),end=" ",sep=" ")
            print()
        plt.plot(ls[n2-1], 'go')

        plt.show()
    pascal_triangle(n1,n2)
except ValueError:
    print("The given input is not an integer.")
