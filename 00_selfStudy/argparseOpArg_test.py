## argparseOpArg_test.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("first_position_arg",
                    nargs=2,
                    help="這是第 1 個位置引數，請輸入兩個任意值")
parser.add_argument("-a",
                    "--arg1",
                    type=str,
                    help="這是第 1 個選項引數，請輸入一個字串")
parser.add_argument("--arg2",
                    nargs=3,
                    type=int,
                    help="這是第 2 個選項引數，請輸入三個整數")
args = parser.parse_args()
print(args)