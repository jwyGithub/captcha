"""
文字验证码识别路由

提供字符类验证码识别的 API 接口。
"""

from fastapi import APIRouter, Depends, Query

from src.api.deps import get_text_service
from src.logger import get_logger
from src.schemas import TextCaptchaRequest, create_success_response
from src.services import TextService


logger = get_logger(__name__)

router = APIRouter()


@router.post(
    "/recognize",
    summary="识别文字验证码",
    description="识别字符类验证码图片并返回文本，支持 URL 和 Base64 格式图片输入",
    response_description="识别出的文本",
)
async def recognize_text(
    request: TextCaptchaRequest,
    service: TextService = Depends(get_text_service),
):
    """
    识别文字验证码（POST）

    通过 JSON Body 传入图片（URL 或 Base64）。

    Args:
        request: 包含 img（URL 或 Base64）的请求体
        service: 文字识别服务实例

    Returns:
        标准响应，data 为识别文本字符串
    """
    logger.info("收到文字验证码识别请求 (POST)")

    text = service.recognize(request.img)

    return create_success_response(
        data=text,
        description="识别成功",
    )


@router.get(
    "/recognize",
    summary="识别文字验证码 (GET)",
    description="通过 URL Query 参数传入图片地址进行文字验证码识别",
    response_description="识别出的文本",
)
async def recognize_text_get(
    img: str = Query(
        ...,
        description="验证码图片 URL",
        examples=["https://example.com/captcha.jpg"],
    ),
    service: TextService = Depends(get_text_service),
):
    """
    识别文字验证码（GET）

    通过 Query 参数 ``img`` 传入图片 URL，适合浏览器直接调用。

    Args:
        img: 验证码图片 URL
        service: 文字识别服务实例

    Returns:
        标准响应，data 为识别文本字符串
    """
    logger.info("收到文字验证码识别请求 (GET)")

    text = service.recognize(img.strip())

    return create_success_response(
        data=text,
        description="识别成功",
    )
