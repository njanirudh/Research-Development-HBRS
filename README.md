# Manipulation of Handles in Domestic Environments
## R&D Project

This repo consists of the code and documentation for the R&D topic "Manipulation of Handles in Domestic Environments"
in partial fulfillment of the [Masters degree in Autonomous Systems](https://www.h-brs.de/en/inf/study/master/autonomous-systems)

### Introduction
This R&D project deals with the study of general pipeline for a robot to manipulate a handle in the domestic environment. We mainly study the two major subtasks involved ie. Perception and Manipulation.

<img src="/images/presentation/pipeline-pipeline full.png" width="800">

---
### Perception 
The general perception subtask involves detection the handle and finding the pose of the handle.

<img src="/images/presentation/pipeline-perception.png" width="400">


---
### Manipulation 
Manipulation subtask involves 1) finding the best grasp position on the handle and 2) depending on the handle type perform the control sequence to manipulate it.

<img src="/images/presentation/pipeline-manipulation_2.png " width="400">

The main learning component involves finding the best position to grasp a handle.
---
### Final Results
The robot "autonomously" detects the hande in its camera view and then uses the learnt model to find the best position to grasp the handle and opens the drawer.
