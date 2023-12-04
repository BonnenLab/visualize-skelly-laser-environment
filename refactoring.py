
def find_walks_with_type(ID,walktype):
    loc = "/N/project/berkeley_walking/BerkeleyData/berkeley_json/"
    filesearch = f'{loc}s{str(ID)}*{walktype}*.json'
    files = glob.glob(filesearch)
    walks = [int(file.split('/')[-1].split('_')[1]) for file in files]
    walkNum = walks
    return walkNum

def load_data(ID,walkNum):
    footholds = []
    gazeGround = []
   
    for x in walkNum:
        loc = '/N/project/berkeley_walking/BerkeleyData/berkeley_pupilShadowMesh'
        data = sio.loadmat(f'{loc}/s{str(ID)}_{x}_pupilShadowMesh.mat')    
        marker,skeleton,fholds,gGround = data['markerNames'], data['shadow'], data['step_plantfoot_xyz'],data['gazeXYZ']
        hips = np.squeeze(skeleton[:,1,:])   
        footholds.append(fholds)
        gazeGround.append(gGround)

    gazeGround = np.vstack(gazeGround)
    footholds = np.vstack(footholds)
    return footholds, gazeGround

def current_distances_closest(footholds,gazeGround):

    frame_edges = np.append(np.append(1,footholds[:,0]),gazeGround.shape[0]+1)
    frames_per_foothold = np.diff(frame_edges)
    current_foothold = np.array(reduce(concat,[int(ff)*[ee] for ee,ff in enumerate(frames_per_foothold)]))

    distances = cdist(gazeGround,footholds[:,2:])
    closest_foothold = np.argmin(distances,axis=1)+1
    distances_min= np.min(distances, axis = 1)
    return current_foothold,distances,closest_foothold
def find_rel_foothold_fixation(distances,closest_foothold,current_foothold):
    distances_min= np.min(distances, axis = 1)  
    rel_foothold_fixation = np.where(distances_min > 0.4, np.nan, closest_foothold-current_foothold)
    steps = [x for x in rel_foothold_fixation if np.abs(x) < 6 and np.abs(x) > 0]
    return rel_foothold_fixation,steps

walkNum = find_walks_with_type(3,'medium')
foothold, gazeGround = load_data(3,walkNum)
current_foothold,distances,closest_foothold = current_distances_closest(footholds,gazeGround)
rel_foothold_fixation,steps = find_rel_foothold_fixation(distances,closest_foothold,current_foothold)