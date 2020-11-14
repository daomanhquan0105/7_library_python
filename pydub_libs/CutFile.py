from pydub import AudioSegment
sound1 = AudioSegment.from_file("120.wav", format="wav")
sound2 = AudioSegment.from_file("image_raw.raw", format="raw",frame_rate=44100, channels=2, sample_width=2)

# all other formats use ffmpeg
mp3_audio = AudioSegment.from_file("Hoa+Hải+Đường.mp3", format="mp3")

# use a file you've already opened (advanced …ish)
with open("120.wav", "rb") as wav_file:
    audio_segment = AudioSegment.from_file(wav_file, format="wav")

from pathlib import Path
wav_path = Path("120.wav")
wav_audio = AudioSegment.from_file(wav_path)