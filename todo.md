# Todo

1. 各項目についての考察
  - 特に各項目を適切にグラフ化する過程でmatplotlibのノウハウを掴みたい 

2. 特に相関の強そうなデータを基に学習してみて一個解答作ってみる

3. 適当に試行錯誤する

4. 疲れたら他の人の解答見てみる

5. 面白そうなものを試す

# データ分析メモ

- 使えそうな人たち
  - OverallQual
    - YearRemodAddとの相関が強いのでYearRemodAddがあれば要らない可能性ありけり
  - OverallCond
    - Qualの方がいいかも
  - YearBuilt
  - YearRemodAdd
    - Builtよりいいかも
  - PoolQc, GarageQual, Fence
    - Exが特に強い
    - この3つはYearRemodAddとの相関も特にないので結構ユニークなのかも
