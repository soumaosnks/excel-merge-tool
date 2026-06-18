# excel-merge-tool
Pythonで作成したExcel自動統合ツール

## 使い方

### ① Excelファイルを input_excels フォルダに入れる
- このツールは、フォルダ内のすべての Excel ファイル（.xlsx）を自動で読み込みます。
- 例：  
  input_excels/  
   ├─ file1.xlsx  
   ├─ file2.xlsx  
   └─ file3.xlsx  

### ② Python環境を準備する
以下のコマンドで必要なライブラリをインストールします：
pip install -r requirements.txt

### ③ ツールを実行する
以下のコマンドで実行します：
python merge_excels.py


### ④ 出力ファイルを確認する
- 実行後、同じフォルダに **merged.xlsx** が生成されます。
- これは input_excels 内のすべての Excel を縦に結合したファイルです。

### ⑤ 注意点
- Excel の列構造（カラム名）は揃えておく必要があります。
- .xlsx 形式のみ対応しています。
