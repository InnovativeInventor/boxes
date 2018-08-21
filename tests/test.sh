i=0
test_env=$1 # Location of test Dockerfile
d=$2 # Location of box to test

echo "Using Dockerfile folder: $test_env"
for env in tests/$test_env/* ; do
    echo "Using Dockerfile $env"
    for d in boxes/** ; do (cp $env $d/Dockerfile && cd $d); done
    cd $d
    monobox build || ((i++)) 
    tag=$(echo $d | tr -cd '[:alnum:] | sed -r "s/^boxes//"') 
    echo $tag
    dgoss run --rm -d -it $tag || ((i++))
    # rm Dockerfile
    cd ..
    done
    cd ..
done
echo "$i"
exit $i