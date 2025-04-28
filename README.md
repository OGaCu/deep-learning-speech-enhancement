# Speech Enhancement from Noise Filtration

### Background
Speech enhancement is fundamentally a task of extracting desired speech signals from noisy environments. Spectral-masking model approaches speech problems by learning to generate a mask that is multiplied to the original audio. The mask not only hightlights speech components while suppressing noise components. This technique is computationally efficient compared to directly predicting clean speech, as the model only needs to learn the difference between clean and noisy signals rather than reconstructing the entire waveform from scratch like in traditional method of waveform-masking. 

Implemented and trained PyTorch based deep neural network models that produce a clean, enhanced speech and perform noise filtration tasks. 

This technique serves as a critical component for **voice assistants** such as Siri and Alexa, where enhanced speech signals significantly improve the accuracy of automated speech detection and recognition.

[**Click here for accessing this repo**](https://github.com/OGaCu/deep-learning-speech-enhancement/edit/main/README.md)

[Click here for more in-depth Methodology on the wesite](https://sites.google.com/umich.edu/eecs-351noisefiltering/methods)

## Features
- Noise removal from speech recordings
- Spectrogram visualization for audio analysis
- The best-performing mode is trained on HPC for efficiency

<!-- ![speech with intrusive noise](spectrograms/example_whamr_spectrogram.png)![clean audio after processing](spectrograms/exapmple_whamr_enhanced_speech_spectrogram.png) -->

| speech with intrusive noise | clean audio after processing |
|:-------:|:-------:|
| ![speech with intrusive noise](spectrograms/example_whamr_spectrogram.png) | ![](spectrograms/exapmple_whamr_enhanced_speech_spectrogram.png) |

## Project Structure
```
├── requirements.txt                         # dependencies for set up
├── virtual_env.sh                           # shell script for using virtual environment for dev
├── create_spectrograms_from_wav.ipynb       # notebook to visualize audio
├── custom_model_driver.py                   # main file to train custom model
│   ├── data_prep.py
│   ├── train.yaml
│   └── model_helpers.py
├── pretrain_driver.py                       # try out pretrained models
│   └── best_hyperparams.yaml
├── noisyspeech_synthesizer.cfg              # config file for syn_noisy
├── noisyspeech_synthesizer.py               # backbone for the synthesizer
├── plot_syn_noisy_time.py                   # code for plotting time-domain visualization
├── syn_noisy/                               # example of customized synthesized noise   
├── whamr/                                   # intrusive noisy speech examples
├── frontend/                                # htmls for model code embeddings
└── audio/                                   # more wav files to play with from MS-SNSD
```

## Setup

#### 1. Clone the repository
```bash
git clone https://github.com/OGaCu/speech-enhancement.git
```

#### 2. Install dependencies
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```

## Notes
- If you would like to train your own model, you may need access to High Performance Computing services, which is designed to support computationally intensive research across disciplines with a focus on simulations, data modeling, and AI.
- Special thanks to Dr. Maha Ali and Alyssa Anderson

## Troubleshooting
- **No wav files found**: Make sure they exist under `audio` with the correct names.

## License
MIT License – feel free to use, modify, and share.

## 🙌 Acknowledgements
- [Attention is All You Need in Speech Separation](https://arxiv.org/abs/2010.13154)
- [A General-Purpose Speech Toolkit](arXiv:2106.04624)
- [TorchAudio](https://pytorch.org/audio/stable/index.html)
- [Open-Source Conversational AI with SpeechBrain](https://arxiv.org/abs/2407.00463)
- [MN-SNSD by Microsoft](https://github.com/microsoft/MS-SNSD/blob/master/README.md)
- [WSJ0 Hipster Ambient Mixtures](http://wham.whisper.ai/)
- [PyTorch](https://pytorch.org/docs/stable/nn.html)


