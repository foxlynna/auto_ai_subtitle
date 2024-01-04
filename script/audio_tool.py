import ffmpeg
import subprocess
from moviepy.editor import VideoFileClip
def mp4ToMp3(mp4_file_name, mp3_file_name):
    """mp4ToMp3
    Args:
        mp4_file_name (_type_): mp4 file path
        mp3_file_name (_type_): mp3 file path
    """
    video = VideoFileClip(mp4_file_name)
    audio = video.audio
    audio.write_audiofile(mp3_file_name)
    
# def audio_extract(input, output):
# 	ffmpeg.input(input, vn=None).output(output).run()

# 解决中文路径ffmpeg无法运行的问题
def audio_extract(input_path, output_path):
	command = [
		'ffmpeg', 
		'-i', 'pipe:0',  # 从stdin读取输入
		'-pix_fmt', 'yuv420p',
		'-analyzeduration','2147483647',
		'-probesize', '2147483647',
		'-vn',          # 仅提取音频
		output_path     # 输出文件路径
	]
	print(command)
	with open(input_path, 'rb') as f:
		subprocess.run(command, input=f.read())