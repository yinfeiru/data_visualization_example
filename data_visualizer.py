import matplotlib
# since we are running this program on a remote machine via ssh,
# plot() will error out when it tries to open up the image
# by using 'Agg', we disallow  matplotlib to open up the file
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from csv_generator import CSVGenerator

places = CSVGenerator(['37.7749,-122.4194', '40.785091,-73.968285'])
csv_path = places.generate_rating_buckets_csv()
df = pd.read_csv(csv_path)
df.plot.bar(x='Rating')
plt.savefig('data.png')
