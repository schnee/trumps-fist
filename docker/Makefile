help:
	@cat Makefile

DATA?="${HOME}/Data"
PROJECT?="${PWD}/.."
GPU?=0
DOCKER_FILE=Dockerfile
DOCKER=GPU=$(GPU) nvidia-docker
BACKEND=tensorflow
PYTHON_VERSION?=3.5
CUDA_VERSION?=8.0
CUDNN_VERSION?=6
TEST=tests/
SRC?=$(shell dirname `pwd`)

build:
	docker build -t trumps-fist --build-arg python_version=$(PYTHON_VERSION) --build-arg cuda_version=$(CUDA_VERSION) --build-arg cudnn_version=$(CUDNN_VERSION) -f $(DOCKER_FILE) .

bash: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data -v $(PROJECT):/project --env KERAS_BACKEND=$(BACKEND) trumps-fist bash

ipython: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data -v $(PROJECT):/project --env KERAS_BACKEND=$(BACKEND) trumps-fist ipython

notebook: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data -v $(PROJECT):/project --net=host --env KERAS_BACKEND=$(BACKEND) trumps-fist

test: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) keras py.test $(TEST)

