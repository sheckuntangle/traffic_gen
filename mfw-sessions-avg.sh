#!/bin/ash

# variables
start_time=$(sed '2q;d' /tmp/session_count_dates.log)
end_time=$(sed 'x;$!d' /tmp/session_count_dates.log)
high_sessions=$(cat /tmp/session_count.log  | sort -n -k1.2 | sed '$!d')
low_sessions=$(cat /tmp/session_count.log  | sort -n -k1.2 | sed -n 1p)
total_sessions=$(awk '{s+=$1} END {print s}' /tmp/session_count.log)
number_of_sessions=$(wc -l /tmp/session_count.log | cut -d " " -f 1)
average_sessions=$(echo "scale=4; $total_sessions/$number_of_sessions" | bc -l)
load_total=$(grep "Load Averages" /tmp/session_count_dates.log | awk -F'[, ]' '{print $5}' | awk '{s+=$1} END {print s}')
load_count=$(grep "Load Averages" /tmp/session_count_dates.log | wc -l)
load_average=$(echo "scale=4; $load_total/$load_count" | bc -l)

# echo title Session Summary
echo "Session Summary"

# echo times
echo "Start Time: $start_time"
echo "End Time: $end_time"
echo "Elapsed Time: $load_count minutes"

# echo session counts
echo "High Session Count: $high_sessions"
echo "Low Session Count: $low_sessions"
echo "Average Session Count: $average_sessions"

# echo load average
echo "CPU Load Average: $load_average"