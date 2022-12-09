#!/usr/bin/env bash

Basins=( 5 25 50 75 95 )
Sims=$(seq 1 2)
#Event_ini=(  1 101 201 301 401 )
#Event_end=( 100 200 300 400 500 )
Event_ini=(  1 11 21 31 41 )
Event_end=( 10 20 30 40 50 )

submit_tmplate="submit_template.job"

for (( j=0; j<${#Basins[@]}; j++ ))
do
	submit="submit_${Basins[$j]}.job"
	cp $submit_tmplate $submit
    for Sim in ${Sims[@]}
    do
        for Event in $(seq ${Event_ini[$j]} ${Event_end[$j]})
        do
            echo "${Basins[$j]} - $Sim - $Event"
            run_script="HMS_Run_${Basins[$j]}_${Sim}_${Event}.jy"
            cp template.jy $run_script
            sed -i -e "s/AAA/${Basins[$j]}/" -e "s/BBB/${Sim}/" -e "s/CCC/${Event}/" $run_script
            echo "srun --exclusive -n 1 hec_hms.sh -script $run_script" >> $submit
        done
    done
	sbatch $submit
done
