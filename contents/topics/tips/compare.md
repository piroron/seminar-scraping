@title[Tips 6-1]

* 比較演算子

```python
value = int(input())
# 120と等しい
if value == 120:
    print("value is equals 120")
# 120と等しくない
if value != 120:
    print("value is not equals 120")
# 120より大きい
if value > 120:
    print("value is greater than 120")
# 120以上
if value >= 120:
    print("value is greater than or equal to 120")
# 120より小さい
if value < 120:
    print("value is less than 120")
# 120以下
if value <= 120:
    print("value is less than or equal to 120")
```

Note:
イコール二つで「同じ」  


+++

@[Tils 6-2]

* 条件を繋げる

```python
name = "John"
value = 120

if name == "John" and value > 130:
   print("and passed")

if name == "John" or value > 130:
   print("or passed")
```

Note:
and と or がある


条件分岐が分かると、できることが増える。
その分、問題の難易度も上がる。
解けなくても気にしない。