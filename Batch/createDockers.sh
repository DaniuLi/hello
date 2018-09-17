#!/bin/bash  
  
i=0  
  
until [[ "$i" -gt 5 ]]    #大于5 
do  
    docker run -d --net my-net 10.42.123.13:5000/centos-cpe
    let "i++"  
done  