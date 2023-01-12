import matplotlib.pyplot as plt
import skvideo
import argparse
import os

def main(args):
    for idx,v in enumerate(os.listdir(args.VideoDIR)):
        for n,i in enumerate(skvideo.io.vread(v)):
            plt.imsave(f'{args.OutputDIR}{idx}_{n}.jpg',i)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
   
    parser.add_argument('--VideoDIR', default='./videos/', type=str)
    parser.add_argument('--OutputDIR', default='./testimg/', type=str)
    
    args = parser.parse_args()
    main(args)