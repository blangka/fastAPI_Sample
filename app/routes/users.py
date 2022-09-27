from fastapi import APIRouter
from starlette.requests import Request

from app.database.schema import Users
from app.errors.exceptions import NotFoundUserEx
from app.model.models import UserMe

router = APIRouter()

# Response Model을 사용하면, Response에 대한 설명 및 범위를 지정해줄수있다.
@router.get("/me", response_model=UserMe)
async def get_user(request: Request):
    """
    get my info
    :param request:
    :return:
    """
    user = request.state.user
    user_info = Users.get(id=user.id)
    return user_info

