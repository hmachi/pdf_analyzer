import os
import sys
from pathlib import Path
from subprocess import call
import glob
import datetime

# PDF読込用のツールのパス
py_path = "pdf2txt.py"

# フォルダ内のpdfファイル一覧を取得
files = glob.glob("./*.pdf")

for index, file in enumerate(files):
    processTextFileName = str(index) + "_process.txt"

    # PDFファイルをテキストファイルに変換
    call(["py", str(py_path), "-o" + processTextFileName, "-p 1", file])

    pdf_name = ""
    with open(processTextFileName, 'r', encoding='UTF-8') as f:
        lines = f.read()

        for index, line in enumerate(lines.split('\n', 1)):
            if line != "":
                # 最初の空白行以外を取得
                pdf_name = line
                break

    if pdf_name != "":
        # ファイル名として使用できない文字を変更
        pdf_name = pdf_name.replace('/', '')
        pdf_name = pdf_name.replace(':', '')
        pdf_name = pdf_name.replace('\\', '')
        pdf_name = pdf_name.replace('*', '')
        pdf_name = pdf_name.replace('?', '')
        pdf_name = pdf_name.replace('"', '')
        pdf_name = pdf_name.replace('<', '')
        pdf_name = pdf_name.replace('>', '')
        pdf_name = pdf_name.replace('|', '')

        # 作成したテキストファイルの削除
        os.remove(processTextFileName)

        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)

        # PDFファイルのリネームと移動
        os.rename(file, "after/" + pdf_name + "_" +
                  now.strftime('%Y%m%d%H%M%S') + ".pdf")

        # TODO 検索用にDBにデータを保存してもいい
