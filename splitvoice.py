from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from pydub.playback import play
import time, datetime
import os


# convert millisecond to '00:00:39,770'
def format_time(ms):
    # ms = millisecond%1000
    # second = millisecond/1000
    # hour = millisecond/
    td = datetime.timedelta(milliseconds= ms)
    return str(td).replace('.',',')


# audio dir
file_path = "4. 雅思模考卷1S4.mp3"
file_suffix = os.path.splitext(file_path)[-1][1:]
print("file path:",file_path,"suffix",file_suffix)

sound = AudioSegment.from_file(file_path, file_suffix)

time.sleep(0.5)
print("start")
# adapt parameter
idx = 0
min_silence_len = 500
previous_end = 0
timestamp_list = detect_nonsilent(sound, min_silence_len, sound.dBFS * 1.3, 10)
for i in range(len(timestamp_list)):
    d = timestamp_list[i][1] - timestamp_list[i][0]
    a = timestamp_list[i][0]
    b = timestamp_list[i][1]
    # input index and timestamp
    idx +=1
    # input index and timestamp
    index_time = '{1} --> {2}'.format(idx, format_time(a), format_time(b))
    print(index_time, "duration is:", d,'ms')
    # soft the voice, add the period which is around the threshold
    start = max(0,a-min_silence_len/2,previous_end)
    if i == len(timestamp_list)-1:
        end = min(len(sound),b+min_silence_len)
    else:
        end = min(timestamp_list[i+1][0],b+min_silence_len)
    play(sound[start: end])
    time.sleep(2)
    previous_end = b
print('dBFS: {0}, max_dBFS: {1}, duration: {2}, split: {3}'.format(round(sound.dBFS,2),round(sound.max_dBFS,2),
                                                                   sound.duration_seconds,len(timestamp_list)))

print('audio time:',str(datetime.timedelta(milliseconds=len(sound)) ) )
