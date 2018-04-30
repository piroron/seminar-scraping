@title[解答 3-1]

### 解答

```python
value = int(input())
print("残り所持金" + str(value) + "円。")
if value >= 120:
    print("ジュース買っちゃえ！")
if value < 120 and value >= 100:
    print("水を買う！")
if value < 100:
    print("何も買えない！")
```

+++

@title[解答 3-1 その2]

### 解答

```python
value = int(input())
print("残り所持金" + str(value) + "円。")
if value >= 120:
    print("ジュース買っちゃえ！")
elif value >= 100:
    print("水を買う！")
else:
    print("何も買えない！")
```
@[5](elif：最初の条件を満たさない場合、別の条件で検証する。120円以上じゃないけど、100円以上。)
@[7](elifを使ったので、「120円以上」じゃなく、「100円以上じゃない」、すなわち100円未満の場合。)
