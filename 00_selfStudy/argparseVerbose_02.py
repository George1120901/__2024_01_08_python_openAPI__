## argparseVerbose_02.py
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v",
                   "--verbose",
                   action="store_true",
                   help="開啟囉唆模式")
group.add_argument("-q",
                   "--quiet",
                   action="store_true",
                   help="開啟安靜模式")
args = parser.parse_args()
if args.verbose:
    print("我現在是個--囉--唆--的程式！")
elif args.quiet:
    print("我現在是個--安.安.靜.靜-- 的程式")
else:
    print(f"args.verbose 的值為：{args.verbose}")
    print(f"args.quiet 的值為：{args.quiet}")
    print("你沒有告訴我該囉唆還是安靜？")