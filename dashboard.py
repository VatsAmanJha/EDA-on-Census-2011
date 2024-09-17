import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from helper import *

# Load the data
df = pd.read_csv("India Census 2011.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1(
            "India Census 2011 Dashboard",
            style={"text-align": "center", "margin-bottom": "20px"},
        ),
        dcc.Dropdown(
            id="state-filter",
            options=[
                {"label": state, "value": state} for state in df["State_name"].unique()
            ]
            + [{"label": "All States", "value": "all"}],
            value="all",  # Default to 'All States'
            style={"width": "50%", "margin": "auto", "margin-bottom": "20px"},
        ),
        html.Div(
            id="kpi-cards",
            style={
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "space-around",
                "margin-bottom": "20px",
            },
        ),
        # First Row: Statewise Population Distribution Map
        dcc.Graph(id="statewise-distribution"),
        # Second Row: Statewise or Districtwise Population
        dcc.Graph(id="statewise-or-districtwise-population"),
        # Third Row: Gender Distribution and Age Group Distribution
        html.Div(
            style={
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "space-around",
            },
            children=[
                dcc.Graph(id="gender-distribution", style={"width": "48%"}),
                dcc.Graph(id="age-group-distribution", style={"width": "48%"}),
            ],
        ),
        # Fourth Row: Education Distribution and Literacy Rate
        html.Div(
            style={
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "space-around",
            },
            children=[
                dcc.Graph(id="education-distribution", style={"width": "48%"}),
                dcc.Graph(id="literacy-rate", style={"width": "48%"}),
            ],
        ),
        # Fifth Row: Worker Distribution, Worker Types Distribution, and Gender-wise Workers
        html.Div(
            style={
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "space-around",
            },
            children=[
                dcc.Graph(id="worker-distribution", style={"width": "32%"}),
                dcc.Graph(id="worker-types-distribution", style={"width": "32%"}),
                dcc.Graph(
                    id="worker-gender-types-distribution", style={"width": "32%"}
                ),
            ],
        ),
        # Sixth Row: worker-vs-literate
        dcc.Graph(id="worker-vs-literate"),
        # Last Row: All Regions and Hindu-Muslim Distribution
        html.Div(
            style={
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "space-around",
            },
            children=[
                dcc.Graph(id="religion-distribution", style={"width": "48%"}),
                dcc.Graph(id="hindu-muslim-distribution", style={"width": "48%"}),
            ],
        ),
    ]
)


# Define the callback to update the dashboard based on the selected state
@app.callback(
    [
        Output("kpi-cards", "children"),
        Output("statewise-distribution", "figure"),
        Output("gender-distribution", "figure"),
        Output("religion-distribution", "figure"),
        Output("hindu-muslim-distribution", "figure"),
        Output("education-distribution", "figure"),
        Output("age-group-distribution", "figure"),
        Output("literacy-rate", "figure"),
        Output("worker-distribution", "figure"),
        Output("worker-types-distribution", "figure"),
        Output("worker-gender-types-distribution", "figure"),
        Output("statewise-or-districtwise-population", "figure"),
        Output("worker-vs-literate", "figure"),
    ],
    [Input("state-filter", "value")],
)
def update_dashboard(state):
    # Calculate KPIs
    kpis = countrywise(df, state)
    kpi_cards = [
        html.Div(
            [html.H3("Total Population"), html.P(f"{kpis['Total_Population']:,}")],
            className="kpi-box kpi-total-population",
        ),
        html.Div(
            [
                html.H3("Total Male Population"),
                html.P(f"{kpis['Total_Male_Population']:,}"),
            ],
            className="kpi-box kpi-total-male-population",
        ),
        html.Div(
            [
                html.H3("Total Female Population"),
                html.P(f"{kpis['Total_Female_Population']:,}"),
            ],
            className="kpi-box kpi-total-female-population",
        ),
        html.Div(
            [
                html.H3("Total Literate Population"),
                html.P(f"{kpis['Total_Literate_Population']:,}"),
            ],
            className="kpi-box kpi-total-literate-population",
        ),
        html.Div(
            [html.H3("Total Workers"), html.P(f"{kpis['Total_Workers']:,}")],
            className="kpi-box kpi-total-workers",
        ),
        html.Div(
            [html.H3("Total Hindus"), html.P(f"{kpis['Total_Hindus']:,}")],
            className="kpi-box kpi-total-hindus",
        ),
        html.Div(
            [html.H3("Total Muslims"), html.P(f"{kpis['Total_Muslims']:,}")],
            className="kpi-box kpi-total-muslims",
        ),
        html.Div(
            [html.H3("Total Christians"), html.P(f"{kpis['Total_Christians']:,}")],
            className="kpi-box kpi-total-christians",
        ),
        html.Div(
            [html.H3("Total Sikhs"), html.P(f"{kpis['Total_Sikhs']:,}")],
            className="kpi-box kpi-total-sikhs",
        ),
        html.Div(
            [html.H3("Total Buddhists"), html.P(f"{kpis['Total_Buddhists']:,}")],
            className="kpi-box kpi-total-buddhists",
        ),
        html.Div(
            [html.H3("Total Jains"), html.P(f"{kpis['Total_Jains']:,}")],
            className="kpi-box kpi-total-jains",
        ),
        html.Div(
            [
                html.H3("Total Secondary Education"),
                html.P(f"{kpis['Total_Secondary_Education']:,}"),
            ],
            className="kpi-box kpi-total-secondary-education",
        ),
        html.Div(
            [
                html.H3("Total Higher Education"),
                html.P(f"{kpis['Total_Higher_Education']:,}"),
            ],
            className="kpi-box kpi-total-higher-education",
        ),
        html.Div(
            [
                html.H3("Total Graduate Education"),
                html.P(f"{kpis['Total_Graduate_Education']:,}"),
            ],
            className="kpi-box kpi-total-graduate-education",
        ),
        html.Div(
            [
                html.H3("Total Age Group 0-29"),
                html.P(f"{kpis['Total_Age_Group_0_29']:,}"),
            ],
            className="kpi-box kpi-total-age-group-0-29",
        ),
        html.Div(
            [
                html.H3("Total Age Group 30-49"),
                html.P(f"{kpis['Total_Age_Group_30_49']:,}"),
            ],
            className="kpi-box kpi-total-age-group-30-49",
        ),
        html.Div(
            [html.H3("Total Age Group 50+"), html.P(f"{kpis['Total_Age_Group_50']:,}")],
            className="kpi-box kpi-total-age-group-50",
        ),
    ]

    # Generate figures based on state selection
    gender_fig = plot_gender_distribution(df, state)
    religion_fig = plot_religion_distribution(df, state)
    hindu_muslim_fig = plot_hindu_muslim_distribution(df, state)
    education_fig = plot_education_distribution(df, state)
    age_group_fig = plot_age_group_distribution(df, state)
    literacy_fig = plot_literacy_rate(df, state)
    worker_fig = plot_worker_distribution(df, state)
    worker_types_fig = plot_worker_types_distribution(df, state)
    worker_gender_types_fig = plot_worker_gender_types_distribution(df, state)
    statewise_or_districtwise_population_fig = (
        plot_statewise_or_districtwise_population(df, state)
    )
    worker_vs_literate_fig = worker_vs_literate(df, state)
    if state=='all':
        statewise_fig = plot_statewise_distribution(df, state)
        return (
            kpi_cards,
            statewise_fig,
            gender_fig,
            religion_fig,
            hindu_muslim_fig,
            education_fig,
            age_group_fig,
            literacy_fig,
            worker_fig,
            worker_types_fig,
            worker_gender_types_fig,
            statewise_or_districtwise_population_fig,
            worker_vs_literate_fig,
        )
    else:
        nonstatewise_fig = plot_statewise_distribution(df, state)
        return (
            kpi_cards,
            nonstatewise_fig,
            gender_fig,
            religion_fig,
            hindu_muslim_fig,
            education_fig,
            age_group_fig,
            literacy_fig,
            worker_fig,
            worker_types_fig,
            worker_gender_types_fig,
            statewise_or_districtwise_population_fig,
            worker_vs_literate_fig,
        )

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
