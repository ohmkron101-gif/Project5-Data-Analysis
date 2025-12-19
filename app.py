import streamlit as st
import pandas as pd
import numpy as np



df = pd.read_csv('sustainable_waste_management_dataset_2024.csv')

st.write(df)






df = pd.read_csv("sustainable_waste_management_dataset_2024.csv")

st.title("ปริมาณขยะรวมแยกตามพื้นที่ (ปี 2024)")


area_summary = df.groupby("area", as_index=False)["waste_kg"].sum()


st.vega_lite_chart(
    area_summary,
    {
        "mark": {
            "type": "bar",
            "cornerRadiusTopLeft": 6,
            "cornerRadiusTopRight": 6
        },
        "encoding": {
            "x": {
                "field": "area",
                "type": "nominal",
                "title": "พื้นที่",
                "axis": {"labelAngle": -30}
            },
            "y": {
                "field": "waste_kg",
                "type": "quantitative",
                "<h1>title": "ปริมาณขยะรวม (กิโลกรัม)</h1>"
            },
            "color": {
                "field": "area",
                "type": "nominal",
                "legend": None
            },
            "tooltip": [
                {"field": "area", "type": "nominal", "title": "พื้นที่"},
                {"field": "waste_kg", "type": "quantitative", "title": "ขยะ (กก.)"}
            ]
        }
    },
    use_container_width=True
)


st.title(" Predicted vs Actual Dollar Price")


df_plot = pd.DataFrame({
    "Actual Price": [100, 150, 200, 250, 300],
    "Predicted Price": [110, 140, 210, 240, 290]
})


st.scatter_chart(
    df_plot,
    x="Actual Price",
    y="Predicted Price"
)




