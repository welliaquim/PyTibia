from src.shared.typings import GrayImage
from src.utils.core import locate
from .config import images


# TODO: add unit tests
# TODO: add perf
def isBackpackOpen(screenshot: GrayImage, name: str) -> bool:
    return locate(screenshot, images['containersBars'][name]) is not None


# TODO: add unit tests
# TODO: add perf
def isLockerOpen(screenshot: GrayImage) -> bool:
    return locate(screenshot, images['containersBars']['locker']) is not None
