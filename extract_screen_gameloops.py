from lib import generateJson,mkdir

import asyncio
import os
import argparse

async def main(args):
    print(args)
    mkdir(args.JsonDIR)
    mkdir(args.VideoDIR)
    observed_id=1
    cnt=0
    assert os.path.exists(args.ReplayDIR) , "Replay directory does not exist"
    for file in os.listdir(args.ReplayDIR):
        assert isinstance(int(args.NUM),int),"ERROR NUM"
        if cnt==int(args.NUM):
            break
        cnt+=1
        replay_path = f"{args.ReplayDIR}{file}"
        
        if  not os.path.exists(f'{args.JsonDIR}{file.split(".")[0]} {observed_id}.json'):
            await generateJson(replay_path,observed_id,args)
        await asyncio.sleep(3)
        if  not os.path.exists(f'{args.JsonDIR}{file.split(".")[0]} {3-observed_id}.json'):
            await generateJson(replay_path,3-observed_id,args)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--NUM', default='1', type=str)
    
    parser.add_argument('--ReplayDIR', default='E:\\proj_sc2\\replay\\playoffs\\', type=str)
    parser.add_argument('--JsonDIR', default='./apidata/', type=str)
    parser.add_argument('--VideoDIR', default='./videos/', type=str)
    
    args = parser.parse_args()
    asyncio.run(main(args))