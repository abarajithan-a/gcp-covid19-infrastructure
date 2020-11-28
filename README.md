# gcp-covid19-infrastructure
Repository for COVID19 cloud infrastructure &amp; components in Google Cloud Platform(GCP)  

This repository consists of Infrastructure-As-Code(IAC) for the Deployment Manager in Google Cloud Platform.  

**Pre-requisites:**
1. An account in Google Cloud Platform(GCP) should exist.
2. Latest version of Google Cloud SDK needs to be installed in the local machine.
3. Google Cloud SDK needs to be initalized and a default project,region,zone attributes should have been set.
4. Python version 3.7.x
5. All the required Google Component APIs should be enabled from the console under *Google Cloud Platform -> APIs & Services*

To deploy the cloud components infrastructure for the first time, run the following from command line  
`gcloud deployment-manager deployments create deploy-gcp-covid19-infrastructure --config prod-gcp-deploymentmanager.yaml`

If you to want update the already existing deployment, run the following from command line  
`gcloud deployment-manager deployments update deploy-gcp-covid19-infrastructure --config prod-gcp-deploymentmanager.yaml`

If you want to delete the deployment, run the following from command line  
`gcloud deployment-manager deployments delete deploy-gcp-covid19-infrastructure`