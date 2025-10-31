## argparseVerbose_Sum.py
import argparse
parser = argparse.ArgumentParser(
    prog="我的程式 argparseVerbose_Sum.py",
    description="這是用來介紹程式功能的地方",
    epilog="這是寫在 help 頁面最後面的句子")
parser.add_argument("-v",
                    "--verbose",
                    action="store_true",
                    help="簡單開關的引數")
args = parser.parse_args()
print(f"args.verbose 的值為：{args.verbose}")