from typing import List

from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse

from audio_utils.audio_loader import import_wavs

app = FastAPI()


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
    transcript = "Sample text tha has been created"

    content = {"transcript": transcript}
    return JSONResponse(content)