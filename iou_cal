def cal_iou(bbox,gbox):
    '''
    :param bbox:
    :param gbox:
    :return:
    '''
    width1,height1=abs(bbox[2]-bbox[0]),abs(bbox[3]-bbox[1])
    width2,height2=abs(gbox[2]-gbox[0]),abs(gbox[3]-gbox[1])
    x_max=max(bbox[0],bbox[2],gbox[0],gbox[2])
    y_max = max(bbox[1], bbox[3], gbox[1], gbox[3])
    x_min = min(bbox[0], bbox[2], gbox[0], gbox[2])
    y_min = min(bbox[1], bbox[3], gbox[1], gbox[3])
    iou_width=width1+width2-(x_max-x_min)
    iou_height=height1+height2-(y_max-y_min)
    if iou_width <=0 or iou_height<=0:
        iou_ratio=0
    else:
        iou_ratio=(iou_height*iou_width)/(width1*height1+width2*height2-iou_width*iou_height)

    return iou_ratio


if __name__ == '__main__':
    box1=[1,3,4,1]
    box2=[2,4,5,2]
    print(cal_iou(box1,box2))
