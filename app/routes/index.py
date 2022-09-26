from datetime import datetime

from fastapi import APIRouter, Depends
from starlette.responses import Response
from sqlalchemy.orm import Session

from app.database.schema import Users
from app.database.conn import db

router = APIRouter()


@router.get("/")
async def index():
    """
    ELB 상태 체크용 API
    :return:
    """

    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
