import os
import json

def load_metadata(metadata_dir):
    # load existing keys
    with open(f"{metadata_dir}/keys.txt", "r") as rf:
        keys = [line.strip() for line in rf.readlines()]
    
    # load sample-indexing function (i -> sample_pth per key & which split)
    with open(f"{metadata_dir}/sample_indexing.json", "r") as rf:
        sample_indexing = json.load(rf)
    
    # if stats file exists, load
    if os.path.exists(f"{metadata_dir}/stats.json"):
        with open(f"{metadata_dir}/stats.json", "r") as rf:
            stats = json.load(rf)
    
    else:
        stats = {key: dict(num=0) for key in keys} # per key
        # for all samples
        for index in sample_indexing.keys():
            # for all keys
            for key in keys:
                # update number of samples in each key
                if key in sample_indexing[index]['paths'].keys():
                    stats[key]['num'] += 1
        
        # save stats
        with open(f"{metadata_dir}/stats.json", "w") as wf:
            json.dump(stats, wf, indent=1)
                
    
    return keys, sample_indexing, stats
        

def load_sample_paths(dataset_pth, selected_keys):    
    # load metadata
    keys, sample_indexing, stats = load_metadata(f"{dataset_pth}/.round/metadata")
    
    # prepare sample paths (& corresponding names)
    sample_pths = []
    sample_names = []
    for i in sorted(list(sample_indexing.keys())):
        skip_sample = False
        
        # for all selected key
        sample_pth_per_key = dict()
        for selected_key in selected_keys:
            # only use if selected_keys all exist within sample
            if selected_key not in sample_indexing[i]['paths'].keys():
                skip_sample = True
                break
            
            # return paths to use
            sample_pth_per_key[selected_key] = sample_indexing[i]['paths'][selected_key]
            
        
        # skip sample if required; if not, save to 'sample_pths'
        if skip_sample:
            continue
        else:
            sample_pths.append(sample_pth_per_key)
            sample_names.append(sample_indexing[i]['sample_name'])

    
    
    return sample_pths, sample_names, len(sample_pths)