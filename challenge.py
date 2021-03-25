import pandas
import time

start = time.time()
dataset = pandas.read_csv("joined_dataset_final.csv", usecols=["BELNR", "NAME1", "WRBTR", "BUKRS", "BLDAT", "XBLNR", "SGTXT"])

length_dataset = len(dataset["WRBTR"])
dict_dataset = dict()

def make_string(dataset, i):
    return str(dataset["WRBTR"][i]) + "|" + str(dataset["BUKRS"][i]) + "|" + str(dataset["BLDAT"][i]) + "|" + str(dataset["XBLNR"][i])

for i in range(length_dataset):
    string_name = make_string(dataset, i)
    try:
        dict_dataset[string_name].append(i)
    except:
        dict_dataset[string_name] = [i]

all_duplicates = []
for elem in dict_dataset:
    elem_i = dict_dataset[elem]
    if len(elem_i) == 1:
        continue
    all_duplicates.extend(elem_i)

dataset.iloc[all_duplicates, :].to_csv("duplicates.csv", index = False)
print(dataset.iloc[all_duplicates, :])

print(f"It took {time.time()-start}s")

# I dont know if you need the full one or only the important ones like above
new_dataset = pandas.read_csv("joined_dataset_final.csv")
new_dataset.iloc[all_duplicates, :].to_csv("full_duplicates.csv", index = False)