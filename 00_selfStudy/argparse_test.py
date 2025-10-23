# test.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("arg1",
                    nargs=3,
                    type=int,
                    help="這是第 1 個引數，請輸入三個整數")
parser.add_argument("arg2",
                    nargs='?',
                    help="這是第 2 個引數，請輸入一個值、也可以不輸入",
                    default="NO_VALUE")
parser.add_argument("arg3",
                    nargs='+',
                    help="這是第 3 個引數，請輸入一個或多個值")
args = parser.parse_args()
print(args)