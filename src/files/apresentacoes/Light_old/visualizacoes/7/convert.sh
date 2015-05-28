for i in *.$1
do
    filename=$(basename "$i" $1)
    python csv2pairs.py $i 0 1 ' '  > $filename
done
