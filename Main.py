import json

import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    # Read the JSON file
    with open('LowDemandTestResult_Windows11.json') as f:
        ld_data = json.load(f)
        ld_runs = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
    with open('MediumDemandTestResult_Windows11.json') as f:
        md_data = json.load(f)
        md_runs = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
    with open('HighDemandTestResult_Windows11.json') as f:
        hd_data = json.load(f)
        hd_runs = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']

    # Create a DataFrame from the runs data
    df = pd.DataFrame({'LowDemand': ld_runs, 'MediumDemand': md_runs, 'HighDemand': hd_runs})

    # Plot the boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, width=0.5)
    plt.title('Boxplot of Jetpack Compose Startup Time')
    plt.ylabel('Time (ms)')
    plt.grid(True)
    plt.show()


main()


