echo "the current user is:" $(users)
echo "The date today  is: "   $(date +%D )
echo  "The time is: "  $(date +%r)
echo "My system uptime is:" $(uptime -p) 

for filename in $1
do 
   >   $filaname
done
