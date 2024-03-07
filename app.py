import os

def main():
    # Read environment variables from the host
    variable1 = os.environ.get('MLFLOW_TRACKING_URI')
    variable2 = os.environ.get('HARNESS_PIPELINE_ID')

    # Echo the variables
    print(f"Variable 1: {variable1}")
    print(f"Variable 2: {variable2}")

if __name__ == "__main__":
    main()
