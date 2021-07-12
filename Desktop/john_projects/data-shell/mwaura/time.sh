# the code must be able to tell the date and time
#  script should list all logged in users
# show system uptime

echo "the current user is:" $(users)
echo "The date today  is: "   $(date +%D )
echo  "The time is: "  $(date +%r)
echo "My system uptime is:" $(uptime -p) 

for filename in $1
do 
   >  less $filename
done
