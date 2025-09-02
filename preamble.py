# Next is original line.
# see https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering/issues/32
#from IPython.display import set_matplotlib_formats, display
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from cycler import cycler

# New block per above url on set_matplotlib_formats problem
# settings for jupyter book: svg for html version, high-resolution png for pdf
import matplotlib_inline.backend_inline
# matplotlib_inline.backend_inline.set_matplotlib_formats('svg', 'png')
# import matplotlib as mpl
# mpl.rcParams['figure.dpi'] = 400

matplotlib_inline.backend_inline.set_matplotlib_formats('pdf', 'png')
#set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['image.cmap'] = "viridis"
plt.rcParams['image.interpolation'] = "none"
plt.rcParams['savefig.bbox'] = "tight"
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['legend.numpoints'] = 1
plt.rc('axes', prop_cycle=(
    cycler('color', mglearn.plot_helpers.cm_cycle.colors) +
    cycler('linestyle', ['-', '-', "--", (0, (3, 3)), (0, (1.5, 1.5))])))

np.set_printoptions(precision=3, suppress=True)

pd.set_option("display.max_columns", 8)
pd.set_option('display.precision', 2)

__all__ = ['np', 'mglearn', 'display', 'plt', 'pd']
