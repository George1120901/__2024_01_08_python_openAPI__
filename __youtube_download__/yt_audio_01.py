# base get_audio_only V0.9 --> 2024.06.24 ok

from pytube import YouTube
import re
import subprocess

def streams_analysis(url):
    yt = YouTube(url) 
    # 影片格式分析
    print(f'標題: {yt.title}')              # 影片標題
    print(f'長度(s): {yt.length}')          # 影片長度 ( 秒 )
    print(f'作者: {yt.author}')             # 影片作者
    print(f'網址: {yt.channel_url}')        # 影片作者頻道網址
    print(f'縮圖網址: {yt.thumbnail_url}')  # 影片縮圖網址
    print(f'觀看數: {yt.views}')            # 影片觀看數

    # 分析
    print(f'支援畫質:{yt.streams}')  # 影片支援哪些畫質
    # print(yt.streams.all())  # all()-->useless
    print('影片支援畫質數: ',len(yt.streams))

    for st in yt.streams:
        print(st)


def get_audio_only(url):
    yt = YouTube(url)   
    print('全名 : ',yt.title)
    list=['/',':','"','<','>','\?','\*']
    yt_titles = yt.title
    for i in list:
        yt_title = re.sub(f'{i}','_',yt_titles)
        yt_titles = yt_title
    print(yt_titles)

    #yt_title = re.search(r'[A-Za-z0-9_ ]+',yt_titles).group()
    yt_title = re.search(r'[\w\u4e00-\u9fff\s]+',yt_titles).group() #設定包含中英文字
    print('簡稱 : ',yt_title)

    yt_audio = yt.streams.filter(abr='128kbps').first()
    yt_audio.download(output_path='C:/Users/Lu/Documents/youtube',filename=f'yt_audio_{yt_title}.mp4', skip_existing=True, max_retries=0)  
    print(f'downdload < {yt.title} > 完成')
    return yt_title

def convert_mp4_to_mp3(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-q:a', '3',
        output_file
    ]
    
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,encoding= 'utf-8')  # 設定encoding='utf-8'
        print("轉換成功！輸出文件位於:", output_file)
    except subprocess.CalledProcessError as e:
        print("ffmpeg轉換過程中發生錯誤:", e)
        if e.stderr:
            print("ffmpeg命令輸出:", e.stderr)
        else:
            print("無法獲取 ffmpeg 錯誤輸出。")

 
# url = 'https://www.youtube.com/watch?v=BGOMTRv-8Js'  # test曲目: Johann Pachelbel - Canon in D major 約翰 帕海貝爾 D大調卡農 古典音樂 放鬆 Classical Music relaxing

work_item = int(input('輸入 ( 1 :分析   2:下載   其他:跳出執行 )'))
if work_item == 1:
   url = str(input("輸入影音網址 (Enter the url of media) : ")) 
   streams_analysis(url) 
elif work_item == 2:
    url = str(input("輸入影音網址(Enter the url of media) : "))  
    yt_title = get_audio_only(url)  #返回結果方式
    convert_mp4_to_mp3(f'C:/Users/Lu/Documents/youtube/yt_audio_{yt_title}.mp4', f'C:/Users/Lu/Documents/youtube/yt_audio_{yt_title}.mp3')
else:
     print('輸入 ( 1 :分析   2:下載   其他:跳出執行 )')