JE-Msc-lower-body-pose-estimation
Recurrent Neural Network for predicting the lower body pose in VR from sparse trackers

Author: Jacob Evans 

Project Requirements:
-Python v.3.10.2
-Jupyter Lab 3.4.3



Project Structure:

-animations<br />
&nbsp;-FBX Animations<br />
-notebooks<br />
&nbsp;-RNN.ipynb: data pre-processing, model creation and training, writing results to file<br />
&nbsp;-Analysis.ipynb: calculates mean absolute error and plots correlation graph based on given results directory<br />
-recordings<br />
&nbsp;-complex: raw motion capture, complex dataset<br />
&nbsp;-simple: raw motion capture, simple dataset<br />
&nbsp;-old: all previous raw motion capture<br />
-results<br />
&nbsp;-other<br />
&nbsp;-run_complex: results of predicting the complex dataset<br />
&nbsp;-run_simple: results of predicting the simple dataset<br />
-test_data<br />
&nbsp;-simple: set of simple motion capture data<br />
&nbsp;-complex :set of complex motion capture data<br />
&nbsp;-old_test_data: previous training dataset <br />
-train_data<br />
&nbsp;-training data CSVs<br />


 
