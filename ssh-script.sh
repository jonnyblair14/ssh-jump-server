echo "Currently connected to $(hostname)"
echo "Select a host to connect to:"

listfile="$HOME/.ssh/config"
hosts=()

all_lines=( $(awk "/^Host /{print}" $listfile) )	# end up with a list ( "Host", "computerA", "Host", "computerB", etc )
							# so the for loop grabs the non "Host" elements in theory and puts 
for ((i=1; i<${#all_lines[@]}; i+=2)); do		# them into the hosts list to iterate through below 
	hosts+=(${all_lines[$i]})
done

index=1

len=${#hosts[@]}

while [ $index -le $len ]; do
	echo "$index. ${hosts[$(($index-1))]}"
	((index++))
done

read -p "Enter selection digit (blank to exit): " selection

if [ ${selection:--1} -eq -1 ];
then 
	exit
fi

command="ssh ${hosts[$(($selection-1))]}"

eval " $command"
