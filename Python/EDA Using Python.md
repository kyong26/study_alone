```python
import pandas as pd 
import numpy as np
import seaborn as sns
```


```python
data = pd.DataFrame([['a',1],['b',2],['c',3]], columns=['x','y'])
```

### 1. Understanding the data


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.shape
```




    (3, 2)




```python
data.describe() #numeric data only
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.5</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.5</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.columns
```




    Index(['x', 'y'], dtype='object')




```python
data.nunique()
```




    x    3
    y    3
    dtype: int64




```python
data['x'].unique()
```




    array(['a', 'b', 'c'], dtype=object)



### 2. Cleaning the data


```python
data.isnull().sum()
```




    x    0
    y    0
    dtype: int64




```python
data = data.drop(['x'], axis=1)
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### 3. Relationship analysis


```python
df = pd.DataFrame([['a',1,5,-1,'Y'],['b',2,6,2,'N'],['c',3,10,-2,'N'], ['c',3,10,-2,'N'],['c',3,9,-2,'N']], 
                   columns=['x','y','z','k','l'])
```


```python
correlation = df.corr()
```


```python
sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
```




    <AxesSubplot:>




![output_17_1](https://user-images.githubusercontent.com/52664532/168409034-3163ec85-3081-4025-ae82-6d84ef73b809.png)

    



```python
sns.pairplot(df) #산점도와 히스토그램으로 시각화
```




    <seaborn.axisgrid.PairGrid at 0x7fc361b54dc0>




![output_18_1](https://user-images.githubusercontent.com/52664532/168409058-21712195-bdc6-49ba-b2d4-a24ee754d07c.png)




```python
sns.relplot(x='y', y='z', hue='x', data=df, style='l')
```




    <seaborn.axisgrid.FacetGrid at 0x7fc361b5f3a0>



![output_19_1](https://user-images.githubusercontent.com/52664532/168409068-5bdc2e80-c23a-48c9-a5d9-d696324ddb5a.png)




```python
sns.distplot(df['y'])
```

    /Users/seomingyeong/.local/lib/python3.8/site-packages/seaborn/distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
      warnings.warn(msg, FutureWarning)





    <AxesSubplot:xlabel='y', ylabel='Density'>


![output_20_2](https://user-images.githubusercontent.com/52664532/168409075-b6473169-04cc-4465-969b-b99a0c1deb02.png)




```python
sns.displot(df['y'])
```




    <seaborn.axisgrid.FacetGrid at 0x7fc358701fd0>




![output_21_1](https://user-images.githubusercontent.com/52664532/168409076-f0faac41-e83c-4366-8bbc-7fb03e3527f5.png)



```python
sns.histplot(df['y'])
```




    <AxesSubplot:xlabel='y', ylabel='Count'>


![output_22_1](https://user-images.githubusercontent.com/52664532/168409082-d44d63f3-785a-4c4a-bffb-5b23fff9295e.png)

    



```python
sns.catplot(x='y', kind= 'box', data= df)
```




    <seaborn.axisgrid.FacetGrid at 0x7fc378c06220>



![output_23_1](https://user-images.githubusercontent.com/52664532/168409087-eb6664fe-d899-4ccf-9044-2275d12f2c53.png)


