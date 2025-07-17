import subprocess
import os
import sys

STACK_NAME = "my-secure-bucket-stack"
TEMPLATE_FILE = os.path.join("templates", "secure-s3-bucket.yml")

def deploy_stack():
    print(f"Deploying stack: {STACK_NAME}")
    try:
        result = subprocess.run([
            "aws", "cloudformation", "deploy",
            "--stack-name", STACK_NAME,
            "--template-file", TEMPLATE_FILE,
            "--capabilities", "CAPABILITY_NAMED_IAM"
        ], check=True)
        print("Deployment successful!")
    except subprocess.CalledProcessError as e:
        print("Deployment failed. Check CloudFormation console for details.")
        sys.exit(e.returncode)

if __name__ == "__main__":
    deploy_stack()