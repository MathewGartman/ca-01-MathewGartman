"""ca_01.py: Starter file to run homework 1"""

__author__ = "Shishir Shah"
__version__ = "1.0.0"
__copyright__ = "Copyright 2022 by Shishir Shah, Quantitative Imaging Laboratory (QIL), Department of Computer  \
                Science, University of Houston.  All rights reserved.  This software is property of the QIL, and  \
                should not be distributed, reproduced, or shared online, without the permission of the author."

import sys
import matplotlib.pyplot as plt
from COSC2306 import MyImage
import logging


def image_display(image):
    if image.get_channels() == 3:
        plt.imshow(image.get_image_data())
        plt.axis('off')
        plt.show()
    else:
        plt.imshow(image.get_image_data(), cmap='gray', vmin=0, vmax=255)
        plt.axis('off')
        plt.show()
    return


def main():
    """ The main function that parses input arguments, calls the appropriate
     method and writes the output image"""

    # Initialize logging
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="output/logfile.log",
                        filemode="w",
                        format=Log_Format,
                        level=logging.INFO)
    logger = logging.getLogger()
    # handler = logging.FileHandler('output/logfile.log')
    # logger.addHandler(handler)
    logger.info('Logging initialized.')

    # Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the input image", metavar="IMAGE")

    parser.add_argument("-d", "--display", dest="display",
                        help="specify if images should be displayed", metavar="DISPLAY")

    args = parser.parse_args()

    # Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        logger.error('Input file name not specified.')
        sys.exit(1)
    if args.display is None or int(args.display) > 1:
        print("Please specify if images should be displayed or now")
        print("use the -h option to see usage information")
        logger.error('Image display option not correctly specified.')
        sys.exit(1)
    else:
        display = int(args.display)
        outputDir = 'output/'
        # Initialize image of type MyImage
        myimage = MyImage.MyImage()
        # Load Image specified in input argument
        try:
            myimage.load_image(args.image)
            logger.info('Image loading succeeded.')
        except:
            logger.error('Error loading image.')
            sys.exit(1)
        if display == 1:
            image_display(myimage)
        # Save Image
        output_image_name = outputDir + 'input_image' + '.ppm'
        try:
            myimage.save_image(output_image_name)
            logger.info('Image saving succeeded.')
        except:
            logger.error('Error saving image.')
            sys.exit(1)

        # Test image operations
        try:
            processed_image = myimage.color_to_gray()
            assert (processed_image != None)
            logger.info('Color to gray operation succeeded.')

        except:
            logger.error('Error in converting image to gray scale.')
            sys.exit(1)
        if display == 1:
            image_display(processed_image)
        output_image_name = outputDir + 'gray_image' + ".pgm"
        processed_image.save_image(output_image_name)

        try:
            t = processed_image.threshold()
            threshold_value = t[0]
            thresholded_image = t[1]
            assert(thresholded_image != None)
            message = 'Threshold value estimated is ' + str(threshold_value)
            logger.info(message)
            logger.info('Image threshold operation succeeded.')

        except:
            logger.error('Error in thresholding image.')
            sys.exit(1)
        if display == 1:
            image_display(thresholded_image)
        output_image_name = outputDir + 'binary_image' + ".pgm"
        thresholded_image.save_image(output_image_name)

        # Test another image operations
        try:
            rotated_image = myimage.rotate_image(55)
            assert(rotated_image != None)
            logger.info('Image rotation operation succeeded.')
        except:
            logger.error('Error in rotating image.')
            sys.exit(1)
        if display == 1:
            image_display(rotated_image)
        output_image_name = outputDir + 'rotated_image' + ".pgm"
        rotated_image.save_image(output_image_name)

        # Test another image operations
        try:
            rotated_image = myimage.rotate_image_inv(55)
            assert(rotated_image != None)
            logger.info('Image rotation with inverse mapping operation succeeded.')
        except:
            logger.error('Error in rotating image with inverse mapping.')
            sys.exit(1)
        if display == 1:
            image_display(rotated_image)
        output_image_name = outputDir + 'rotated_image_inv' + ".pgm"
        rotated_image.save_image(output_image_name)

if __name__ == "__main__":
    main()
