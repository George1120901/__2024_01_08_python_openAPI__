## argparseVerbose_04.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v",
                    "--verbose",
                    action="count",
                    default=0,
                    help="請輸入囉唆程度")
args = parser.parse_args()
print(f"args.verbose 的值為：{args.verbose}")

if args.verbose == 0  and args.verbose >= 4:
    print('請輸入囉唆程度-選擇:1~3')
elif args.verbose == 1 : 
    print('進入囉唆度 level1')
elif args.verbose == 2 : 
    print('進入囉唆度 level2')
else:
    print('進入囉唆度 level3')