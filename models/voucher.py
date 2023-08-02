from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import uuid

class Voucher(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    code: str
    status: Optional[str] = "Mới đặt"
    data_create: Optional[str] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    device: str
    shop: str
    type_voucher: str
    