"""
文字验证码识别服务

使用 ddddocr classification 识别字符类验证码（含干扰线等）。
"""

from src.core.ocr import get_classification_ocr_instance
from src.exceptions import OCRRecognitionError
from src.logger import get_logger
from src.utils import get_image_content


logger = get_logger(__name__)


class TextService:
    """
    文字验证码识别服务

    使用与算术验证码相同的 OCR classification 实例，仅返回识别文本。

    使用示例:
        >>> service = TextService()
        >>> text = service.recognize("https://example.com/captcha.jpg")
    """

    def __init__(self) -> None:
        """初始化服务"""
        self._ocr = get_classification_ocr_instance()

    def recognize(self, image_input: str) -> str:
        """
        识别文字验证码并返回文本

        Args:
            image_input: 图片输入（URL 或 Base64）

        Returns:
            识别出的字符串（可能包含空格，由调用方自行规范化）

        Raises:
            OCRRecognitionError: 识别失败时
        """
        logger.info("开始文字验证码识别...")

        try:
            image_bytes = get_image_content(image_input)
            ocr_result = self._ocr.classification(image_bytes)
            logger.info(f"OCR 识别结果: {ocr_result}")
            return ocr_result.strip()

        except OCRRecognitionError:
            raise
        except Exception as e:
            logger.error(f"文字验证码识别失败: {e}")
            raise OCRRecognitionError(
                message="文字验证码识别失败",
                details=str(e),
            )
