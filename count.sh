#!/bin/sh

TEXT=$1

echo "# 更新時間カウント"
cat $TEXT | awk '{print $2}' | awk -F: '{print $1}' | sort | uniq -c | \
awk '{{OFS="\t"} {print $2,$1}}'

echo "# 更新日カウント"
cat $TEXT | awk -F- '{print $3}' | awk '{print $1}' | sort | uniq -c | \
awk '{{OFS="\t"} {print $2,$1}}'

echo "# 更新月カウント"
cat $TEXT | awk -F- '{print $2}' | sort | uniq -c | \
awk '{{OFS="\t"} {print $2,$1}}'

echo "# 更新年カウント"
cat $TEXT | awk -F- '{print $1}' | sort | uniq -c | \
awk '{{OFS="\t"} {print $2,$1}}'

echo "# 更新年月カウント"
cat $TEXT | awk -F- '{{OFS="-"} {print $1,$2}}' | sort | uniq -c | \
awk '{{OFS="\t"} {print $2,$1}}'

