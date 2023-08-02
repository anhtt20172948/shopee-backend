from fastapi import APIRouter
from models.voucher import Voucher
from database.database import DataBase
from bson import json_util
import json
router = APIRouter(prefix="/voucher", tags=["Voucher"])

database = DataBase()

@router.get("/get_voucher_by_name")
async def get_voucher_by_name(name: str):
    """Returns the name voucher"""
    voucher = database.colection_voucher.find_one({"name":name})
    return json.loads(json_util.dumps(voucher))

@router.get("/get_all_vouchers")
async def get_all_vouchers():
    """Returns all voucher"""
    voucher = database.colection_voucher.find()
    return json.loads(json_util.dumps(voucher))

@router.post("/add_voucher")
async def add_voucher(voucher:Voucher):
    print(voucher)
    voucher = dict(voucher)
    print(voucher)
    database.colection_voucher.insert(voucher)
    voucher = json.loads(json_util.dumps(voucher))
    return voucher


@router.post("/update_by_id")
async def update_by_code(id: str, status:str, code:str, shop:str, type:str, device:str):
    print(status)
    voucher = database.colection_voucher.find_one_and_update({"id":id}, {"$set": {"status": status, "code":code, "shop":shop, "type_voucher":type, "device":device}})
    return json.loads(json_util.dumps(voucher))


@router.post("/delete_by_id")
async def delete_by_id(id: str):
    voucher = database.colection_voucher.find_one_and_delete({"id":id})
    return json.loads(json_util.dumps(voucher))