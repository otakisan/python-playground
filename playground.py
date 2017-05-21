import os
curDir = os.getcwd()
print(curDir)

filelist = os.listdir(os.getcwd())
for f in filelist:
    print(f)

# ヒアドキュメント
heredocsample = """
ヒアドキュメントのサンプルです。
任意の文字列{samplestr}を入れられます。
"""
processedstr = heredocsample.format(samplestr='[任意！]')
print(processedstr)

# 文字列補間
anythingstr = "[サンプル！]"
complstr = f"文字列補間でも、任意の文字列{anythingstr}を入れられます。"
print(complstr)

# ファイル
import codecs
filehandle = codecs.open("playground.py", "r", "utf-8")
alltext = filehandle.read()
filehandle.close()
print(alltext)

## テスト
assert(True)
assert(False)