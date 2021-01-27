Using Dask and AWS Fargate with Amazon SageMaker Jupyter Notebooks
===================================================================

This example uses AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook and AWS Fargate cluster for using Dask for distributed computation over large data volumes.

There are several Jupyter notebooks showing examples of how to work with data directly from S3. The notebooks show examples of how to pull a 2D or 3D variable from a dataset and visualize it. Additionally, the notebooks show how to extract a time series of a variable from a location.

### Getting started

[![cloudformation-launch-stack](cloudformation/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=dask&templateURL=https://s3.amazonaws.com/docs.opendata.aws/cloudformation/dask-fargate.yaml)

1. Launch the stack, by default it will be in the `us-east-1` region (since that is the location of most of the weather & climate data) but you can change it to any region you prefer.

![architecture](cloudformation/cloudformation_1.png)

2. On the Parameters page, enter your `DaskWorkerGitToken` which is a GitHub OAuth Token. See below for how to get one if you don't have it. You can leave all the other parameters alone for now. Hit the `next` button.

If you don't have a GitHub OAuth Token you can generate one. The AWS services require a GitHub OAuth token to be able to build the Docker container image for the Dask worker & scheduler nodes. To generate the token go to [https://github.com/settings/tokens](https://github.com/settings/tokens). It is enough for the token to only have `public_repo` permissions.

![architecture](cloudformation/cloudformation_2.png)

3. Hit `next` next on this page as no input or changes are necessary.

![architecture](cloudformation/cloudformation_3.png)

4. Check that you understand this will create IAM resources. Hit the `next` button to start stack creation.

![architecture](cloudformation/cloudformation_4.png)

5. Wait for the stack to finish creating. The last item in the events will be the name of your stack with CREATE_COMPLETE when it has successfully finished. This can take 10s of minutes to finish. Then navigate to the `Outputs` tab for the link to your Jupyter Notebook.

![architecture](cloudformation/cloudformation_5.png)

### Jupyter Notebook

The Jupyter notebook environment will be set up with a kernel called `conda_daskpy3` which will contain the matching software for the dask-workers. 

### Architecture

![architecture](cloudformation/architecture.png)
