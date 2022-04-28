# replication-materials-sudhamshow
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6429151.svg)](https://doi.org/10.5281/zenodo.6429151)

## Research Question
Research question: Is there a significant shift in the discourse of language and user interaction on Reddit as a consequence of a mass content-moderation event?

## Preliminary Findings
Preliminary analysis of data collected from different subreddits (whose list is available in [/data/moderation.txt]
(/data/moderation.txt) indicated that out of the several subreddits of interest for which data was collected, only a 
few were worthy of analysis - those that had a discernible change (proportionally) in the amount of moderation 
events over time. 
Further analysis was only conducted on 3 months (11/2018, 12/2018 and 01/2019) on 2 subreddits that likely seems to 
show some interesting discourse in language.

The months and subreddits were selected based on the analysis of count of popular (score > 100 or < -50 (gained strong 
support or 
crticism from the community) ) post removals. 2 example plots are displayed below -

r/Politics
![png](findings/Politics.png)

r/Conservative
![png](findings/Conservative.png)

Other subreddits with high content moderation, not considered for analysis -

r/SandersForPresident (Weak evidence of mass-moderation as there's only 1 month of high moderation)
![png](findings/Sanders4Pres.png)

r/The_Donald ( Low evidence of conflict (negative posts), and moreover the subreddit has been removed from the 
platform for various reasons )
![png](findings/The_Donald.png)

One can observe a clear sign of conflict in the first 2 plots (the two plots follow each other closely). My 
hypothesis is that present setting of 
popular subreddits 
(even controversial ones) have diverse crowds. When people post controversial posts (identified by deletion by 
the moderator) that gain traction (support, by upvotes) in the community, people from the opposite ideology (hence 
probably the many downvotes) might offer a counter-argument opposing the initial posts, thus resulting in a conflict.
It is also possible that a user could go heretic and post things (or use of language) that do not align with the 
ideals of the group. These posts however get taken down as well. I am interested in further studying how this
(if) marginalised section responds or is impacted by content moderation in platforms that they can't garner support in.

Initial analysis of the most distinguising words in r/Conservative suggested an excessive use of markers of 
censorship (like 'delete', 'ban', 'removed', etc.) during 12/18 when content moderation was at its peak, compared to 
other months in the vicinity.

Wordclouds for most distinguishing words in r/Conservative for months 11/18, 12/18 and 01/19 in the same order -
<img src="findings/Consv1.png" width="250" height="250"> <img src="findings/Consv2.png" width="250" height="250"> 
<img src="findings/Consv3.png" width="250" height="250">


Further semantic analysis (Key Word in Context - KWIC) reveal that words like 'ban', 'censor' and 'delete' were used 
in a more general setting in 11/18 as opposed to using it around 'conservatives' or 'republicans' as the subject in 
12/2018 when the moderation rose (awareness of conservatives being censored).

KWIC 18/11:
<img src="findings/1811_consv_kwic.png" width="400" height="250">

KWIC 18/12:
<img src="findings/1812_consv_kwic.png" width="400" height="250">

## Relevance to Research Question
The initial analysis points to discernible differences in the use of language (both syntactic and semantic). With 
this initial proof of change in language discourse, I plan to use more sophisticated techniques to study the shift 
in language and behaviour (activity on reddit) with mass-moderation events as a treatment.

## Supplemental Code for replication

The code and data in this repository is an example of a reproducible research workflow for MACS 30200 "Perspectives on Computational Research" at the University of Chicago.

The code is written in Python 3.7.11 and all of its dependencies can be installed by running the following in the 
terminal (with the `requirements.txt` file included in this repository):

```
pip install -r requirements.txt
```

Then, you can import the `analysis` module located in this repository to reproduce the analysis in the (hypothetical) publication that this code supplements (in a Jupyter Notebook, like README.ipynb in this repository, or in any other Python script):


```python
import analysis
```

You can then use the `process_data` function in the `analysis` module to process the data and get it ready to analyze. The `plot` function will reproduce Figure 1 from the (hypothetical) publication.


```python
df = analysis.process_data('data.csv')
analysis.plot(df)
```



![png](README_files/output_3_0.png)



Alternatively, to replicate the analysis and produce all of the figures and quantitative analyses from the (hypothetical) publication that this code supplements, build and run the `Dockerfile` included in this repository via the instructions in the file).

If you use this repository for a scientific publication, we would appreciate it if you cited the [Zenodo DOI](https://doi.org/10.5281/zenodo.6429151) (see the "Cite as" section on our Zenodo page for more details).