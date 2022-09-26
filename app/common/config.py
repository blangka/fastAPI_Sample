from dataclasses import dataclass, asdict
from os import path, environ

# 상대경로를 하기 어렵기 때문에 절대 경로를 위해서 관리 용도로 사용한다.
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config): # Config를 상속받음
    PROJ_RELOAD: bool = True

# 언팩킨해서 사용할 수 있도록 asdict를 사용한다.
# asdict는 dataclass를 dict로 변환해준다.
# def abc(DB_EHO=None, DB_POOL_RECYCLE=None, **kwargs):
#     print(DB_EHO, DB_POOL_RECYCLE)
#
# print(asdict(LocalConfig()))
# arg = asdict(LocalConfig())
# abc(**arg)
# 딕셔너리 형태로 넘길수 있다.

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local")) # 환경변수를 가져온다. 없다면 local을 써라


