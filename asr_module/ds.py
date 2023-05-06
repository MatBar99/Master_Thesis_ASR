import deepspeech
import numpy as np


def init_stt_model(model_path: str, scorer_path: str):
    model = deepspeech.Model(model_path)
    model.enableExternalScorer(scorer_path)
    return model


def speech_to_text(model: deepspeech.Model, audio: np.array):
    return model.stt(audio)

if __name__ == "__main__":
    print("Modules to use ds")

