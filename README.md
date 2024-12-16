# File Structure

This repository verifies accessibility and functionality of NVDIA gpu on your machine using a docker container.
A `Dockerfile`, along with bash scripts to build `dockerbuild.sh` and run `dockerrun.sh` the container are included.

### _**Local Machine**_
```
/current_directory/nvda-gpu-test
├── data/
├── src/
│   ├── gpu_test.py
```

When running the container using `dockerrun.sh`, the project directory is mounted as `/workdir`. This directory is treated as a ros2 workspace.
### _**Docker Container**_
```
/workdir
├── data/
├── src/
│   ├── gpu_test.py
```

## Usage

Building and running the container

1 - Clone the repo and change directory into the repo:

`git@github.com:albud187/nvda-gpu-test.git`
`cd nvda-gpu-test`

2 - Build the container:

`sh dockerbuild.sh`

3 - Run the container:

`sh dockerrun.sh`

4 - Testing. In the container, you should be able to execute `nvtop` and `nvdia-smi`. To test pytorch (loading data on GPU), on `/workdir`, execute: 

`bash run.sh`

This will execute the `gpu_test.py` script. If successful you will see a message similar to this:
```
GPU is available!
Using GPU: NVIDIA GeForce RTX 2070
Tensor operation on GPU successful.
```
