import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from models import EditPDFRequest
from pdf import edit_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.post("/pdf")
async def edit_pdf_file(request: EditPDFRequest) -> FileResponse:
    output_pdf = "templates/mercado_pago_editado.pdf"
    edit_pdf(
        "templates/mercado_pago.pdf",
        output_pdf,
        request.new_value,
        request.new_name,
        request.new_cpf,
        request.new_bank,
        request.new_agency,
        request.new_account,
    )

    return FileResponse(output_pdf)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port="8000",
        log_level="info",
        workers=2,
        reload=True,
        reload_dirs=["./"],
    )
