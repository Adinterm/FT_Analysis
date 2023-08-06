def save_data():
        data = np.column_stack((freq_cols_pos, magnitude_spectrum_pos.mean(axis=0)))
        np.savetxt('fft_data.csv', data, delimiter=',', header='Frequency,Magnitude', comments='')

