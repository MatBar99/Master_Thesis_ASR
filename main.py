from typing import List

from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse

from audio_utils.audio_loader import import_wavs
from asr_module.ds import init_stt_model, speech_to_text

config_dict = {"model_path": "deepspeech-0.9.3-models.pbmm",
               "scorer_path": "deepspeech-0.9.3-models.scorer"}

app = FastAPI()
model = init_stt_model(model_path=config_dict["model_path"],
                       scorer_path=config_dict["scorer_path"])

@app.get("/", response_class=HTMLResponse, tags=["utils"])
def redirect():
    html_content = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Polish Speech Library</title>
             <meta charset="UTF-8" />
             <meta http-equiv="refresh" content="1; URL=/docs" />
           </head>
           <body>
             <p>Redirecting to the API Swagger</p>
           </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/transcript", response_class=JSONResponse)
async def transcript_file(files: List[UploadFile]):

    audio_list = import_wavs(file_source_list=files)
    transcripts =[]
    for audio in audio_list:
        transcripts.append(speech_to_text(model, audio))

    content = {"transcripts": transcripts}
    return JSONResponse(content)

# TODO Implement normalization and resampling, if files have different sampling frequency than 16kHz
# TODO transcription has poor quality.