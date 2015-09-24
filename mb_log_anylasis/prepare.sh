#!/bin/sh
log_dir=$1
FILES=`ls $log_dir/*-*`
#FILES=`ls ./$log_dir/vespa.*`
current_time=`date +"%Y%m%d%H%M%S"`
result_dir=formated.data
if [ -d "$result_dir" ]
then
    mv  $result_dir $result_dir.$current_time
fi
mkdir $result_dir

for f in $FILES
do
    echo "Processing $f"
        for kw in mb.latency mb.url serving.latency up.latency res.count adCount
    do
        cat $f | grep $kw | awk -F "[" '{print "["$2}' >> $result_dir/$kw
    done
done

