import matplotlib.pyplot as plt
from PIL import Image
import imagehash
import numpy as np
import cv2

class Phash:

    @staticmethod
    def  get_phash( image):
        grabcut = Phash.grabcut(image)
        cv2.imwrite('grabcut.jpg', grabcut)
        img = Image.open('grabcut.jpg')
        return imagehash.phash(img)

    @staticmethod
    def compare_phash( phash1, phash2):
        return phash1 - phash2

    @staticmethod
    def grabcut(image) -> np.array:
        # open image in cv2 from django
        img = image

        # use open cv grab cut algorithm to remove background

        img = image
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        h, w, c = img.shape
        rect = (int(w * 0.1), int(h * 0.1), int(w * 0.9), int(h * 0.9))
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = img * mask2[:, :, np.newaxis]
        return img

    # products must be in the form [(hash, product)]
    @staticmethod
    def phash_list(src_hash, products ) -> list:
        product_scores = []
        for product in products:
            product_scores.append((Phash.compare_phash(product[0], src_hash), product[1]))

        product_scores.sort(key=lambda x: x[0])
        return product_scores
