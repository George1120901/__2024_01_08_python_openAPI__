# [Todo] from ChatGpt
import argparse
import subprocess
import sys
from pathlib import Path

def run_cmd(cmd):
    print("🚀 執行：")
    print(" ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("❌ 指令執行失敗")
        sys.exit(1)

def download_with_ytdlp(url, output, mode, audio_format):
    """
    使用 yt-dlp 下載
    """
    cmd = ["yt-dlp", url]

    if mode == "video":
        cmd += [
            "-f", "bv*+ba/best",        # 最佳影像 + 最佳音訊
            "--merge-output-format", "mp4",
            "-o", output
        ]

    elif mode == "audio":
        cmd += [
            "-x",                       # extract audio
            "--audio-format", audio_format,
            "-o", output
        ]

    run_cmd(cmd)

def post_process_ffmpeg(input_file, output_file, action):
    """
    ffmpeg 後處理
    """
    if action == "extract_audio":
        cmd = [
            "ffmpeg", "-i", input_file,
            "-vn", "-acodec", "libmp3lame",
            "-b:a", "192k",
            "-y", output_file
        ]
        run_cmd(cmd)

    elif action == "convert_mp4":
        cmd = [
            "ffmpeg", "-i", input_file,
            "-c:v", "libx264",
            "-crf", "23",
            "-preset", "medium",
            "-c:a", "aac",
            "-y", output_file
        ]
        run_cmd(cmd)

def main():
    parser = argparse.ArgumentParser(
        description="🎬 yt-dlp + ffmpeg 混合媒體下載工具"
    )

    parser.add_argument("url", help="媒體網址（YouTube / 串流 / 網站）")
    parser.add_argument(
        "--mode",
        choices=["video", "audio"],
        default="video",
        help="下載模式"
    )
    parser.add_argument(
        "--output",
        default="%(title)s.%(ext)s",
        help="輸出檔名樣板（yt-dlp 格式）"
    )
    parser.add_argument(
        "--audio-format",
        default="mp3",
        help="音訊格式（mp3 / m4a / opus）"
    )
    parser.add_argument(
        "--post",
        choices=["none", "extract_audio", "convert_mp4"],
        default="none",
        help="下載後的 ffmpeg 後處理"
    )
    parser.add_argument(
        "--post-output",
        help="後處理輸出檔名（僅 post != none 時需要）"
    )

    args = parser.parse_args()

    download_with_ytdlp(
        args.url,
        args.output,
        args.mode,
        args.audio_format
    )

    if args.post != "none":
        if not args.post_output:
            print("❌ 使用 post 時必須指定 --post-output")
            sys.exit(1)

        # 假設 yt-dlp 下載後的檔名已知（簡化示例）
        input_file = Path(args.output.replace("%(title)s", "*")).as_posix()

        post_process_ffmpeg(
            input_file,
            args.post_output,
            args.post
        )

if __name__ == "__main__":
    main()
