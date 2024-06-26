
# Directory

The data can be accessed using Quartz or BigRed200 
At this directory:
/N/project/berkeley_walking

# Navigating json and mesh files in Python
Both sets of files contain data for subject 3-10, each have ~26 walks and the walktype in file name

## Berkeley_json

Loading in the json file should result in a dictionary that looks like this

![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-20-23.png) ![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-19-52.png)


Steps_HS_TO_Stanceleg_XYZ (step number, heel strike, toe off, left or right )
![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-19-18.png)

Example of how this data is used in fixation-vs-feet
![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-23-07.png)

'rEyeBlink' contain 0's and 1's. These values were later used to create a boolean mask to find fixations.

## Berkeley_pupilShadowMesh

sio.loadmat(dir) to load mesh files in as a dictionary

Example in fixation-histograms
![alt text](https://github.com/BonnenLab/visualize-skelly-laser-environment/blob/96f3fb3fab1a789c94e092fa141f33aba864fcd4/Assets/Screenshot%20from%202024-05-06%2013-27-41.png)



## MATLAB
