import os
import os.path as osp
import cv2
import argparse


dataset_path = 'your-path-to-data'
track = 'Track2'


def check_and_create(folder_path):
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    return folder_path


def main(args, data_root):
    print(f'start {data_root}:')
    seq_list = os.listdir(data_root)

    for seq_name in seq_list:
        path_data = os.path.join(data_root, seq_name)
        path_vdo = os.path.join(path_data, 'vdo.avi')
        path_images = os.path.join(path_data, 'img1')
        check_and_create(path_images)

        vidcap = cv2.VideoCapture(path_vdo)
        success, image = vidcap.read()

        count = 1
        while success:
            path_image = os.path.join(path_images, '%06d.jpg' % count)
            cv2.imwrite(path_image, image)
            success, image = vidcap.read()
            if count % 100 == 0:
                print('Data path: %s; Frame #%06d' % (path_data, count))
            count += 1


if __name__ == '__main__':
    print("Loading parameters...")
    set_paths = ['train/S01', 'validation/S02',
                 'train/S03', 'train/S04', 'validation/S05', ]
    parser = argparse.ArgumentParser(description='Extract video frames')
    parser.add_argument('--data-root', dest='data_root', default=set_paths[0],
                        help='dataset root path')

    args = parser.parse_args()
    for set_path in set_paths:
        data_root = osp.join(dataset_path, track, set_path)
        print(data_root)
        main(args, data_root)
