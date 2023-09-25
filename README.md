# Nested Threshold Public Goods Game

This is the code for a behavioural experiment where people play nested threshold public goods games. 

The folder "x_paper" contains collected data and code for analysis.

## Mini Pilot Analysis

The analysis use a mixture of R and python code. The R code is mainly used for fitting statistical models, to leverage the libraries available in R. The python code is used to manipulate data and run simulations. 

## Files 

The main analysis files are listed bewlo, in a logical order that mirrors the analysis process. 

### Pilot Data

We ran a mini pilot aiming for n=24 participants. The data from that pilot, in raw form, is available in "x_paper/data/mini_pilot.csv". 

### Data Wrangling

The python file "data_wrangling.py" takes the pioot data and pivots it to a more usable format, focussed on a mem-1 strategy. 

I also pivoted that data to "data/memory_1_actions.csv". This file is easier to work with, and includes the following colums:

- participant. The participant id. 
- action. The participant's action in round t.
- round. The round number, t.
- last_action. The participant's action in the last round (t-1). 
- last_global_count. How many players contributed to Allshire last round. {0,1,2,3,4,5,6} 
- last_local_count. How many players in the participant's small group contributed to Westville last round. {0,1,2,3}
- last_kept_count. How many players in the large group defected and kept their coin last round. {0,1,2,3,4,5,6}

### Fitting a Model

The R script "h_1_pilot_analysis.R" fits logistic regression model to the pilot data. 

### Simulating behaviour

The model estimates from the R analysis are used to simulate behaviour in "simulations.py"

This is tested for prediction accuracy at the individual level against machine learnign classifiers and simple strategies in "classication.py". 

I ran simulations of 100 groups with fixed effects and 100 with mixed effects. Data is exported to "data/simmed_data_parameterised_fixed_effects_only.csv" and "data/simmed_data_parameterised_mixed_effects.csv".

The simulations are compared to the pilot data in "comparing_sims_and_pilot_data.py". 

### Plots
The plots folder contains some plots of all that. 

### Old code

There's a bunch more code in "old and messy code". It isn't well documented. 

# Testing the Experiment

Things to test:
- Players dropout - are they handled correctly?
- Group of 4 players arrive - are they grouped up? 
- Grouping is done correctly (at the game stage). 
- Group IDs match the groups. Y
- id_in_group matches the local groups. Y
- Run through game ok. Y
- Run through the entire experiments ok. 
- BEFORE deploying: Are timeouts the correct legnth of time? 




