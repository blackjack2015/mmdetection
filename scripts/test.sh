
python tools/test.py \
	configs/faster_rcnn/faster_rcnn_r50_fpn_1x_car.py \
	checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
	--show-dir detectors_car

#python tools/test.py \
#    configs/detectors/detectors_cascade_rcnn_r50_1x_4k.py \
#    checkpoints/detectors_cascade_rcnn_r50_1x_coco-32a10ba0.pth \
#    --show-dir detectors_car
