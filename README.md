# Manipulation of Handles in Domestic Environments
## R&D Project

This repo consists of the code and documentation for the R&D topic "Manipulation of Handles in Domestic Environments"
in partial fulfillment of the [Masters degree in Autonomous Systems](https://www.h-brs.de/en/inf/study/master/autonomous-systems). The complete report can be found [here](https://github.com/njanirudh/Research-Development-HBRS/blob/master/reports/Manipulation_of_Handles__R_D_compressed.pdf).

![](/images/presentation/Manipulation_lq.gif)

### Introduction
This R&D project deals with the study of general pipeline for a robot to manipulate a handle in the domestic environment. We mainly study the two major subtasks involved ie. Perception and Manipulation.

<img src="/images/presentation/pipeline-pipeline full.png" width="800"></img>

---
### Perception 
The general perception subtask involves detection the handle and finding the pose of the handle.

<img src="/images/presentation/pipeline-perception.png" width="400">

The handle type and the handle 3D bounding box is sent to the Manipulation subtask where it is used to find the best best grasping point.

---
### Manipulation 
Manipulation subtask involves 1) finding the best grasp position on the handle and 2) depending on the handle type perform the control sequence to manipulate it.

<img src="/images/presentation/pipeline-manipulation_2.png " width="400">

#### Grasp Position Learning
The main learning component involves finding the best grasp position on the handle. This is done by using a method called a Weighted Maximum Likelihood Estimation. 

---
### Final Results
The robot "autonomously" detects the hande in its camera view and then uses the learnt model to find the best position to grasp the handle and opens the drawer.

![](/images/presentation/Manipulation_lq.gif)
