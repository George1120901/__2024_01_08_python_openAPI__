## argparseVerbose_01.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose",
                    action="store_true",  # 引數儲存為 boolean
                    help="簡單開關的引數")
args = parser.parse_args()
print('args.verbose 的數值為：',args.verbose)
if args.verbose :
    print('我現在是個囉唆的程式')
else:
    print('未指示如何處理！')