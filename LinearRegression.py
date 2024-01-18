import matplotlib.pyplot as plt

class LinearRegressionModel():
    def __init__(self):
        self.m=0
        self.b=0
        self.y=[]
    def fit(self,x_list,y_list):
        num=0
        den=0
        x_bar=0
        y_bar=0
        for xi in x_list:
            x_bar +=xi
        for yi in y_list:
            y_bar +=yi
        x_bar = x_bar/len(x_list)
        y_bar = y_bar/len(y_list)
        for xi in x_list:
            for yi in y_list:
                num+=(xi-x_bar)*(yi-y_bar)
        for xi in x_list:
                den+=(xi-x_bar)**2
        self.m = num/den
        self.b = y_bar - self.m*x_bar

        print(self.m)
        print(self.b)

    def predict(self,x_list):
        for xi in x_list:
            self.y.append(self.m*xi+self.b)
        return self.y


x_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y_list=[100,12,13,45,67,89,190,1,45,5,67,88,24,45,56,66,79,70,120,34]
lr=LinearRegression()
lr.fit(x_list,y_list)
y=lr.predict(x_list)
plt.plot(x_list,y_list)
plt.plot(x_list,y)
plt.show()
