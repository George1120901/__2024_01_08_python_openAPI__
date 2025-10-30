## argparseVerbose_031.py版 + except argparse.ArgumentError:
import argparse
parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument("-v",
                    "--verbosity",
                    type=int,
                    choices=[0, 1, 2],
                    help="請輸入囉唆程度")
try:
    args = parser.parse_args()   
    print(f"args.verbosity 的值為：{args.verbosity}")
except argparse.ArgumentError:
    print('Catching an argumentError')