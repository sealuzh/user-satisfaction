## How To

Following, we describe what to do in order to replicate the results of the study.

To be able to execute the scripts, you should use:

* Python 2.7;
* Install `click` (`pip install click`) and `pandas` (`pip install pandas`);
* Install `plotly` (`pip install plotly`) to be able to run the figures and plot the results.

With the `setting.py` file you can change the destination of the folders where the results will be saved.
By default, the scripts create them in the main directory where the `main.py` file is places.

Thus, just clone the repository with
```
git clone https://github.com/giograno/replication.git
```
and move into the subfolder `script_analysis`.

### Results for RQ1
To compute the results for the first research question, run the following command:
```
python main.py code_rating
```
Use the flag `--plot` if you want to plot out the corresponding heat-maps.

### Results for RQ2
To compute the results for the second research question, run the following command:
```
python main.py user_rating
```
Again, use the flag `--plot` if you want to plot out the corresponding heat-maps.

### Results for RQ3
To compute the results for the third research question, run the following command:
```
python main.py code_feature
```
If you want, use `--plot` how explained.
