#streamlit run streamlit_tutorial.py

import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100,2)/(50,50) + [35.69, 139.70],
    columns = ['lat', 'lon']
)

#公式docs display data
#st.dataframe(df.style.highlight_max(axis=0)) #動的
#st.table(df.style.highlight_max(axis=0)) #静的

# 公式docs display chart
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
st.map(df)

'''
## コード

```python
import streamlit as st
import numpy as np
a = 123
```
'''