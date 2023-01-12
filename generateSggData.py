from lib import gData,mkdir

import json
import os
import argparse

def main(args):
    print(args)

    try:
        assert os.path.exists(args.OutputDIR) , "output directory does not exist , and make it"
    except:
        mkdir(args.OutputDIR)
    vdir=args.VideoDIR
    jsondir=args.JsonDIR
    foobar=gData()
    for file in os.listdir(jsondir):
        foobar.encodeJsonData(vdir+file[:-4]+'mp4',jsondir+file)

    with open(f'{args.OutputDIR}\\objects.json', 'w') as f:
        json.dump(foobar.objects, f)
    with open(f'{args.OutputDIR}\\attributes.json', 'w') as f:
        json.dump(foobar.attributes, f)
    with open(f'{args.OutputDIR}\\relationships.json', 'w') as f:
        json.dump(foobar.relationships, f)
    with open(f'{args.OutputDIR}\\image_data.json', 'w') as f:
        json.dump(foobar.image_data, f)
        
    with open(f'{args.OutputDIR}/objects.json','r') as f:
        objs=json.load(f)
    with open(f'{args.OutputDIR}/relationships.json','r') as f:
        rels=json.load(f)
    synsets={}
    objsdict=set()
    for img in objs:
        for o in img['objects']:
            objsdict.add(o['names'][0])
            if o['names'][0] not in synsets:
                synsets[o['names'][0]]=o['synsets'][0]
    with open(f'{args.OutputDIR}/object_list.txt','w') as f:
        for i in list(objsdict):
            f.write(i+'\n')
    with open(f'{args.OutputDIR}/object_alias.txt','w') as f:
        pass
    relsdict=set()
    for img in rels:
        for r in img['relationships']:
            relsdict.add(r['predicate'])
            if r['predicate'] not in synsets:
                synsets[r['predicate']]=o['synsets'][0]
    with open(f'{args.OutputDIR}/predicate_list.txt','w') as f:
        for i in list(relsdict):
            f.write(i+'\n')
    with open(f'{args.OutputDIR}/predicate_alias.txt','w') as f:
        pass
    with open(f'{args.OutputDIR}/attribute_synsets.json','w') as f:
        json.dump(synsets,f)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--OutputDIR', default='./generateDate', type=str)
    parser.add_argument('--JsonDIR', default='./apidata/', type=str)
    parser.add_argument('--VideoDIR', default='./videos/', type=str)
    
    args = parser.parse_args()
    main(args)