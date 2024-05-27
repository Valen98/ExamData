from scipy import stats
import json

is_significant = 0.05


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


def low_cpu():
    xml = [20, 17.8, 17, 15, 17, 21, 19.8, 17, 20, 17.6, 21.8, 17.7, 20, 17, 16.9, 16, 18, 17, 20.9, 20.7, 18.9, 20.9,
           16.9, 17, 22, 17.9, 20, 18, 20]
    jetpack = [16.3, 16.9, 18, 21.8, 20.9, 21.7, 21.9, 17.9, 20.8, 18.9, 16.9, 21, 20.9, 21.8, 19.4, 19.6, 21.2, 22, 18,
               18.9, 16.9, 21, 20.6, 19.8, 17.9, 19.6, 17.9, 17, 18.5, 19.9]
    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("Low cpu: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def low_memory():
    xml = [55.8, 55.7, 55.8, 55.7, 210, 55.7, 55.7, 55.7, 55.7, 116, 57.3, 334, 57.4, 57.4, 57.4, 57.3, 211, 57.4,
           57.4, 57.4, 57.3, 57.4, 57.5, 64.4, 57.4, 328, 57.4, 57.4, 57.4]
    jetpack = [57.3, 57.1, 57.0, 57.0, 265, 57.0, 57.1, 57.1, 57.1, 57.1, 57.4, 221, 57.5, 57.5, 57.5, 57.4, 57.5, 57.5,
               57.5, 57.5, 221, 57.6, 57.6, 57.6, 57.6, 57.5, 57.6, 57.6, 57.6, 341]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("Low memory: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def low_battery():
    xml = [58000, 373000, 314000, 119000, 120000, 105000, 60000, 91000, 76000, 61000, 51000, 106000, -21000, 111000,
           97000, 131000, -61000, 263000, 10000, 81000, 84000, -44000, 154000, -16000, 70000, 77000, 46000, 101000,
           -34000]
    jetpack = [89000, 172000, -142000, 85000, 24000, 73000, 82000, -51000, -43000, 94000, 148000, 94000, 78000, 115000,
               94000, 66000, 119000, 126000, 74000, 131000, 105000, 26000, 99000, 86000, 89000, 70000, 74000, 99000,
               -18000, 0]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("Low battery: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def medium_cpu():
    xml = [6.8, 19, 22.5, 20.1, 21.9, 20.9, 19.6, 22, 21.8, 20.4, 20.5, 19.9, 19, 16.9, 18.8, 20.7, 21.8, 19.6, 20.4,
           16.6, 19.9, 20.2, 20.4, 19, 25, 21.9, 20.4, 21.1, 19.8]
    jetpack = [37.1, 28.8, 40.7, 34.9, 36, 39.6, 40.6, 39, 31.8, 29, 31.7, 37.4, 37.8, 36.2, 33.7, 41.3, 34.7, 33.9,
               38.4, 32.9, 35.8, 35.6, 38.7, 38.9, 44.9, 34.5, 37, 42.4, 42.9, 43.2]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("medium cpu: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def medium_memory():
    xml = [336, 340, 341, 339, 342, 337, 339, 334, 335, 337, 342, 338, 340, 340, 338, 337, 336, 337, 335, 335, 57.7,
           336, 335, 334, 336, 335, 336, 335, 340]
    jetpack = [441, 826, 878, 758, 57.7, 57.6, 57.7, 134, 345, 345, 690, 689, 730, 898, 57.9, 57.8, 57.9, 57.9, 229,
               345, 694, 688, 898, 57.9, 57.9, 57.8, 57.9, 136, 346, 690]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("medium memory: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def medium_battery():
    xml = [-234000, -228000, 3000, 85000, 218000, 28000, 125000, 101000, 74000, 156000, 251000, 107000, 247000, 13000,
           52000, 44000, 102000, 109000, 241000, 93000, -127000, 362000, 131000, 228000, 85000, 144000, 91000, 86000,
           59000]
    jetpack = [241000, 205000, 97000, 85000, 96000, 44000, 16000, 81000, 73000, 87000, 69000, 72000, 103000, 98000,
               118000, 96000, 120000, 81000, 84000, 42000, 103000, 116000, 133000, 114000, 99000, 101000, 164000,
               100000, 131000, 96000]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("medium battery: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def high_cpu():
    xml = [21.9, 22, 21.4, 21.3, 20.6, 19, 21.9, 20, 21.5, 20.7, 20.7, 20.3, 22.6, 21.6, 21, 22.7, 21.4, 21.6, 21.4,
           21.9, 20.9, 21.9, 20, 22.6, 20.9, 19.9, 21, 22.9, 21.7, 21.6]
    jetpack = [19.7, 21.6, 25, 25, 29, 24.6, 31.6, 21.4, 27.9, 28.9, 22.4, 24.7, 20, 22.5, 37, 23.6, 37, 26.9, 37, 25,
               24.4, 25, 29.5, 26.9, 37, 37, 37, 25, 25, 37]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("high cpu: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def high_memory():
    xml = [351, 339, 336, 57.9, 335, 334, 333, 338, 337, 335, 337, 340, 58.1, 338, 58.1, 341, 335, 340, 336, 346, 58,
           335, 335, 338, 332, 58, 118, 58.2, 336, 334]
    jetpack = [227, 227, 348, 440, 535, 881, 58.2, 58.2, 58.2, 58.2, 58.2, 320, 341, 438, 573, 58.3, 58.4, 58.4, 58.4,
               228, 346, 435, 438, 533, 58.4, 58.3, 58.4, 227, 349, 440]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("high memory: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


def high_battery():
    xml = [121000, 205000, 87000, 93000, 110000, 274000, 41000, 117000, 115000, 86000, 120000, 124000, 237000, 99000,
           110000, 88000, 108000, 134000, 163000, 241000, 90000, 0, 111000, 124000, 60000, 235000, 34000, 101000, 98000,
           83000]
    jetpack = [257000, 100000, 89000, 98000, 134000, 111000, 122000, 377000, 211000, 336000, 418000, 348000, 355000,
               425000, 417000, 377000, 397000, 391000, 318000, 413000, 453000, 399000, 303000, 456000, 450000, 389000,
               418000, 409000, 240000, 340000]

    t_statistic, p_value = stats.ttest_ind(xml, jetpack)
    print("high battery: ")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")
    if p_value < is_significant:
        print("SIGNIFICANT")
    print("\n")


low_cpu()
low_memory()
low_battery()
medium_cpu()
medium_memory()
medium_battery()
high_cpu()
high_memory()
high_battery()
t_test()
