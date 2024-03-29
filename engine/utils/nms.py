from abc import ABC, abstractmethod

from typing import List


class NMS(ABC):
    # TODO [Ashwin]: Check if it's worth speeding this up with MT
    # TODO [Ashwin]: Unit test this class
    
    # Notes to self [Ashwin]
    # 1. Write a separate class agnostic NMS that uses this class
    # do not try to update this class
    
    # 2. torchvision.ops.nms performs class-agnostic nms
    # So, this implementation should largely match torchvision.ops.nms
    # leaving aside minor differences, if any
    
    def __init__(self, multi_thread: bool = False, class_agnostic: bool = True) -> None:
        self.multi_thread: bool = multi_thread  # not implemented
        
        # this implementation is meant to handle only class agnostic NMS
        self.class_agnostic: bool = class_agnostic
    
    def apply_nms(self,
                  detections: List,
                  score_threshold: float,
                  iou_threshold: float) -> List:
        
        self.check_detections_class(detections=detections)
        
        if len(detections) == 0:
            return []
        
        detections = [detection
                      for detection in detections
                      if detection.objectness_score >= score_threshold]
    
        if len(detections) == 0:
            return []
        
        if self.class_agnostic is False:
            self.adjust_detections(detections, True)

        if 1:
            # Sort detections by objectness score in descending order
            detections.sort(key=lambda x: x.objectness_score, reverse=True)
            
            # for d in detections:
            #     print(d.objectness_score)
            
            selected_detections: list = []
            
            # until the pool runs out of detections...
            while len(detections) > 0:
                
                # always retain the detection with the highest score
                current_detection = detections.pop(0)

                selected_detections.append(current_detection)
                
                # check IOU of current detection with all other detections in the pool
                # discard detections from which have high overlap
                # retain detections with smaller overlap (< iou_threshold) in the pool
                remaining_detections: list = []
                for detection in detections:
                    iou: float = current_detection.intersection_over_union(detection)
                    
                    if iou < iou_threshold:
                        remaining_detections.append(detection)
                
                detections = remaining_detections
        else:
            pass

        if self.class_agnostic is False:
            self.adjust_detections(selected_detections, False)
        
        return selected_detections
    
    @abstractmethod
    def adjust_detections(self, detections, shift):
        raise NotImplementedError
    
    @abstractmethod
    def check_detections_class(self, detections):
        raise NotImplementedError