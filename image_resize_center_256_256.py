# -*- coding: utf-8 -*-
import glob
import os
from PIL import Image

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
def resize(path):
    img = Image.open(path)
    img = crop_center(img, min(img.size), min(img.size))
    img = img.resize((256, 256))
    return img

def bundle_resize(dir):
    path_list = glob.glob(dir + '/*')
    name_list = []
    ext_list = []

    for i in path_list:
        file = os.path.basename(i)
        name, ext = os.path.splitext(file)
        name_list.append(name)
        ext_list.append(ext)

        #予め保存先のフォルダを作成しておき、絶対パスでそのフォルダを指定
        out_path = os.path.join(*['./', name + ext])

        img = resize(i)
        img.save(out_path, quality=95)
    return

#絶対パスでリサイズしたい画像が入ったフォルダを指定
bundle_resize('./')
