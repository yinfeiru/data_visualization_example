import matplotlib
# since we are running this program on a remote machine via ssh,
# plot() will error out when it tries to open up the image
# by using 'Agg', we disallow  matplotlib to open up the file
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from csv_generator import CSVGenerator

csvgenerator = CSVGenerator()
csv_path = csvgenerator.generate_csv()
df = pd.read_csv(csv_path)
df.plot()
plt.savefig('data.png')
