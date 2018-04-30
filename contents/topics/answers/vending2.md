@title[解答 3-2]

### 解答

こういう問題になると、書き方はいろいろある。

さっきの解答

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

+++

@title[解答 3-2 例1]

### その１ 素直に解く

```python
value = int(input())
print("残り所持金" + str(value) + "円。")
if value >= 120:
    print("ジュース買っちゃえ！")
    value = value - 120
    print("残り所持金" + str(value) + "円。")
    if value == 0:
        print("お金がない！")
elif value >= 100:
    print("水を買う！")
    value = value - 100
    print("残り所持金" + str(value) + "円。")
    if value == 0:
        print("お金がない！")
else:
    print("何も買えない！")
```
@[5-8](購入したので、残金の計算)
@[11-14](ここでも購入したので、残金の計算)

+++

@title[解答 3-2 例2]

### その２　支払金額を持つ

```python
value = int(input())
pay_amount = 0
print("残り所持金" + str(value) + "円。")
if value >= 120:
    print("ジュース買っちゃえ！")
    pay_amount = 120
elif value >= 100:
    print("水を買う！")
    pay_amount = 100
else:
    print("何も買えない！")
if pay_amount != 0:
    rest = value - pay_amount
    print("残り所持金" + str(rest) + "円。")
    if rest == 0:
        print("お金がない！")
```
@[2](「支払額」を表す変数を用意)
@[6, 9](支払が発生したら、値をセット)
@[12](支払が起こったかチェックする)
@[13-16](支払が起こった場合、残金と0円の場合の表示)