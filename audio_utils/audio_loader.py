import soundfile as sf

from typing import List
from starlette.datastructures import UploadFile


def import_wav(file_source: UploadFile):
    audio, sr = sf.read(file_source.file)
    return audio


def import_wavs(file_source_list: List[UploadFile]):
    audio_list = []

    for file_source in file_source_list:
        audio = import_wav(file_source)
        audio_list.append(audio)
    return audio_list
# TODO add proper normalization if it is not implemented already in DeepSpeech.