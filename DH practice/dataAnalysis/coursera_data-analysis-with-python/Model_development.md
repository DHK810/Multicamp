# Model Development

- Simple Linear Regression
- Multiple Linear Regression
- Polynomial Regression



## Simple Linear Regression

- Relationship between 2 variables
- ![1566116004455](C:\Users\15Z970-GA5BK\AppData\Roaming\Typora\typora-user-images\1566116004455.png)

# Multiple Linear Regression

- ![1566116325843](C:\Users\15Z970-GA5BK\AppData\Roaming\Typora\typora-user-images\1566116325843.png)
- ![1566116464782](C:\Users\15Z970-GA5BK\AppData\Roaming\Typora\typora-user-images\1566116464782.png)



# Evaluating if model is right

### Mean_squared_error

```
from sklearn.metrics import mean_squared_error
mean_squared_error(df['price'], Y_predict_simple_fit)
```

### R-squared 

```
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)

lm.score(X, Y)
```







