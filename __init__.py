import sys
from pathlib import Path
from .utils import here
import platform

sys.path.insert(0, str(Path(here, "src").resolve()))

from .nodes.image.load_node import LoadImageNode
from .nodes.image.save_node import SaveImageNode
from .nodes.image.save_node import SaveImagesNode
from .nodes.image.size_node import ImageResizeNode
from .nodes.image.size_node import ImageSizeNode
from .nodes.image.size_node import ConstrainImageNode
from .nodes.image.watermark_node import WatermarkNode
from .nodes.mask.mask_node import MaskAddNode
from .nodes.video.load_node import LoadVideoNode
from .nodes.video.save_node import SaveVideoNode
from .nodes.video.info_node import VideoInfoNode
from .nodes.video.batch_node import BatchManagerNode
from .nodes.preprocessor.midas_node import MIDAS_Depth_Map_Preprocessor
from .nodes.preprocessor.dwpose_node import DWPose_Preprocessor, AnimalPose_Preprocessor
from .nodes.preprocessor.densepose_node import DensePose_Preprocessor

NODE_CLASS_MAPPINGS = {
    "MaskAddNode": MaskAddNode,
    "ImageLoader": LoadImageNode,
    "ImageSaver": SaveImageNode,
    "ImagesSaver": SaveImagesNode,
    "ImageResize": ImageResizeNode,
    "ImageSize": ImageSizeNode,
    "WatermarkNode": WatermarkNode,
    "VideoLoader": LoadVideoNode,
    "VideoSaver": SaveVideoNode,
    "VideoInfo": VideoInfoNode,
    "BatchManager": BatchManagerNode,
    "ConstrainImageNode": ConstrainImageNode,
    "DensePosePreprocessor": DensePose_Preprocessor,
    "DWPosePreprocessor": DWPose_Preprocessor,
    "AnimalPosePreprocessor": AnimalPose_Preprocessor,
    "MiDaSDepthPreprocessor": MIDAS_Depth_Map_Preprocessor,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskAddNode": "MaskAddNode",
    "ImageLoader": "Image Load",
    "ImageSaver": "Image Save",
    "ImagesSaver": "Image List Save",
    "ImageResize": "Image Resize",
    "ImageSize": "Image Size",
    "WatermarkNode": "Watermark",
    "VideoLoader": "Video Load",
    "VideoSaver": "Video Save",
    "VideoInfo": "Video Info", 
    "BatchManager": "Batch Manager",
    "ConstrainImageNode": "Image Constrain",
    "DensePosePreprocessor": "DensePose Estimator",
    "DWPosePreprocessor": "DWPose Estimator",
    "AnimalPosePreprocessor": "AnimalPose Estimator",
    "MiDaSDepthPreprocessor": "MiDaS Depth Estimator"
}


if platform.system() == "Darwin":
    WEB_DIRECTORY = "./web"
    __all__ = ["WEB_DIRECTORY", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
else:
    __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]