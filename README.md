# inswhite

As rectangular shaped photos are far more common than square shaped ones, Instagram allowed users to post rectangular photos without forcing you to crop it, like what it did in its early days. However, on anyone's profile page, all posts are still displayed as 3xN squares, which means the composition of all rectangular photos is ruined.

Therefore, you may notice that many Instagram users, especially professional photographers, add a white "frame" to their rectangular photos, to make it a square. It not only makes sure the whole photo is kept as is on the profile page display but also make the profile page looks less squeezy or messy.

There are defiantly a lot of apps available in the marketplace for you to do this trick, and also many more. But I'm sure not many of them, if there is any, do not ask for your email and/or social media info. So, as I generally against download a "many-in-one" app for just one feature that I also don't use very often, I wrote a few lines of Python code, probably less than this readme, to do it for me.

So what does **inswhite** do? It simply makes a rectangular photo to be square, by adding white area to two sides - top and bottom, or left and right, depends on the orientation. At least this is what it was meant to do at first.

# inszoom

Not able to pinch to zoom? Split a photo into multiple pieces to show more details on Instagram. Each small piece is, of course, a square one filled with white space.

## Dependencies

**OpenCV** is the only external package used here.

## Installation

```
`> pip install -r requirements.txt

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
