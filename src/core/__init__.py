"""
核心算法模块

提供滑块验证码识别的核心算法实现。
"""

from src.core.ocr import recognize_by_ocr, get_classification_ocr_instance
from src.core.opencv import recognize_by_opencv

__all__ = [
    "recognize_by_ocr",
    "get_classification_ocr_instance",
    "recognize_by_opencv",
]

