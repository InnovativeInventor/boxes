i=0
for test_env in tests/*/* ; do
    for d in boxes/*/ ; do (cp $test_env $d/Dockerfile && cd $d); done
    cd boxes 
    for d in ./*/ ; do 
        cd $d
        monobox build || ((i++)) 
        tag=$(echo $d | tr -cd '[:alnum:]') 
        echo $tag
        dgoss run --rm -d -it $tag || ((i++))
        rm Dockerfile
        cd ..
    done
done
echo "$i"
exit $i