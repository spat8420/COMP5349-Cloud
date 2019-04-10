import sys

def update_dict(category_dict, key, value):
    if key in category_dict:
        category_dict[key].append(value)
    else:
        category_dict[key] = [value]
    return category_dict

output_file = open(sys.argv[1], "r")
#print(sys.argv[1])

category_dict = {}
for line in output_file:
    category = line.strip().split("\t", 1)[0]
    video_country =  line.strip().split("\t", 1)[1]
    category_dict = update_dict(category_dict, category, video_country)

for key in category_dict:
    print(key + " " + str(len(category_dict[key])))


