import sys
import csv

if(len(sys.argv) != 3):
    sys.exit("Invalid arguments")

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w+")
reader = csv.reader(input_file)
i = 0
for line in reader:
    #print(line)
    #video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,comment_count,ratings_disabled,video_error_or_removed,country
    if (i != 0):
        # Check that the line is of the correct format
        # If line is malformed, we ignore the line and continue to the next line
        category = line[3]
        video_id = line[0]
        country = line[11]
        value = '' + video_id + ' ' + country
        #print(len(line))

        #for tag in tags:
            # In hadoop streaming, the output is sys.stdout, thus the print command
        output_file.write("{}\t{}\n".format(category, value))

    i += 1