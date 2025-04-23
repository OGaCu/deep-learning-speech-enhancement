from speechbrain.inference.separation import SepformerSeparation as separator
import torchaudio
import torch
import os

os.environ["TORCHAUDIO_BACKEND"] = "soundfile"  

model = separator.from_hparams(source="speechbrain/sepformer-whamr-enhancement", 
                               savedir='pretrained_models/sepformer-whamr-enhancement4')

enhanced_speech = model.separate_file(path='/home/yangct/351_mic_peak.wav')
sample_rate = 16000

output_path = '/home/yangct/351_enhanced_speech.wav'
torchaudio.save(output_path, enhanced_speech, sample_rate)
print(f"Enhanced speech saved to {output_path}")
