from fastapi import APIRouter, UploadFile, BackgroundTasks, File

from utils.regex_sorter import regex_log_worker
from service.log_service import get_log_service
from connections.postgres import get_session


router = APIRouter()

def read_words(file: UploadFile):
    file_content = file.file.read()
    file_content = file_content.decode('utf-8')
    return file_content.splitlines()

async def file_worker(file_content: str):
    async for session in get_session():
        log_service = get_log_service(session=session)
        for line in file_content:
            parsing_result = regex_log_worker(line)
            if parsing_result.get('log_type') == 'message':
                await log_service.create_message(parsing_result.get('data'))
            elif parsing_result.get('log_type') == 'log':
                await log_service.create_log(parsing_result.get('data'))
            else:
                print('something went wrong')
        

@router.post("/file")
async def send_your_logfile_here(
    background_tasks: BackgroundTasks, 
    file: UploadFile = File(...)
):
    file_content = read_words(file)
    
    background_tasks.add_task(file_worker, file_content)
    
    return {"message": "File uploaded successfully. Processing......"}
