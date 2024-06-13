
# Directory

The data can be accessed using Quartz or BigRed200 
At this directory:
/N/project/berkeley_walking

# Navigating json and mesh files in Python
Both sets of files contain data for subject 3-10, each have ~26 walks and the walktype in file name

## Berkeley_json

Loading in the json file should result in a dictionary that looks like this
|||
|:----------------------------------------------------------:|:----------------------------------------------------------------:|
|![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-20-23.png)|![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-19-52.png)|


Steps_HS_TO_Stanceleg_XYZ (step number, heel strike, toe off, left or right )
![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-19-18.png)

Example of how this data is used in fixation-vs-feet

```
framerate = x['framerate']
        steps = np.array(x['steps_HS_TO_StanceLeg_XYZ'])
        step_start, step_end = steps[:,0].astype(int), steps[:,1].astype(int)
        step_start_time, step_end_time = step_start / framerate, step_end / framerate
        step_frames = steps[:,0:2].astype(int)
        step_time = step_frames.T / framerate
```

'rEyeBlink' contain 0's and 1's. These values were later used to create a boolean mask to find fixations.

## Berkeley_pupilShadowMesh

sio.loadmat(dir) to load mesh files in as a dictionary

Example in fixation-histograms
```
loc = '/N/project/berkeley_walking/BerkeleyData/berkeley_pupilShadowMesh'
        data = sio.loadmat(f'{loc}/s{str(ID)}_{x}_pupilShadowMesh.mat')
        Data.append(data)    
        marker,skeleton,fholds,gGround = data['markerNames'], data['shadow'], data['step_plantfoot_xyz'],data['gazeXYZ']
        footholds.append(fholds)
        gazeGround.append(gGround)
        hips = np.squeeze(skeleton[:,1,:])
```


## MATLAB

Having problems accessing MATLAB via terminal, red desktop works: <u>https://red.uits.iu.edu</u>

Terminal Commands
`
module load matlab
matlab
`

| Input the directory in the path entry field                                                            |Access pupilshadow mesh files: BerkeleyData => berkeley_PupilShadowMesh                         |
|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
|![](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/main/Assets/matlab1.png)     |![](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/main/Assets/matlab2-1.png)|



