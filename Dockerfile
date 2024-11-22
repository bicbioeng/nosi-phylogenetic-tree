FROM public.ecr.aws/sagemaker/sagemaker-distribution:1.11-gpu

LABEL authors="Tuyen Do" description="Docker image containing all software requirements for phylogenetic tree"
USER root

RUN apt-get update --allow-unauthenticated 
RUN apt-get install git

RUN conda install mamba -n base -c conda-forge -y

RUN mamba env create -n main-conda -f main.yaml
ENV PATH /opt/conda/envs/main-conda/bin:$PATH
RUN mamba install -n main-conda ipykernel

RUN jupyter lab --allow-root --no-browser --ip=0.0.0.0 --port=8888