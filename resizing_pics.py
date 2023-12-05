import cv2 as cv
import os


def resizing_images(dir_path:str) -> None:
    '''Resizes all images in particular folder'''
    for path_img in os.listdir(dir_path):
        path = os.path.join(dir_path,path_img)
        img = cv.imread(path)
        print(f"{path} : resized!")
        img = cv.resize(img, (int(img.shape[1] * .75), int(img.shape[0] * .75)))


        # Saving results
        cv.imwrite(f"../beerBot_DATA/pics/resized/{path_img}",img)


dir = "../beerBot_DATA/pics/all_beers_full_size/"
resizing_images(dir)

