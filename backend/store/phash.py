import matplotlib.pyplot as plt
from PIL import Image
import imagehash
import numpy as np
import cv2

class Phash:


    def get_phash(self, image):
        grabcut = self.grabcut(image)
        cv2.imwrite('grabcut.jpg', grabcut)
        img = Image.open('grabcut.jpg')
        return imagehash.phash(img)

    def compare_phash(self, phash1, phash2):
        return phash1 - phash2

    def grabcut(self, image):
        # use open cv grab cut algorithm to remove background
        img = cv2.imread(image)
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        h, w, c = img.shape
        rect = (int(w * 0.1), int(h * 0.1), int(w * 0.9), int(h * 0.9))
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = img * mask2[:, :, np.newaxis]
        return img