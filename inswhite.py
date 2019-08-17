import cv2
import math
import sys
import glob


def display(img, name, x_diff, y_diff):
    cv2.namedWindow(name)
    cv2.moveWindow(name, x_diff, y_diff)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def inswhite(imgPath, outPath):
    PADDING = 0
    COLOR = [255, 255, 255]

    img = cv2.imread(imgPath)

    shape = img.shape
    h = shape[0]
    w = shape[1]

    # Landscape
    if (w > h):
        diff = w - h
        top = math.floor(diff / 2)
        btm = math.ceil(diff / 2)
        img = cv2.copyMakeBorder(img, top + PADDING, btm + PADDING, PADDING, PADDING, cv2.BORDER_CONSTANT, value=COLOR)
    # Portrait
    else:
        diff = h - w
        left = math.floor(diff / 2)
        right = math.ceil(diff / 2)
        img = cv2.copyMakeBorder(img, PADDING, PADDING, left + PADDING, right + PADDING, cv2.BORDER_CONSTANT, value=COLOR)

    # Display Image
    # display(img, 'image', -1000, -2000)
    cv2.imwrite(outPath, img)
    return


def main(args):
    if len(args) < 1:
        print('Provide file path to at least one image.')
        exit

    i = 0
    while i < len(args):
        imgPaths = glob.glob(args[i])
        for inPath in imgPaths:
            if inPath.lower().endswith(('.png', '.jpg', '.jpeg')):
                split = inPath.rsplit('.', 1)
                outPath = split[0] + '-inswhite.' + split[1]
                inswhite(inPath, outPath)
        i += 1

main(sys.argv[1:])