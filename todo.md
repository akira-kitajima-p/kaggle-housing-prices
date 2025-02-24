# Todo

1. 各項目についての考察
  - 特に各項目を適切にグラフ化する過程でmatplotlibのノウハウを掴みたい 

2. 特に相関の強そうなデータを基に学習してみて一個解答作ってみる

3. 適当に試行錯誤する
  - XGBoost使ってみる
  - XGBoostとのアンサンブルをやってみる

4. 疲れたら他の人の解答見てみる

5. 面白そうなものを試す

# データ分析メモ

- 使えそうな人たち
  - OverallQual
    - YearRemodAddとの相関が強いのでYearRemodAddがあれば要らない可能性ありけり
  - GrLivArea
    - GarageCars, GarageAreaと合わせて価格との相関係数が高い。どれか一個高ければ他も高くなる気もする。
  - TotalBsmtSF
  - YearBuilt
  - YearRemodAdd
    - Builtよりいいかも
  - PoolQc, GarageQual, Fence
    - Exが特に強い
    - この3つはYearRemodAddとの相関も特にないので結構ユニークなのかも
  - Functional
    - Type以外のデータ数が少ないが、Typの平均値が高いのは間違いない
    - Typ(問題無し)とそれ以外くらいの分け方はしたほうがよさそう
  - MSSubClass
    - 値によって価値にかなり違いがありそうなので、カテゴリカル変数にしておきたい
  - MSZoning
    - カテゴリ化はしたい
  - NeighborHood
    - 地域名、24種？くらいしかないが平均に大きな差があるので絶対にカテゴリ化すべき
  - Foundation
    - 工事方法。平均値の差が大きいのでカテゴリ化の価値はありそう
    - 建築年代別に流行がありそうな気もしたけど、グラフ化するとそんなことなかった
