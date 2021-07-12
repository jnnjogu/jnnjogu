#write a command that gets the first line
echo "my name is " \t
 for filename in myinfo.txt
do
   head -n 2 $filename | tail -n 1
done

echo  "my school is" \t

for filename in myinfo.txt
do
tail -n 1 1
done
