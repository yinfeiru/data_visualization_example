import matplotlib
# since we are running this program on a remote machine via ssh,
# plot() will error out when it tries to open up the image
# by using 'Agg', we disallow  matplotlib to open up the file
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from csv_generator import CSVGenerator

sf_places = CSVGenerator('37.7749,-122.4194')
sf_csv_path = sf_places.generate_csv()
sf_df = pd.read_csv(sf_csv_path)
sf_df.plot()
plt.savefig('data.png')

ny_places = CSVGenerator('40.785091,-73.968285')
ny_csv_path = ny_places.generate_csv()
ny_df = pd.read_csv(ny_csv_path)
ny_df.plot()
plt.savefig('data.png')
