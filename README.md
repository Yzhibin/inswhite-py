# inswhite
As rectangular shaped photos are far more common than square shaped ones, Instagram allowed users to post rectangular photos without forcing you to crop it, like what it did in its early days. However, on anyone's profile page, all posts are still displayed as 3xN squares, which means the composition of all rectangular photos is ruined. 

Therefore, you may notice that many Instagram users, especially professional photographers, add a white "frame" to their rectangular photos, to make it a square. It not only makes sure the whole photo is kept as is on the profile page display but also make the profile page looks less squeezy or messy.

There are defiantly a lot of apps available in the marketplace for you to do this trick, and also many more. But I'm sure not many of them, if there is any, do not ask for your email and/or social media info. So, as I generally against download a "many-in-one" app for just one feature that I also don't use very often, I wrote a few lines of Python code, probably less than this readme, to do it for me.

So what does **inswhite** do? It simply makes a rectangular photo square, by adding white colour area to *both* sides - top and bottom, or left and right, depends on the orientation. At least this is what it is capable of for now.

## Prerequisites
**OpenCV** is the only external package used here.

## Usage
`python inswhite.py [path1] ([path2] [path3] ...)`
> path can be either specific or using wildcard. e.g. `path/to/picture.png` and `path/to/album/*` are both acceptable;
> accept 1 or more paths to target photos

## Pending Features/Changes
- Takes in a PADDING parameter for adding extra padding, which will create white areas on all 4 sides.

- Takes in colour parameter, to make inswhite not only adding white. 

- Takes in a out_path parameter, to allow user specify the output directory. Currently, processed photos are created within the same dir of the original.