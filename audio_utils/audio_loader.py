import librosa
import numpy as np

from scipy.io import wavfile
from typing import List
from starlette.datastructures import UploadFile


def import_wav(file_source: UploadFile):
    sr, audio = wavfile.read(file_source.file)
    audio = resample_audio(audio, sr)
    audio = normalize_audio(audio)
    return audio


def import_wavs(file_source_list: List[UploadFile]):
    audio_list = []

    for file_source in file_source_list:
        audio = import_wav(file_source)
        audio_list.append(audio)
    return audio_list


def resample_audio(audio: np.array, sr: int, target_sr: int = 16000):
    return librosa.resample(audio / np.max(audio), sr, target_sr) if sr != target_sr else audio


def normalize_audio(audio: np.array):
    audio = audio / np.max(audio)
    audio = audio * (32767 - 2**10)  # int16 is type wanted in DeepSpeech
    audio = audio.astype(np.int16)
    assert np.max(audio) < 32767, "Problem with normalization has occured."
    return audio

# consider if it is important to implement mono signal