# inswhite

Instagram used to force users to crop their photos to a square shape before posting it, but it's not the case anymore. 

Rectangular shaped photos or videos are very common on ins now. However, the display of them on user's profile page is really bad - it basically only shows a centre part of the picture as a preview so that everything is nicely in a square shape.

I built this tool simply to pad a rectangular photo to a square shaped one with some colour, most likely white, so that when my profile page is shown, the composition of my photos are not affected. With those white padding, simply looking at one photo also seems better, at least to my aesthetic choice.

I know there are apps that offer this feature, but I found many of them either ask you to purchase or to subscribe, at least to sign up. I'm not saying that there is anything wrong with that, I simply want to write my own tool to help me to do this simple task.

If you find using this is slightly tedious, which is probably very true, some automation and shortcut can help you. I personally use Apple Automator to run it and have added the Automator action as a service for image files on my mac. Hope that helps.

# inszoom

Not able to pinch to zoom? Split a photo into multiple pieces to show more details on Instagram. Each small piece is, of course, a square one filled with white space. 

## Dependencies

**OpenCV** is the only external package used here.

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python inswhite.py  [path1] ([path2] [path3] ...)
```

> path can be either specific or using wildcard. e.g. `path/to/picture.png` and `path/to/album/*` are both acceptable;
> accept 1 or more paths, with or w/o wildcard

optional flags:

```
--colour, --color, -c: colour in HEX representation, with or without "#"

--ratio, -r: the ratio of added padding to the original image. This is a preferred flag over --padding as it gives a same visual effect regardless of the pixel size of the image.

--padding, -p: width of padding, in pixels. When provided, --ratio is ignored

--out, -o: output directory, default is same as original file

--mode -m: "inszoom" or default "inswhite"

--X -X: horizontal pieces, or horizontal "ratio" if not used with inszoom mode

--Y -Y: vertical pieces, or vertical "ratio" if not used with inszoom mode
```

When none of the above optional flags is provided, it is assumed to use

` --mode inswhite --color #FFFFFF --ratio 16`
