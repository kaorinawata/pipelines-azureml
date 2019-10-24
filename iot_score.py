# Check core SDK version number
import azureml.core
from azureml.core import Workspace

print("SDK version:", azureml.core.VERSION)
