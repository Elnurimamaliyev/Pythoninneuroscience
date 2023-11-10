import matplotlib.pyplot as plt

def detect_spikes(recording,timeseconds,threshold):
    '''
    Detect spikes in a recording.

    Args::
    - voltage: the recording (voltage values)
    - time: time (in seconds) for each value in recording
    - threshold: voltage threshold for detecting spikes

    Returns:
    - spike_voltages: voltage values at which spikes occurred
    - spike_times: time (in seconds) at which spikes occurred
    '''
    spike_voltages=[]
    timeofspike=[]
    for idx,val in enumerate(recording):
        if val > threshold:
            spike_voltages.append(val)
            timeofspike.append(timeseconds[idx])
    return timeofspike,spike_voltages

def plot_spikes(recording,timeseconds,spike_voltages,timeofspike,trial_number):
    """
    Plot the voltage trace and spikes.

    Args::
    - voltage: the recording (voltage values)
    - time: time (in seconds) for each value in recording
    - spike_voltages: voltage values at which spikes occurred
    - spike_times: time (in seconds) at which spikes occurred
    - trial_number: Number of trial
    """
    plt.figure(figsize=(18, 3))
    plt.plot(timeseconds,recording,'k', label='voltage')
    plt.scatter(timeofspike,spike_voltages,c='r',alpha=0.2, label='spikes')
    plt.title(f"{len(spike_voltages)} spikes detected in trial#{trial_number}")
    plt.xlim(timeseconds[0],timeseconds[-1])
    plt.xlabel('Time[seconds]')
    plt.ylabel('Vm[mV]')
    plt.legend()