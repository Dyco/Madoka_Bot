from typing import Dict
from pathlib import Path
from ..utils import ResType, SubFolder, get_indexed_files

# ====== 启动时生成皮肤映射 ======

SKIN_MAP: Dict[str, Path] = get_indexed_files(
    ResType.IMAGE,
    SubFolder.CHAR,
    prefix="skin"
)