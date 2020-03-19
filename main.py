'''
function:conver the audio to text
note:
1.start pycharm with acministrator role
2.put MUMU on the left top.
3.set input device to stereo in Windows
4.open ifly input method in MUMU in advance
requirement:
1.MUMU Android simulator
2.install yinxiang and ifly input method in MUMU
3.install pydub refer https://github.com/jiaaro/pydub
4.pip install pyautogui
limited:
1.audio length should less than 24 hours
2.lingos app and some other copy words app would cause typing error
'''
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from pydub.playback import play
import pyautogui
import pyperclip
import time, datetime
import os


# convert millisecond to '00:00:39,770'
def format_time(ms):
    # ms = millisecond%1000
    # second = millisecond/1000
    # hour = millisecond/
    td = datetime.timedelta(milliseconds= ms)
    return str(td).replace('.',',')


# 模拟器位于左上时，键位的坐标
space_loc = (239, 927)
enter_loc = (484, 936)
edit_loc = (310, 607)
select_all_loc = (150, 918)
cut_loc = (374, 919)
back_loc = (479, 922)
# audio dir
file_path = "2. 雅思模考卷1S2.mp3"
file_suffix = os.path.splitext(file_path)[-1][1:]
print("file path:",file_path,"suffix",file_suffix)
# write a file
srt_file = os.path.splitext(file_path)[0]+'.srt'
f = open(file=srt_file, mode="w",encoding='utf8')
sound = AudioSegment.from_file(file_path, file_suffix)

start_time = time.localtime()
print("start",time.strftime('%H:%M:%S',start_time))

idx = 0
min_silence_len = 500
previous_end = 0
timestamp_list = detect_nonsilent(sound, 500, sound.dBFS * 1.3, 10)
for i in range(len(timestamp_list)):
    d = timestamp_list[i][1] - timestamp_list[i][0]
    a = timestamp_list[i][0]
    b = timestamp_list[i][1]
    # srt file's index
    idx +=1
    # soft the voice, add the period which is around the threshold
    start = max(0, a - min_silence_len / 2, previous_end)
    if i == len(timestamp_list) - 1:
        end = min(len(sound), b + min_silence_len)
    else:
        end = min(timestamp_list[i + 1][0], b + min_silence_len)
    previous_end = b
    # input index and timestamp
    index_time = '{0}\n{1} --> {2}\n'.format(idx, format_time(start), format_time(end))
    # press space
    pyautogui.moveTo(space_loc[0], space_loc[1])
    pyautogui.mouseDown()
    time.sleep(0.05)
    play(sound[start: end])
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.5)
    # cut
    delay_time = 1 #second
    pyautogui.click(edit_loc[0], edit_loc[1])
    time.sleep(delay_time)
    pyautogui.click(select_all_loc[0], select_all_loc[1])
    time.sleep(delay_time)
    pyautogui.click(cut_loc[0], cut_loc[1])
    time.sleep(delay_time)
    pyautogui.click(back_loc[0], back_loc[1])
    time.sleep(delay_time)
    text = pyperclip.paste()
    f.write(index_time+text+'\n')
    print("Section is :", timestamp_list[i], "duration is:", d,'text:',text)
f.close()
# end
end_time = time.localtime()
print('end',time.strftime('%H:%M:%S',end_time),'processing time:',
      format_time(1000*(time.mktime(end_time)-time.mktime(start_time) ) ),
      'audio time:',str(datetime.timedelta(milliseconds=len(sound)) ) )

