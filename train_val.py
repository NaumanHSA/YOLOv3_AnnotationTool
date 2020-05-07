import glob, os
import sys

# ============================== Config ========================================

DATA_PATH = './random'
DATA_PATH_TOWRITE = '/content/gdrive/My Drive/darknet/dataset_configuration_3/dataset/'  # Directory where the data will reside, relative to 'darknet.exe'
OUTPUT_PATH = './garbage'
TEST_PERCENTAGE = 15  # Test Image Percentage
IMAGE_FORMAT = ['jpg', 'png', 'jpeg', 'txt']  # Image Format of your data [jpg / png / jpeg]

# ============================== Config ========================================


def separate_train_val():
    images = 0
    txt_files = 0
    file_train = open('train.txt', 'w')
    file_test = open('val.txt', 'w')

    counter = 1
    index_test = round(100 / TEST_PERCENTAGE)

    for format in IMAGE_FORMAT:
        for pathAndFilename in glob.iglob(os.path.join(DATA_PATH, str("*." + format))):
            basename = os.path.basename(pathAndFilename)

            if basename.split('.')[1] != 'txt':
                if counter == index_test:
                    counter = 1
                    file_test.write(DATA_PATH_TOWRITE + basename + "\n")
                else:
                    file_train.write(DATA_PATH_TOWRITE + basename + "\n")
                    counter = counter + 1
                images += 1
            else:
                txt_files += 1

    lines_train = open('train.txt', 'r').read().split("\n")
    lines_test = open('val.txt', 'r').read().split("\n")

    print('All images present : ' + str(images))
    print('All txt files present : ' + str(txt_files))
    print('Training images separated: %s' % (len(lines_train) - 1))
    print('Validation images separated: %s' % (len(lines_test) - 1))
