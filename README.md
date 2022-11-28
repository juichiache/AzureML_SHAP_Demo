# Azure Machine Learning - SHAP Model Explanations Demo
Sample code demonstrating how to use the open source SHAP package to generate model explanations within an Azure Machine Learning workspace.

## Azure Machine Learning Background

[Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/) is Microsoft’s enterprise-grade machine learning development platform which pulls together all the necessary services and resources to support data science initiatives of any scale while leveraging [MLOps best practices](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/manage/mlops-machine-learning). 

AML has been designed to meet the needs of data scientists of all skill levels – whether your preference is to develop using graphical UI tools or to build and deploy models directly in code. Using AML you can prepare data, build reusable development environments, train models, track experiments, deploy to production, and monitor performance all from a single pane of glass. This hack is designed to give you hands-on experience working inside AML to achieve all the tasks listed above.

## Environment Setup
<b>Note:</b> Recommend running the included notebooks (`UploadData.ipynb` & `GenerateSHAPExplanations.ipynb`) on an Azure Machine Learning Compute Instance using the preconfigured `Python 3.8 - AzureML` environment. These notebooks are intended to be run in sequence as listed here.
To build and run the sample notebooks here the following resources are required:
* Azure Machine Learning Workspace
* Azure Machine Learning Compute Instance