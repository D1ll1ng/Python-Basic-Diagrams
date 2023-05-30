import numpy as np
import seaborn as sns
sns.set_theme(style="ticks")

rs = np.random.RandomState(1)
x = rs.gamma(305, size=1500)
y = 3.5 * x + rs.normal(size=1500)

sns.jointplot(x=x, y=y, kind="hex", color="#4CB391")