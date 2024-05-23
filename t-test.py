from scipy import stats
import json
import numpy as np


def t_test():
    xml_path = '30_OP_XML_Test'
    xml_low_demand = "Startup_Files/" + xml_path + '/LowDemandTestResult.json'
    xml_medium_demand = "Startup_Files/" + xml_path + '/MediumDemandTestResult.json'
    xml_high_demand = "Startup_Files/" + xml_path + '/HighDemandTestResult.json'

    jetpack_path = '30_OP_Test'
    jetpack_low_demand = "Startup_Files/" + jetpack_path + '/LowDemandTestResult.json'
    jetpack_medium_demand = "Startup_Files/" + jetpack_path + '/MediumDemandTestResult.json'
    jetpack_high_demand = "Startup_Files/" + jetpack_path + '/HighDemandTestResult.json'

    def read_json_file(file_path):
        with open(file_path) as f:
            data = json.load(f)
            runs = data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
        return runs

    with open(xml_low_demand) as f:
        xml_ld_runs = read_json_file(xml_low_demand)

    with open(xml_medium_demand) as f:
        xml_md_runs = read_json_file(xml_medium_demand)

    with open(xml_high_demand) as f:
        xml_hd_runs = read_json_file(xml_high_demand)

    with open(jetpack_low_demand) as f:
        jetpack_ld_runs = read_json_file(jetpack_low_demand)

    with open(jetpack_medium_demand) as f:
        jetpack_md_runs = read_json_file(jetpack_medium_demand)

    with open(jetpack_high_demand) as f:
        jetpack_hd_runs = read_json_file(jetpack_high_demand)

    is_significant = 0.05

    xml_runs = [xml_ld_runs, xml_md_runs, xml_hd_runs]
    jetpack_runs = [jetpack_ld_runs, jetpack_md_runs, jetpack_hd_runs]
    i = 0
    for xml_run in xml_runs:
        print(i)
        t_statistic, p_value = stats.ttest_ind(xml_run, jetpack_runs[i])
        print(f"T-statistic: {t_statistic}")
        print(f"P-value: {p_value}")
        if p_value < is_significant:
            print("SIGNIFICANT")
        print("\n")
        i += 1


t_test()
