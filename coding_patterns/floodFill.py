# an image is represented by 2 D-ARRAY of integers, each integer reprs the 
# pixel value of the image(from 0 to 65535). Given a coordinate(sr, sc) the 
# starting pixel(row and column) of the flood fill and a pixel value new color, "flood fill the image" 
# to perform a flood fill, consider the starting pixel , plus any pixel connected 4 - directionally to the startingit rm --cached java_ubs/6666da9f-3d07-44be-beeb-a8c9a57992dcg pixel of the same color 
# as the starting pixel,plus any pixels connected 4 - directionally to those pixels (also with the same color as the starting pixel) and so on. Replace the color of all the aforementioned pixels with the newColor
#  at the end, return the modified image
# image = [[1, 1, 1], [1, 1 , 0], [1, 0, 1]] sr = 1, sc = 1, newColor = 2
# output [[2, 2, 2], [2, 2, 0], [2, 0, 1]]