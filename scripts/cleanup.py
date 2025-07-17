import subprocess
import sys

STACK_NAME = "my-secure-bucket-stack"

def delete_stack(stack_name):
    try:
        print(f"🧹 Deleting stack: {stack_name}...\n")
        subprocess.run(
            ["aws", "cloudformation", "delete-stack", "--stack-name", stack_name],
            check=True
        )
        print(f"Delete request submitted for stack: {stack_name}")
        print("Check CloudFormation console for progress.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete stack: {e}")
        sys.exit(1)

if __name__ == "__main__":
    delete_stack(STACK_NAME)
