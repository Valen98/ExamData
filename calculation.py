import json
import math


def main():
    path = "./androidProfiler_data.json"

    def read_json_file(file_path):
        with open(path) as f:
            return json.load(f)

    all_data = read_json_file(path)
    print(all_data)
    for data in all_data:
            print(data)
            for categories in all_data[data]:
                mean = sum(all_data[data][categories]) / len(all_data[data][categories])
                variance = sum([((x - mean) ** 2) for x in all_data[data][categories]]) / len(all_data[data][categories])
                res = variance ** 0.5
                z = 1.96
                e = z * res / math.sqrt(len(all_data[data][categories]))
                print("with category: " + categories + " E = " + str(round(e, 3)) + "\n")


main()
