from app.database import database
from app.models import FileUpload
from bson import ObjectId

async def upload_file(file_data: FileUpload):
    result = await database.files.insert_one(file_data.dict())
    return str(result.inserted_id)

async def get_files():
    files = await database.files.find().to_list(length=None)
    return files

async def get_file(file_id: str):
    file = await database.files.find_one({"_id": ObjectId(file_id)})
    return file

async def delete_file(file_id: str):
    result = await database.files.delete_one({"_id": ObjectId(file_id)})
    return result.deleted_count > 0