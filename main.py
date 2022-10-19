import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
        '--append-action', action='append', dest="data", help="Can be data_5K, data_10K, data_15K, data_20K, data_30K, data_100K, data_500K, data_750K"
    )
args = parser.parse_args()

print(args.data)

list_to_dict= args.data[0].split(",")

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


# Driver code

print(Convert(list_to_dict))
def true_list(lst):
    res_list = [lst[i] for i in range(0,len(lst), 2)]
    return res_list

print(true_list(list_to_dict))

