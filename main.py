import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from dataclasses import dataclass
from modules import calcs
import user_data


st.title("Betondoorsnede")
st.markdown("Eerste test voor controle betondoorsnede in Python met Streamlit")

if __name__ == "__main__":
    data_input = user_data.dims()
    dims = calcs.dims(data_input.width, data_input.height)

# Input box for dins of the section
width = st.number_input("breedte [mm]", value=data_input.width, step=1, format="%d", min_value=1, width = 200)
height = st.number_input("hoogte [mm]",  value=data_input.height,step=1, format="%d", min_value=1, width = 200)


section = calcs.dims(width, height)

st.write(f"De doorsnede heeft een breedte: {width} mm en een hoogte: {height} mm.")
st.write(f"De doorsnede heeft een oppervlakte: {section.area} mm^2.")




# Initial table data
df = pd.DataFrame({
    "#": [1, 2, 3],
    "omschrijving": ["druk", "neutraal", "trek"],
    "normaalkracht N [kN]": [-100, 0, 100],
    "moment M [kNm]": [-50, 50, 50],
})

# Editable table input
edited_df = st.data_editor(df, width=100, height=None, use_container_width=True, hide_index=True, column_order=None, column_config={
    "normaalkracht N [kN]": st.column_config.NumberColumn("Normaalkracht", format="%.1f"),
    "moment M [kNm]": st.column_config.NumberColumn("Moment", format="%.1f")
}
, num_rows="dynamic", disabled=False, key=None, on_change=None, args=None, kwargs=None, row_height=None)

# uploaded_file = st.file_uploader("Upload Excel or CSV file")

# if uploaded_file:
#     if uploaded_file.name.endswith(".xlsx"):
#         df = pd.read_excel(uploaded_file)
#     else:
#         df = pd.read_csv(uploaded_file)
#     st.dataframe(df)
    

# Extract x and y using column indices
x = edited_df.iloc[:, 3]  # 3rd column → 'moment'
y = edited_df.iloc[:, 2]  # 2nd column → 'normaalkracht'

# Plot the data
fig, ax = plt.subplots()
ax.scatter(x, y, color="blue")
ax.set_xlabel("moment M [kNm]")
ax.set_ylabel("normaalkracht N [kN]")
ax.set_title("krachten")
ax.grid(True)

# Show plot under the table
st.pyplot(fig)


# Extract the column into a list and create the object
input_data = user_data.forces(\
        description=edited_df["omschrijving"].tolist(),
        normal=edited_df["normaalkracht N [kN]"].tolist(), 
        bending=edited_df["moment M [kNm]"].tolist())


# Show the list in Streamlit
st.write("omschrijving:", input_data.description)
st.write("Normaalkrachten:", input_data.normal)
st.write("Mommenten:", input_data.bending)




