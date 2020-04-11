import pandas as pd
import streamlit as st
import dataset_knn as dt

@st.cache
def getDatasets():
    df = dt.LoadDataset("./DB_KNN.csv")
    df_class_name = dt.LoadDataset("./DB_KNN_Classes.csv")
    return df, df_class_name

if __name__ == "__main__":
    
    df, df_class_name = getDatasets()
    

    figs_2d_tbl = dt.GetFigures2D()
    figs_3d_tbl = dt.GetFigures3D()
    plot_2d_choices_list = [fig["title"] for fig in figs_2d_tbl]
    plot_3d_choices_list = [fig["title"] for fig in figs_3d_tbl]


    st.title("Power Signature Blob - Dataset")
    st.sidebar.title("About")
    st.sidebar.info("")
    st.sidebar.title("Publications")
    fig_to_plot_2d = st.sidebar.selectbox("2D Plot choices", plot_2d_choices_list, 0)
    fig_to_plot_3d = st.sidebar.selectbox("3D Plot choices", plot_3d_choices_list, 0)

    entry = [fig for fig in figs_2d_tbl if fig["title"] == fig_to_plot_2d][0]
    fig = dt.Create2DFigure(df, df_class_name, entry["x"], entry["y"], entry["title"])
    st.write(fig)

    entry = [fig for fig in figs_3d_tbl if fig["title"] == fig_to_plot_3d][0]
    fig = dt.Create3DFigure(df, df_class_name, entry["x"], entry["y"], entry["z"], entry["title"])
    st.write(fig)