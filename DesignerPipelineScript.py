
# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from matplotlib import pyplot as plt

# The entry point function MUST have two input arguments.
# If the input port is not connected, the corresponding
# dataframe argument will be None.
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):

    # Execution logic goes here
    # Install SHAP manually
    import os
    os.system(f"pip install shap==0.37")
    import shap
    print(shap.__version__)

    # Rename loaded dataframes
    training_df = dataframe1
    testing_df = dataframe2

    # Define target column
    target_column = 'MEDV'

    # Split into X & y components for train/test
    X_train = training_df.drop(columns=[target_column])
    y_train = training_df[[target_column]]

    X_test = testing_df.drop(columns=[target_column])
    y_test = testing_df[[target_column]]

    # Initialize and train model
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    # Get Run Context for file upload
    from azureml.core import Run
    run = Run.get_context(allow_offline=True)

    # Generate SHAP summary values
    shap_values = shap.TreeExplainer(model).shap_values(X_test)
    fig = shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
    fig_filename = 'summary_plot.png'
    plt.savefig(fig_filename)
    run.upload_file(f"graphics/{fig_filename}", fig_filename)
    shap.matplotlib.pyplot.close()

    # Alternate view
    fig = shap.summary_plot(shap_values, X_test, show=False)
    fig_filename = 'summary_plot_2.png'
    plt.savefig(fig_filename)
    run.upload_file(f"graphics/{fig_filename}", fig_filename)

    return dataframe1,

