import json

import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    # Load data from JSON files
    with open('LowDemandTestResult.json') as f:
        ld_data = json.load(f)
    with open('MediumDemandTestResult.json') as f:
        md_data = json.load(f)
    with open('HighDemandTestResult.json') as f:
        hd_data = json.load(f)

    # Create DataFrames
    ld_df = pd.DataFrame(ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs'])
    md_df = pd.DataFrame(md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs'])
    hd_df = pd.DataFrame(hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs'])

    # Print DataFrames (optional)
    print(ld_df)
    print(md_df)
    print(hd_df)

    # Plot boxplot
    plt.figure(figsize=(10, 6))  # Adjust height as needed
    sns.boxplot(data=[ld_df['mean'], md_df['mean'], hd_df['mean']], width=0.5)
    plt.title('BoxPlot of Jetpack startup Result')
    plt.xlabel('Runs')
    plt.ylabel('Time MS')
    plt.xticks(ticks=[0, 1, 2], labels=['LowDemand', 'MediumDemand', 'HighDemand'])
    plt.grid(True)
    plt.show()


# main()


def test():
    # Read the JSON file
    with open('LowDemandTestResult.json') as f:
        ld_data = json.load(f)
        ld_runs = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
    with open('MediumDemandTestResult.json') as f:
        md_data = json.load(f)
        md_runs = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
    with open('HighDemandTestResult.json') as f:
        hd_data = json.load(f)
        hd_runs = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']

    # Create a DataFrame from the runs data
    df = pd.DataFrame({'LowDemand': ld_runs, 'MediumDemand': md_runs, 'HighDemand': hd_runs})

    # Plot the boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, width=0.5)
    plt.title('Boxplot of Time to Initial Display')
    plt.ylabel('Time (ms)')
    plt.grid(True)
    plt.show()


test()
