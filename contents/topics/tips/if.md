@title[Tips 5]

* 条件分岐（if文）

```python
if [条件]:
    # 条件を満たしたときの処理
else:
    # 条件を満たさなかった時の処理
```

Note:
コロンの入力を忘れないこと。  
コロン入力→改行とすると、先頭に空白が4つ入るが、それはそのままにする。
+++

@title[Tips 5-2]

* 例

点数が70点以上だったら？

```python
score = int(input())
if score >= 70:
    print("合格")
else:
    print("不合格")
```
@[2](条件。「scoreが70以上」かどうか判定している。)