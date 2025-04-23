import os
import torch
import torchaudio
import speechbrain as sb
from hyperpyyaml import load_hyperpyyaml
from mini_librispeech_prepare import prepare_mini_librispeech
from data_prep import dataio_prep
from model_helpers import Brain
from model_helpers import train_custom_model

def populate_dataset(hparams):
    prepare_mini_librispeech(
        data_folder=hparams["data_folder"],
        save_json_train=hparams["train_annotation"],
        save_json_valid=hparams["valid_annotation"],
        save_json_test=hparams["test_annotation"],
    )
    datasets = dataio_prep(hparams)
    return datasets

def enhance_audio(noisy_file, output_file_path):
    """
    Enhance a noisy audio file and save the result.
    
    Arguments:
    ---------
    noisy_file : str
        Path to the noisy WAV file
    output_file : str
        Path where to save the enhanced WAV file
    """
    with open("train.yaml") as fin:
        hparams = load_hyperpyyaml(fin)
    sb.create_experiment_directory(hparams["output_folder"])

    brain = Brain(
        modules=hparams["modules"],
        opt_class=hparams["opt_class"],
        hparams=hparams,
        checkpointer=hparams["checkpointer"],
    )

    print(f"hyperparameters established")
    # print(f"seed: {hparams["seed"]}")
    print(f"compute in frequency domain using: {hparams["compute_STFT"]}")
    print(f"custom masking model architecture overview: {hparams["model"]}")

    datasets = populate_dataset(hparams)
    se = train_custom_model(brain, datasets, hparams)

    noisy_wav, sample_rate = torchaudio.load(noisy_file)
    noisy_wav = noisy_wav.to(se.device)
    noisy_feats = se.compute_feats(noisy_wav)
    
    # Apply the model to get the mask
    with torch.no_grad():
        mask = se.modules.model(noisy_feats)
    
    enhanced_feats = torch.mul(mask, noisy_feats)
    
    # Convert back to waveform
    enhanced_wav = se.hparams.resynth(torch.expm1(enhanced_feats), noisy_wav)
    torchaudio.save(output_file_path, enhanced_wav.cpu(), sample_rate)
    
    return enhanced_wav

# Apply to your noisy file
your_noisy_file = "/home/yangct/351_mic_peak.wav"
output_file_path = "/home/yangct/351_enhanced_e20.wav" # epoch 20

enhanced_audio = enhance_audio(your_noisy_file, output_file_path)
# print(f"Enhanced audio saved to {output_file}")
