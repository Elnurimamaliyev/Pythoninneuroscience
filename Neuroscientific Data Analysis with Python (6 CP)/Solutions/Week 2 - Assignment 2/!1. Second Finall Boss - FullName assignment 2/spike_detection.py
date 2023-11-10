import matplotlib.pyplot as plt


def detect_spikes(voltage, time, v_thres: float):
    """Detect spikes.

    Args:
        voltage: Voltage trace.
        time: Time points for the voltage. List of time values, one time value for each voltage value.
        v_thres (float): Voltage threshold for detecting spikes

    Returns:
        spike_voltages, spike_times
    """

    # initialize empty lists for holding the results
    spike_voltages = []
    spike_times = []
    for idx, current_voltage in enumerate(voltage):  # iterate over the voltage values, plus generate an index
        if current_voltage > v_thres:  # if the current voltage exceeds the threshold
            spike_voltages.append(current_voltage)  # save the voltage value
            spike_times.append(time[idx])  # use the index to get the corresponding time

    return spike_voltages, spike_times


def plot(voltage, time, spike_voltages, spike_times):
    """Plot voltage and spiketimes.

    Args:
        voltage: Voltage trace.
        time: Time (in seconds) for the voltage. List of time values, one time value for each voltage value.
        spike_voltages: Voltage value for each spike
        spike_times: Time of each spike (in seconds)
    """
    plt.figure(figsize=(20, 2))
    plt.plot(time, voltage, 'k', label='Voltage')
    plt.plot(spike_times, spike_voltages, 'or', alpha=0.3, label='Spikes')
    plt.title(f"{len(spike_times)} spikes detected")
    plt.xlim(min(time), max(time))
    plt.xlabel('Time [seconds]')
    plt.ylabel('Vm [mV]')
    plt.legend(loc='upper right')
    plt.show()
