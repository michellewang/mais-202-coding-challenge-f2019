#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:47:30 2019

@author: michellewang
"""

if __name__ == '__main__':
    
    # import packages
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    # load data
    df_loans = pd.read_csv('../data/loan_data.csv')
    df_home = pd.read_csv('../data/home_ownership_data.csv')
    
    # join dataframes on member_id
    df_all = df_loans.merge(df_home, how='inner', on='member_id')
    
    # compute average loan amount for each home ownership status
    df_avg = df_all.groupby('home_ownership').mean()['loan_amnt'].reset_index()
    print(df_avg.head())
    
    # start figure
    fig, ax = plt.subplots(figsize=(8, 4))
    
    labels = df_avg['home_ownership'].unique()
    x = np.arange(len(labels))
    height = df_avg['loan_amnt']
    
    # plot
    ax.bar(x, height, width=0.6)
    
    # add x-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    
    # add titles
    ax.set_xlabel('Home ownership')
    ax.set_ylabel('Average loan amount ($)')
    ax.set_title('Average loan amount per home ownership')
    
    fig.tight_layout()
    
    # save figure
#    fig.savefig('avg_loan_per_home_ownership.png', dpi=150)

    # show figure
    plt.show()