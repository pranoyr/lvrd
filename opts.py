import argparse


def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weight_path', type=str,
                        help='path to weight file')
    args = parser.parse_args()

    return args