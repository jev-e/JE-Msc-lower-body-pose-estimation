JE-Msc-lower-body-pose-estimation
Recurrent Neural Network for predicting the lower body pose in VR from sparse trackers

Author: Jacob Evans 

Project Requirements:
-Python v.3.10.2
-Jupyter Lab 3.4.3



Project Structure:

-animations<br />
  -FBX Animations<br />
-notebooks<br />
  -RNN.ipynb: data pre-processing, model creation and training, writing results to file<br />
  -Analysis.ipynb: calculates mean absolute error and plots correlation graph based on given results directory<br />
-recordings<br />
  -complex: raw motion capture, complex dataset<br />
  -simple: raw motion capture, simple dataset<br />
  -old: all previous raw motion capture<br />
-results<br />
  -other<br />
  -run_complex: results of predicting the complex dataset<br />
  -run_simple: results of predicting the simple dataset<br />
-test_data<br />
  -simple: set of simple motion capture data<br />
  -complex :set of complex motion capture data<br />
  -old_test_data: previous training dataset <br />
-train_data<br />
  -training data CSVs<br />


 
