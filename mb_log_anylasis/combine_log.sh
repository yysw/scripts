#!/bin/bash
for date in `date -d "1 days ago" +%Y%m%d`
do
    echo $date
    find "/home/yahoo/$date" -path "*${date}-*.gz" | xargs -t -I {} cat {} >> /home/yahoo/moneyball.feature.log.$date.gz
done
