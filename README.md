# Continuous benchmarking using Github Actions
## Authors ## 
* Johan Hammarstedt (johhamm@kth.se), Github: [jhammarstedt](https://github.com/jhammarstedt)
* Carl Leijonberg (carllei@kth.se), Github : [carllei](https://github.com/carllei)

## Task
This project was aimed to teach others how to setup a Github Action to create continuous benchmarking with pytest. We also added a simple visualisation with Github Pages that we walk through brefily in the tutorial. 

This will help developers easily compare benchmark results and alert on worse performance when making a new commits. The statistics from the latest run is found in `output.json` and the historical comparission table is visualized in the generated page available [here](https://jhammarstedt.github.io/Benchmarking-DevOps/). 

## Katacoda tutorial (Scheduled to be complete the latest on 30/4/2020)
We have created a katacoda tutorial that walks through every step of how to build and set up this repo. It will soon be published here.

## Description and usage
To try this project out simply fork this repository and create a commit. 

Ideally you would change the [benchmarking.py script](https://github.com/jhammarstedt/Benchmarking-DevOps/blob/master/src/benchmarking.py) since that will give different performance results. We have 2 test functions, a slower `turtle` and faster `cheetah` which are just used to test the benchmarking. So try to change:

line 22: `benchmark(turtle)` --> `benchmark(cheetah)`

Commit this, get some results, and then change back and commit again to see the difference. 

* The workflow file is found in [`.github/workflows/python.yml`](https://github.com/jhammarstedt/Benchmarking-DevOps/tree/master/.github/workflows)
* The configurations for the webpage is found in [docs](https://github.com/jhammarstedt/Benchmarking-DevOps/tree/master/docs)
* All python scrips are found in [`src`](https://github.com/jhammarstedt/Benchmarking-DevOps/tree/master/src)


### Clean the table

If you want to reset the table simply run
```./scripts/clear_table.sh```

## Easter egg hint

<details> 
  <summary>Click me for hint</summary>
  Did you collect the 🥚 from scripts?
  
  <details>
  <summary> Fun fact regarding easter egg (open after finding it) </summary>
    The author of the action did not support memes by repo owners, which would be a problem for our purpose. So I raised that
   <a href="https://github.com/deep5050/memes-on-issues-action/issues/4" target="_top">issue</a> and got a new feature merged for this tutorial 🤙
    
  </details>
</details>


## Future work
* Add support for more languages
