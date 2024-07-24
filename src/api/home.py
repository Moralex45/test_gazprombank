from fastapi import APIRouter, Depends, Request, Form
from service.log_service import get_log_service, LogService
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="api/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )


@router.post("/", response_class=HTMLResponse)
async def home(
    request: Request,
    address: str = Form(...),  # Add Form parameter
    log_service: LogService = Depends(get_log_service)
):
    result, len_result = await log_service.get_form_result(address)
    return templates.TemplateResponse(
        request=request, name="result.html", context={
            "result": result, "len_result": len_result})
