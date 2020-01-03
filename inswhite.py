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


def inswhite(imgPath, outPath, _colour, _padding):
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

    # Display Image
    # display(img, 'image', -1000, -2000)
    cv2.imwrite(outPath, img)
    return

def zoomWhite (img, outPath ,colour, padding, position):

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
        if (position == 'first'):
            img = cv2.copyMakeBorder(img,
                                 padding,
                                 padding,
                                 left + padding + right + padding,
                                 0,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)
        elif(position == 'last'):
            img = cv2.copyMakeBorder(img,
                                 padding,
                                 padding,
                                 0,
                                 left + padding + right + padding,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)
        else:
             img = cv2.copyMakeBorder(img,
                                 padding,
                                 padding,
                                 0,
                                 0,
                                 cv2.BORDER_CONSTANT,
                                 value=colour)
    # Display Image
    # display(img, 'image', -1000, -2000)
    cv2.imwrite(outPath, img)
    return

def inszoom(imgPath, outPath, _colour, _padding):
    padding = int(_padding)
    colour = parseColourHex(_colour)

    img = cv2.imread(imgPath)

    shape = img.shape
    h = shape[0]
    w = shape[1]

    # Landscape
    if (w > h):
        h = h + padding
        portions = (w // h) + 1
        sectionWidth = math.ceil(w / portions)
        i = 0
        while i < portions:
            out = outPath.rsplit('/', 1)[0] + '/' + str(i) + '_' + outPath.rsplit('/', 1)[1]
            position = 'mid'
            if i == 0:
                position = 'first'
            if i == portions - 1:
                position = 'last'
            
            cropped = img[0:h, sectionWidth * i : sectionWidth * (i+1)].copy()

            zoomWhite(cropped, out, colour, padding, position)

            i += 1


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

                if (args.mode == 'inswhite'):
                    inswhite(inPath, outPath, args.colour, args.padding)
                elif (args.mode == 'inszoom'):
                    inszoom(inPath, outPath, args.colour, args.padding)
        i += 1


main()