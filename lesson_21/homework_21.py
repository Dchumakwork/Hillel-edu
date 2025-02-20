import logging
from datetime import datetime, timedelta

file_for_analysis = "hblog.txt"

logging.basicConfig(
    filename='hb_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

filter_value = "Key TSTFEED0300|7E3E|0400"

filtered_log = []
with open(file_for_analysis, 'r', encoding="utf-8") as file:
    for line in file:
        if filter_value in line:
            timest_index = line.find("Timestamp ")
            timest = line[timest_index + 10: timest_index + 18]
            timest = datetime.strptime(timest, "%H:%M:%S")
            filtered_log.append((timest, line.strip()))

for i in range(0, len(filtered_log)-1):
    heartbeat = filtered_log[i][0] - filtered_log[i+1][0]
    if timedelta(seconds=33) > heartbeat > timedelta(seconds=31):
        logging.warning(f"WARNING: Pay attention to the heartbeat interval: {heartbeat.seconds} at {filtered_log[i][0].time()}")
    elif heartbeat > timedelta(seconds=33):
        logging.error(f"ERROR: Pay attention to the heartbeat interval: {heartbeat.seconds} at {filtered_log[i][0].time()}")

print(f'File {file_for_analysis} is analyzed, results in "b_test.log"')
