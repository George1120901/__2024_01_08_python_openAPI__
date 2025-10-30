## argparseVerbose_03.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v",
                    "--verbosity",
                    type=int,
                    choices=[0, 1, 2],
                    help="請輸入囉唆程度")
args = parser.parse_args()
print(f"args.verbosity 的值為：{args.verbosity}")