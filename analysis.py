import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_mod_count(substr: str):
    num_mod = pd.read_csv("/data/moderation.txt")
    num_mod_neg = pd.read_csv('/data/moderation_neg.txt')
    X = []
    Y_pos = []
    Y_neg = []
    plt.figure(figsize=(15, 8))
    for index, file_name in num_mod.iterrows():
        if substr in file_name[0]:
            X.append(file_name[0].split('_')[0])
            Y_pos.append(file_name[1])
    for index, file_name in num_mod_neg.iterrows():
        if substr in file_name[0]:
            Y_neg.append(file_name[1])
    plt.xticks(ticks=range(len(X)), labels=X, rotation='vertical')
    plt.plot(X, np.array(Y_pos) * 2, label="(Score > 100)*2")
    plt.plot(X, Y_neg, color='red', label="Score < -50")
    plt.legend(loc="best")


def plot_word_cloud(DF: pd.DataFrame):
    import wordcloud
    import matplotlib.pyplot as plt
    temp = []
    DF['normalized_tokens'].apply(lambda x: temp.extend(x))
    wc = wordcloud.WordCloud(background_color="white", max_words=500, width=10000, height=10000, mode='RGBA', scale=
    .1).generate(' '.join(temp))
    plt.figure(figsize=(15, 10))
    plt.imshow(wc)
    plt.axis("off")


def print_kwic(DF: pd.DataFrame, kw: str):
    import nltk
    temp = []
    DF['normalized_tokens'].apply(lambda x: temp.extend(x))
    text = nltk.Text(temp)
    print(text.common_contexts([str]))
