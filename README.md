JE-Msc-lower-body-pose-estimation
Recurrent Neural Network for predicting the lower body pose in VR from sparse trackers

Author: Jacob Evans 

Project Requirements:
-Python v.3.10.2
-Jupyter Lab 3.4.3



Project Structure:

-animations
  -FBX Animations
-notebooks
  -RNN.ipynb: data pre-processing, model creation and training, writing results to file
  -Analysis.ipynb: calculates mean absolute error and plots correlation graph based on given results directory
-recordings
  -complex: raw motion capture, complex dataset
  -simple: raw motion capture, simple dataset 
  -old: all previous raw motion capture
-results
  -other
  -run_complex: results of predicting the complex dataset
  -run_simple: results of predicting the simple dataset
-test_data
  -simple: set of simple motion capture data
  -complex :set of complex motion capture data
  -old_test_data: previous training dataset 
-train_data
  -training data CSVs


 
