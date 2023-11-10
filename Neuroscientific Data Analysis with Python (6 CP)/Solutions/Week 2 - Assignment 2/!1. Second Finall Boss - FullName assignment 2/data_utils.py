import numpy as np
def load_voltage_data(trial: int = 0):
    """Loads data from file for a specific trial.

    Args:
        trial (int, optional): Trial number to load data for. Defaults to 0.

    Returns:
        list[float]: List of voltage values (as floats) for the trial
    """
    all_trials = np.loadtxt('voltage_traces.txt')
    single_trial = all_trials[trial, :].tolist()
    return single_trial