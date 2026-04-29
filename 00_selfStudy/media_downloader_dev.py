import argparse
import subprocess
import sys

def run_cmd(cmd):
    print("🚀 執行：")
    print(" ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("❌ 指令執行失敗")
        sys.exit(1)

def download(url, mode, output, audio_format):
    cmd = ["yt-dlp"]

    if mode == "video":
        cmd += [
            "-f", "bv*+ba/best",
            "--merge-output-format", "mp4"
        ]

    elif mode == "audio":
        cmd += [
            "-x",
            "--audio-format", audio_format
        ]

    cmd += [
        "-o", output,
        url
    ]

    run_cmd(cmd)

def main():
    parser = argparse.ArgumentParser(
        description="yt-dlp + ffmpeg 媒體下載工具（開發版）"
    )

    parser.add_argument("url", help="影片或串流網址")
    parser.add_argument(
        "--mode",
        choices=["video", "audio"],
        default="video"
    )
    parser.add_argument(
        "--output",
        default="%(title)s.%(ext)s",
        help="輸出檔名樣板"
    )
    parser.add_argument(
        "--audio-format",
        default="mp3",
        help="音訊格式（mp3 / m4a / opus）"
    )

    args = parser.parse_args()

    download(
        args.url,
        args.mode,
        args.output,
        args.audio_format
    )

if __name__ == "__main__":
    main()