import pandas as pd
import glob
import os

def merge_excels(input_folder: str, output_file: str):
    # フォルダ内のExcelファイル一覧を取得
    excel_files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    if not excel_files:
        print("Excelファイルが見つかりませんでした。")
        return

    merged_df = pd.DataFrame()

    for file in excel_files:
        try:
            df = pd.read_excel(file)
            df["元ファイル名"] = os.path.basename(file)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        except Exception as e:
            print(f"読み込みに失敗しました: {file}, エラー: {e}")

    # 統合結果を保存
    merged_df.to_excel(output_file, index=False)
    print(f"統合が完了しました: {output_file}")


if __name__ == "__main__":
    input_folder = "input_excels"
    output_file = "merged.xlsx"

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"{input_folder} フォルダを作成しました。ここにExcelを入れてください。")

    merge_excels(input_folder, output_file)
