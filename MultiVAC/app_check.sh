#"!/bin/bash
line=`curl -s -X POST -d data="Entropy is irreversible!" http://localhost:5000/multivac/data`

if [[ "$line" =~ .*MultiVAC.* ]]
then
echo ok
else echo 'something is wrong'
exit 1
fi

del=`curl -s -X DELETE http://localhost:5000/multivac/zzz/`

if [ $del == "Deleted!" ]
then echo ok
else echo 'something is wrong with the /zzz/ endpoint'
exit 1
fi

#get=`curl -s -X GET http://localhost:5000/multivac`

#if [ "$get" ]
