from pydub import AudioSegment
import numpy as np

song = AudioSegment.from_mp3("SampleMusic/Ratatat - Loud Pipes.mp3")

window_length = 1000   #  1 sec
window_stride = 500    # .5 sec
duration = len(song)

print "Frame Count: "+str(song.frame_count())
print "Frame Width: "+str(song.frame_width)
print "Frame Rate : "+str(song.frame_rate)
print "Sampl Width: "+str(song.sample_width)
print "Channels   : "+str(song.channels)

sample_array =  song[:1000].split_to_mono()[1].get_array_of_samples()

x = np.absolute(np.fft.fft(sample_array))


print x 
print x.shape

#for idx in range(0,duration,window_stride):
#    print "Outputing slice " + str(idx)
#    song[idx:idx+window_length-1].export("testdata/song1_"+str(idx)+".wav", format="wav")


