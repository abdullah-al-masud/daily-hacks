import argparse

def get_args(jupyter=False, show=False):
    parser = argparse.ArgumentParser()
    
    # ========================== #
    parser.add_argument('--data-dir', type=str, default='data/mRI-multi-modal', help='path to the data set root directory')
    parser.add_argument('--output-dir', type=str, default='outputs/visualization', help='output directory path')
    parser.add_argument('--stack-frame', type=int, default=3, help='number of radar frames to be stacked')
    parser.add_argument('--start-frame', type=int, default=300, help='starting frame number for visualization animation')
    parser.add_argument('--end-frame', type=int, default=400, help='ending frame number for visualization animation')
    parser.add_argument('--fps', type=int, default=2, help='frame per second for generated animation video')
    parser.add_argument('--pose-dim', type=str, default='3d', help='dimension of pose label data')
    # ========================== #

    args = parser.parse_args([]) if jupyter else parser.parse_args()
    # args.view_angle = list(map(int, args.view_angle.strip()[1: -1].split(',')))
    if show:
        print(args)
    
    return args

