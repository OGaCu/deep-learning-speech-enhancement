# Speech Enhancement from Noise Filtration

[Click here for more on Methodology] (https://sites.google.com/umich.edu/eecs-351noisefiltering/methods)

![speech with intrusive noise](spectrograms/example_whamr_spectrogram.png) ![clean audio after processing](spectrograms/exapmple_whamr_enhanced_speech_spectrogram.png)


## 🔍 Features
- Noise removal from speech recordings
- Spectrogram visualization for audio analysis


## 📁 Project Structure
```
├── requirements.txt                         # dependencies for set up
├── create_spectrograms_from_wav.ipynb       # notebook to visualize audio
├── syn_noisy/                               # example of customized synthesized noise   
├── whamr/                                   # intrusive noisy speech examples
├── frontend/                                # html files for model code embeddings
└── audio/                                   # more wav files to play with from MS-SNSD
```

## ⚙️ Setup

#### 1. Clone the repository
```bash
git clone https://github.com/OGaCu/speech-enhancement.git
```

#### 2. Install dependencies
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```

## 🧪 Notes
- 

## 🛠️ Troubleshooting
- **No wav files found**: Make sure they exist under `audio` with the correct names.

## 📄 License
MIT License – feel free to use, modify, and share.

## 🙌 Acknowledgements
- 