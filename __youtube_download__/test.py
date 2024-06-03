# 直接在終端機上執行 :
# $ python test.py -->ok
import subprocess

def merge_video_and_audio(video_path, audio_path, output_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-i', audio_path,
        '-c', 'copy',
        '-map', '0:v',
        '-map', '1:a',
        output_path
    ]
    
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("合併成功！輸出文件位於:", output_path)
    except subprocess.CalledProcessError as e:
        print("ffmpeg合併過程中發生錯誤:", e)
        if e.stderr:
            print("ffmpeg命令輸出:", e.stderr)
        else:
            print("無法獲取 ffmpeg 錯誤輸出。")

merge_video_and_audio("C:/Users/Lu/Documents/youtube/python_231212V.mp4", "C:/Users/Lu/Documents/youtube/python_231212A.mp4", "C:/Users/Lu/Documents/youtube/python_231212All.mp4")
