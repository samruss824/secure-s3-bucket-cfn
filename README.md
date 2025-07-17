# Secure S3 Bucket Project

This project demonstrates how to deploy a secure AWS S3 bucket using CloudFormation with best practices such as blocking public access and enabling server-side encryption.

## Features

- Creates an S3 bucket with a unique name including AWS Account ID and Region
- Blocks all public access (ACLs and policies)
- Enables server-side encryption (AES256)
- Uses CloudFormation for infrastructure as code
- Includes deployment scripts for **Windows (.bat)** and **Python (cross-platform)**

## Prerequisites

- AWS CLI configured with appropriate permissions
- Python 3.x installed (for the Python deploy script)
- AWS account with CloudFormation and S3 access
- Git installed for version control

## Deployment

### 1. Clone this repository:
   ```bash
   git clone https://github.com/samruss824/secure-s3-bucket-cfn.git
   cd secure-s3-bucket-cfn
   ```
   
### 2. Deploy the CloudFormation stack:
   You have multiple options to deploy the secure S3 bucket:

#### Option A: Using the Python script (cross-platform)
```bash
python scripts\deploy.py
```
    
#### Option B: Using the Windows batch script
```bash
./scripts/deploy.bat
```

#### Option C: Manually using the AWS CLI
```bash
aws cloudformation deploy --stack-name my-secure-bucket-stack --template-file templates/secure-s3-bucket.yml --capabilities CAPABILITY_NAMED_IAM
```

## Repository Structure
templates/
└── secure-s3-bucket.yml     # CloudFormation template for secure S3 bucket

scripts/
├── deploy.bat               # Deployment script for Windows
└── deploy.py                # Cross-platform Python deployment script

README.md                    # Project overview and instructions
.gitignore                   # Git ignore rules


## Future Enhancements
- Add lifecycle policies for object management
- Integrate Lambda functions for compliance monitoring
- Automate deployments with GitHub Actions
- Add Tines integration for workflow automation

## Author
[Sam Russell] – <russell-s@comcast.net>
[GitHub Profile](https://github.com/samruss824)