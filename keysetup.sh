listfile="./server-list.txt"
lines=($(cat $listfile))
index=1
len=${#lines[@]}
while [ $index -le $len ]; do
	eval "ssh-keygen -t ed25519 -f ~/.ssh/${lines[$(($index-1))]}_from_$(hostname) -C \"${lines[$(($index-1))]} from $(hostname) Gen Apr26\""
	echo "${lines[$(($index-1))]}"
	((index++))
done
