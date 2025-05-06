import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""<h1>Binary Ninja Analysis</h1>""")
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>Marimo notebook setup</h2>""")
    return


@app.cell
def _():
    import marimo as mo
    import plotly.express as px
    import polars as pl
    import quak
    import altair as alt
    return alt, mo, pl, quak


@app.cell
def _(mo):
    mo.md(r"""<h2>Load the parquet results</h2>""")
    return


@app.cell
def _(mo, pl, quak):
    df = pl.read_parquet("./binary_analysis_results.parquet")
    widget = mo.ui.anywidget(quak.Widget(df))
    widget
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""<h2>Marimo data explorer</h2>""")
    return


@app.cell
def _(df, mo):
    mo.ui.data_explorer(df['Binary', 'Entropy', 'Average_Cyclomatic_Complexity'])
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(mo):
    mo.md(r"""<h2>Charting with Altair</h2>""")
    return


@app.cell
def _(alt, df, mo):
    chart = alt.Chart(df).mark_bar().encode(
        x='Binary:N',  # :N specifies it as a nominal (categorical) field
        y=alt.Y('Entropy:Q', title='Entropy'),  # :Q specifies it as quantitative
        color=alt.Color('Average_Cyclomatic_Complexity:Q', scale=alt.Scale(scheme='viridis'))
    ).properties(
        width=600,
        height=400,
        title='Binary Files by Entropy and Complexity'
            ).configure_axisX(
        labelAngle=45
    )

    # Display the chart in Marimo
    mo.ui.altair_chart(chart)
    return


if __name__ == "__main__":
    app.run()
