
import cv2


class PhotoshopUtil:
    @staticmethod
    def crop_transparency(input_image, output):
        image = cv2.imread(input_image, cv2.IMREAD_UNCHANGED)  # 读取图片
        box = PhotoshopUtil.get_transparency_location(image)
        result = PhotoshopUtil.cv2_crop(image, box)
        cv2.imwrite(output, result)

    @staticmethod
    def cv2_crop(im, box):
        """cv2实现类似PIL的裁剪

        :param im: cv2加载好的图像
        :param box: 裁剪的矩形，(left, upper, right, lower)元组
        """
        return im.copy()[box[1]:box[3], box[0]:box[2], :]

    @staticmethod
    def get_transparency_location(image):
        """获取基于透明元素裁切图片的左上角、右下角坐标
        :param image: cv2加载好的图像
        :return: (left, upper, right, lower)元组
        """
        # 1. 扫描获得最左边透明点和最右边透明点坐标
        height, width, channel = image.shape  # 高、宽、通道数
        assert channel == 4  # 无透明通道报错
        first_location = None  # 最先遇到的透明点
        last_location = None  # 最后遇到的透明点
        first_transparency = []  # 从左往右最先遇到的透明点，元素个数小于等于图像高度
        last_transparency = []  # 从左往右最后遇到的透明点，元素个数小于等于图像高度
        for y, rows in enumerate(image):
            for x, BGRA in enumerate(rows):
                alpha = BGRA[3]
                if alpha != 0:
                    if not first_location or first_location[1] != y:  # 透明点未赋值或为同一列
                        first_location = (x, y)  # 更新最先遇到的透明点
                        first_transparency.append(first_location)
                    last_location = (x, y)  # 更新最后遇到的透明点
            if last_location:
                last_transparency.append(last_location)

        # 2. 矩形四个边的中点
        top = first_transparency[0]
        bottom = first_transparency[-1]
        left = None
        right = None
        for first, last in zip(first_transparency, last_transparency):
            if not left:
                left = first
            if not right:
                right = last
            if first[0] < left[0]:
                left = first
            if last[0] > right[0]:
                right = last

        # 3. 左上角、右下角
        upper_left = (left[0], top[1])  # 左上角
        bottom_right = (right[0], bottom[1])  # 右下角

        return upper_left[0], upper_left[1], bottom_right[0], bottom_right[1]
