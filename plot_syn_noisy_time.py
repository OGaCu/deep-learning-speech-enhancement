import matplotlib.pyplot as plt
from scipy.io import wavfile

# List your .wav file paths
audio_files = ['clean/p234_001.wav', 'noise/AirConditioner_1.wav', 'NoisySpeech_training/noisy1_SNRdb_0.0_clnsp1.wav']
# plot_file_names = ['clean/speech_p234_001.wav', 'noise/']
# Create a figure
plt.figure(figsize=(12, 8))

# Loop over each file and plot
for i, file in enumerate(audio_files):
    samplerate, data = wavfile.read(file)
    
    # If stereo, take one channel
    if data.ndim > 1:
        data = data[:, 0]

    time = [t / samplerate for t in range(len(data))]

    plt.subplot(3, 1, i+1)
    plt.plot(time, data)
    plt.title(f'Waveform of {file}')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
