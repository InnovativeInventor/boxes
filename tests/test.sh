i=0
for d in boxes/*/ ; do (cp tests/Dockerfile $d/Dockerfile && cd $d); done
cd boxes 
for d in ./*/ ; do 
    cd $d
    monobox build || ((i++)) 
    tag=$(echo $d | tr -cd '[:alnum:]') 
    echo $tag
    dgoss run --rm -d -it $tag || ((i++))
    cd ..
done
echo "$i"
exit $i