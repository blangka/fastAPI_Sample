from datetime import datetime

from fastapi import APIRouter, Depends
from starlette.responses import Response
from sqlalchemy.orm import Session

from app.database.schema import Users
from app.database.conn import db

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session)):
    """
    ELB 상태 체크용 API
    :return:
    """
    # 샘플로 DB 테스트
    Users().create(session, auto_commit=True, status='active', name='코알라')

    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
