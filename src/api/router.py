"""
API 路由注册

对外由应用挂载在 ``/api/v1``（或环境变量 API_PREFIX）下，形成统一结构::

    /api/v1/                     服务信息
    /api/v1/health               健康检查
    /api/v1/slider/...           滑块验证码
    /api/v1/arithmetic/...       算术验证码
    /api/v1/text/...             文字验证码
"""

from fastapi import APIRouter

from src.api.routes import health, slider, arithmetic, text


api_router = APIRouter()

api_router.include_router(
    health.router,
    tags=["健康检查"],
)

api_router.include_router(
    slider.router,
    prefix="/slider",
    tags=["滑块识别"],
)

api_router.include_router(
    arithmetic.router,
    prefix="/arithmetic",
    tags=["算术识别"],
)

api_router.include_router(
    text.router,
    prefix="/text",
    tags=["文字识别"],
)

