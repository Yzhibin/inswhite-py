import cv2
import math
import sys
import glob
import re
import argparse
import os


def display(img, name, x_diff, y_diff):
    cv2.namedWindow(name)
    cv2.moveWindow(name, x_diff, y_diff)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def parseColourHex(hex):
    if (hex[0] == "#"):
        hex = hex[1:]
    r = hex[0:2]
    g = hex[2:4]
    b = hex[4:6]
    rgb = [int(r, 16), int(g, 16), int(b, 16)]
    return rgb


def inswhite(imgPath, outPath, _colour, _padding, inszoom, x_portions,
             y_portions):
    padding = int(_padding)
    colour = parseColourHex(_colour)

    img = cv2.imread(imgPath)

    shape = img.shape
    h = shape[0]
    w = shape[1]

    # Landscape
    if (w > h):
        diff = w - h
        top = math.floor(diff / 2)
        btm = math.ceil(diff / 2)
        img = cv2.copyMakeBorder(img,
                                 top + padding,
                                 btm + padding,
                                 padding,
                                 padding,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)
    # Portrait
    else:
        diff = h - w
        left = math.floor(diff / 2)
        right = math.ceil(diff / 2)
        img = cv2.copyMakeBorder(img,
                                 padding,
                                 padding,
                                 left + padding,
                                 right + padding,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)

    # Wide
    if (x_portions > y_portions):
        ratio = x_portions / y_portions
        diff = (ratio - 1) * img.shape[0]
        left = math.ceil(diff / 2)
        right = math.floor(diff / 2)
        img = cv2.copyMakeBorder(img,
                                 0,
                                 0,
                                 left,
                                 right,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)

    # Tall
    elif (x_portions < y_portions):
        ratio = y_portions / x_portions
        diff = (ratio - 1) * img.shape[0]
        top = math.ceil(diff / 2)
        btm = math.floor(diff / 2)
        img = cv2.copyMakeBorder(img,
                                 top,
                                 btm,
                                 0,
                                 0,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)

    if (inszoom):
        l = math.ceil(img.shape[0] / y_portions)
        i = 0
        while i < y_portions:
            j = 0
            while j < x_portions:
                outSplit = outPath.rsplit('/', 1)
                segmentPath = outSplit[0] + '/' + str(i) + str(
                    j) + '_' + outSplit[1]
                segment = img[l * i:l * (i + 1), l * j:l * (j + 1)].copy()
                print(segmentPath)
                cv2.imwrite(segmentPath, segment)
                j += 1

            i += 1

    else:
        cv2.imwrite(outPath, img)

    # Display Image
    # display(img, 'image', -1000, -2000)
    return


def hexType(s, pat=re.compile(r"^#?[a-f0-9A-F]{6}$")):
    if not pat.match(s):
        raise argparse.ArgumentTypeError
    return s


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inPath', nargs="+")
    parser.add_argument('--colour',
                        '--color',
                        '-c',
                        type=hexType,
                        default='#FFFFFF',
                        required=False)
    parser.add_argument('--out', '-o', required=False)
    parser.add_argument('--padding', '-p', default=26, required=False)
    parser.add_argument('--mode', '-m', default='inswhite', required=False)
    parser.add_argument('--X', '-X', default=1, required=False)
    parser.add_argument('--Y', '-Y', default=1, required=False)

    args = parser.parse_args()
    return args


def main():
    args = argParser()
    inPathWildcard = args.inPath
    i = 0
    while i < len(inPathWildcard):
        curr = inPathWildcard[i]
        if (os.path.isdir(curr)):
            curr = curr + "/*"
        imgPaths = glob.glob(curr)
        for inPath in imgPaths:
            if inPath.lower().endswith(('.png', '.jpg', '.jpeg')):

                if (args.out):
                    outDir = args.out
                    if (not os.path.isdir(outDir)):
                        print(
                            'Expect a directory for "outPath". "{}" is not a directory'
                            .format(outDir))
                        exit()
                    outPath = outDir + '/inswhite-' + inPath.rsplit('/', 1)[1]
                else:
                    split = inPath.rsplit('/', 1)
                    outPath = split[0] + '/inswhite-' + split[1]

                inswhite(inPath, outPath, args.colour, args.padding,
                         args.mode == 'inszoom', int(args.X), int(args.Y))

        i += 1


main()