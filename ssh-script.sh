echo "Connected to $(hostname)"
echo "Select a host to connect to:"
listfile="./server-list.txt"
lines=($(cat $listfile))
index=1
len=${#lines[@]}
while [ $index -le $len ]; do
	echo "$index. ${lines[$(($index-1))]}"
	((index++))
done

read -p "Enter selection digit (blank to exit): " selection

if [ ${selection:--1} -eq -1 ];
then 
exit
fi

command="ssh ${lines[$(($selection-1))]}"

eval " $command"
