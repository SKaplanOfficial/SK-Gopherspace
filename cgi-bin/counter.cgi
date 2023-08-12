#/bin/ksh
count=$(cat .cnt)
if [ -z "$count" ]
then
        count=1
else
        count=$((count + 1))
fi
echo $count > .cnt
echo "Viewed $count times and counting!"