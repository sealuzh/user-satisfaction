# Replication Package

This is the replication package for the paper: 

#### Investigating the Criticality of User Reported Issues through Their Relations with App Rating.

### Dataset

We make available all the data we used to carry out our study. In particular, we share the list of the apks, the entire set of reviews mined, the extracted sentences together with both the users and the code quality metrics computed. 

The list of the available CSV files is the following:

* A [file][versions] reporting the **list of the analyzed apps**; every app has the indication of the version, the release date, as well an unique ID; 
* A [file][reviews] reporting the **set of the reviews** mined. In this CSV file we provide the following fields. In particular, the lattest refer to the unique ID of the apk showed in the CSV above;
* A [file][sentences] reporting all the **sentences** extracted from the set of mined reviews. For each sentences we report the unique ID of the corresponding review, the text of the sencence, the intention and the topic that it refers to;
* A [file][user-metrics] with the list of the computed **user metrics**. We reported in this file the ID version of all the apks along with the extracted metrics. It is worth to notice that the CSV reports also the absolute values for each intention and topic; however, four our analysis, we relied only on the relative values;
* A [file][code-metrics] for the computed **code metrics**. Again, we report the each apk its unique ID together with the extracted factors.

### Heat-maps

In order to support the analysis proposed in our paper, we report the heat-maps employed for our [RQ1](rqs/rq1.md) and [RQ2](rqs/rq2.md). 

### Crawling Tool

To mine the user reviews from the Play Store we relied on the crawling tool made available with the paper *Android Apps and User Feedback: a Dataset for Software Evolution and Quality Improvement*, available at [this link](https://github.com/sealuzh/user_quality/tree/master/tools). The zip contains the jar, an example of configuration file and a README that explain how to use it.

### Quality Metrics Extractors

In order to calculate the quality metrics listed in the paper, we relied on Python scripts developed for a previous work (see Crawling Tool section) available at [this link](https://github.com/sealuzh/user_quality/tree/master/code_metrics_scripts).

### Employed script

We also share the python script we use to calculate all the correlations and plot the images. They are available at the following [link][script]

[versions]: https://github.com/sealuzh/user-satisfaction/blob/master/csv/versions.csv
[reviews]: https://github.com/sealuzh/user-satisfaction/blob/master/csv/reviews.csv
[sentences]: https://github.com/sealuzh/user-satisfaction/blob/master/csv/sentences.csv
[user-metrics]: https://github.com/sealuzh/user-satisfaction/blob/master/csv/user_metrics.csv 
[code-metrics]: https://github.com/sealuzh/user-satisfaction/blob/master/csv/code_metrics.csv
[git]: https://github.com/sealuzh/user-satisfaction
[script]: https://github.com/sealuzh/user-satisfaction/tree/master/script_analysis

## Main Contributors

[Giovanni Grano](https://github.com/giograno) - (University of Zurich)

[Sebastiano Panichella](https://github.com/panichella) - (University of Zurich)

[Andrea di Sorbo](https://github.com/adisorbo) - (University of Sannio)

[python]: https://github.com/giograno/replication/tree/master/script_analysis
[raw]: https://github.com/giograno/replication/tree/master/csv
[topic]: https://github.com/giograno/replication/tree/master/topic_distribution
