import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
        "--data", dest="data", help="Can be data_5K, data_10K, data_15K, data_20K, data_30K, data_100K, data_500K, data_750K", default="data_5K"
    )
args = parser.parse_args()

print(args.data)
