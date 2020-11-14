import os
import glob
from pydub import AudioSegment
from pydub.playback import play

# run mp3
sound = AudioSegment.from_file("Hoa+Hải+Đường.mp3", format="mp3")
play(sound)
# run wav
sound = AudioSegment.from_file("120.wav", format="wav")
play(sound)
# run mp4
sound = AudioSegment.from_file("120.mp4", format="mp4")
play(sound)
# convert mp3 -> ogg
song = AudioSegment.from_mp3("Hoa+Hải+Đường.mp3")
song.export("out.ogg", format="ogg")
# convert mp4 -> mp3
video_dir = 'mp4'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv')
os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')


# cut file:
playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*.mp3")]

first_song = playlist_songs.pop(0)

# let's just include the first 30 seconds of the first song (slicing
# is done by milliseconds)
beginning_of_song = first_song[:30*1000]

playlist = beginning_of_song
for song in playlist_songs:

    # We don't want an abrupt stop at the end, so let's do a 10 second crossfades
    playlist = playlist.append(song, crossfade=(10 * 1000))

# let's fade out the end of the last song
playlist = playlist.fade_out(30)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = len(playlist) / (1000*60)

# lets save it!
with open("%s_minute_playlist.mp3" % playlist_length, 'wb') as out_f:
    playlist.export(out_f, format='mp3')

#cut file and edit data

ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds]
last_5_seconds = song[-5000:]
# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3
without_the_middle = beginning + end
without_the_middle.duration_seconds == 15.0
backwards = song.reverse()

with_style = beginning.append(end, crossfade=1500)
do_it_over = with_style * 2
awesome = do_it_over.fade_in(2000).fade_out(3000)
awesome.export("mashup.mp3", format="mp3")