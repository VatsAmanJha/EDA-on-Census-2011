import pandas as pd
import plotly.graph_objects as go
import json
import plotly.express as px


# Function to calculate KPIs
def countrywise(df, state="all"):
    if state == "all":
        kpis = {
            "Total_Population": df["Population"].sum(),
            "Total_Male_Population": df["Male"].sum(),
            "Total_Female_Population": df["Female"].sum(),
            "Total_Literate_Population": df["Literate"].sum(),
            "Total_Workers": df["Workers"].sum(),
            "Total_Hindus": df["Hindus"].sum(),
            "Total_Muslims": df["Muslims"].sum(),
            "Total_Christians": df["Christians"].sum(),
            "Total_Sikhs": df["Sikhs"].sum(),
            "Total_Buddhists": df["Buddhists"].sum(),
            "Total_Jains": df["Jains"].sum(),
            "Total_Secondary_Education": df["Secondary_Education"].sum(),
            "Total_Higher_Education": df["Higher_Education"].sum(),
            "Total_Graduate_Education": df["Graduate_Education"].sum(),
            "Total_Age_Group_0_29": df["Age_Group_0_29"].sum(),
            "Total_Age_Group_30_49": df["Age_Group_30_49"].sum(),
            "Total_Age_Group_50": df["Age_Group_50"].sum(),
        }
        return kpis
    df = df[df["State_name"] == state]
    kpis = {
        "Total_Population": df["Population"].sum(),
        "Total_Male_Population": df["Male"].sum(),
        "Total_Female_Population": df["Female"].sum(),
        "Total_Literate_Population": df["Literate"].sum(),
        "Total_Workers": df["Workers"].sum(),
        "Total_Hindus": df["Hindus"].sum(),
        "Total_Muslims": df["Muslims"].sum(),
        "Total_Christians": df["Christians"].sum(),
        "Total_Sikhs": df["Sikhs"].sum(),
        "Total_Buddhists": df["Buddhists"].sum(),
        "Total_Jains": df["Jains"].sum(),
        "Total_Secondary_Education": df["Secondary_Education"].sum(),
        "Total_Higher_Education": df["Higher_Education"].sum(),
        "Total_Graduate_Education": df["Graduate_Education"].sum(),
        "Total_Age_Group_0_29": df["Age_Group_0_29"].sum(),
        "Total_Age_Group_30_49": df["Age_Group_30_49"].sum(),
        "Total_Age_Group_50": df["Age_Group_50"].sum(),
    }
    return kpis


# Function to plot gender distribution
def plot_gender_distribution(df, state="all"):
    if state == "all":
        gender_data = df[["Male", "Female"]].sum().reset_index()
        gender_data.columns = ["Gender", "Population"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=gender_data["Gender"],
                    values=gender_data["Population"],
                    textinfo="label+percent",
                    hole=0.3,
                    marker=dict(colors=["#1f77b4", "#ff7f0e"]),
                )
            ]
        )

        fig.update_layout(
            title_text="Gender Distribution in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    gender_data = df[["Male", "Female"]].sum().reset_index()
    gender_data.columns = ["Gender", "Population"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=gender_data["Gender"],
                values=gender_data["Population"],
                textinfo="label+percent",
                hole=0.3,
                marker=dict(colors=["#1f77b4", "#ff7f0e"]),
            )
        ]
    )

    fig.update_layout(
        title_text=f"Gender Distribution in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot religion distribution
def plot_religion_distribution(df, state="all"):
    if state == "all":
        religion_data = (
            df[["Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains"]]
            .sum()
            .reset_index()
        )
        religion_data.columns = ["Religion", "Population"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=religion_data["Religion"],
                    values=religion_data["Population"],
                    hole=0.3,
                    textinfo="label+percent",
                    marker=dict(
                        colors=[
                            "#ff9933",  # Hindu
                            "green",  # Muslim
                            "#4DB6AC",  # Christian
                            "#7986CB",  # Sikh
                            "#F06292",  # Buddhist
                            "#E57373",  # Jain
                        ]
                    ),
                )
            ]
        )

        fig.update_layout(
            title_text="Overall Religion-wise Population Distribution in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    religion_data = (
        df[["Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains"]]
        .sum()
        .reset_index()
    )
    religion_data.columns = ["Religion", "Population"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=religion_data["Religion"],
                values=religion_data["Population"],
                hole=0.3,
                textinfo="label+percent",
                marker=dict(
                    colors=[
                        "#ff9933",  # Hindu
                        "green",  # Muslim
                        "#4DB6AC",  # Christian
                        "#7986CB",  # Sikh
                        "#F06292",  # Buddhist
                        "#E57373",  # Jain
                    ]
                ),
            )
        ]
    )

    fig.update_layout(
        title_text=f"Overall Religion-wise Population Distribution in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot Hindu-Muslim distribution
def plot_hindu_muslim_distribution(df, state="all"):
    if state == "all":
        hindu_muslim_data = df[["Hindus", "Muslims"]].sum().reset_index()
        hindu_muslim_data.columns = ["Religion", "Population"]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=hindu_muslim_data["Religion"],
                    y=hindu_muslim_data["Population"],
                    marker_color=["#ff9933", "green"],
                )
            ]
        )

        fig.update_layout(
            title_text="Hindu-Muslim Population Distribution in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    hindu_muslim_data = df[["Hindus", "Muslims"]].sum().reset_index()
    hindu_muslim_data.columns = ["Religion", "Population"]

    fig = go.Figure(
        data=[
            go.Bar(
                x=hindu_muslim_data["Religion"],
                y=hindu_muslim_data["Population"],
                marker_color=["#ff9933", "green"],
            )
        ]
    )

    fig.update_layout(
        title_text=f"Hindu-Muslim Population Distribution in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot education distribution
def plot_education_distribution(df, state="all"):
    if state == "all":
        education_data = (
            df[["Secondary_Education", "Higher_Education", "Graduate_Education"]]
            .sum()
            .reset_index()
        )
        education_data.columns = ["Education Level", "Population"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=education_data["Education Level"],
                    values=education_data["Population"],
                    textinfo="label+percent",
                    hole=0.3,
                    marker=dict(colors=["#1f77b4", "#ff7f0e", "#2ca02c"]),
                )
            ]
        )

        fig.update_layout(
            title_text="Education Level Distribution in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    education_data = (
        df[["Secondary_Education", "Higher_Education", "Graduate_Education"]]
        .sum()
        .reset_index()
    )
    education_data.columns = ["Education Level", "Population"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=education_data["Education Level"],
                values=education_data["Population"],
                textinfo="label+percent",
                hole=0.3,
                marker=dict(colors=["#1f77b4", "#ff7f0e", "#2ca02c"]),
            )
        ]
    )

    fig.update_layout(
        title_text=f"Education Level Distribution in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot state-wise distribution
def plot_statewise_distribution(df, state="all"):
    if state == "all":
        india_states = json.load(open("states_india.geojson", "r"))
        df_state = df.groupby("State_name")["Population"].sum().reset_index()

        state_id_map = {
            "ANDAMAN AND NICOBAR ISLANDS": 35,
            "ANDHRA PRADESH": 28,
            "ARUNACHAL PRADESH": 12,
            "ASSAM": 18,
            "BIHAR": 10,
            "CHANDIGARH": 4,
            "CHHATTISGARH": 22,
            "DADRA AND NAGAR HAVELI": 26,
            "DAMAN AND DIU": 25,
            "GOA": 30,
            "GUJARAT": 24,
            "HARYANA": 6,
            "HIMACHAL PRADESH": 2,
            "JAMMU AND KASHMIR": 1,
            "JHARKHAND": 20,
            "KARNATAKA": 29,
            "KERALA": 32,
            "LAKSHADWEEP": 31,
            "MADHYA PRADESH": 23,
            "MAHARASHTRA": 27,
            "MANIPUR": 14,
            "MEGHALAYA": 17,
            "MIZORAM": 15,
            "NAGALAND": 13,
            "NCT OF DELHI": 7,
            "ORISSA": 21,
            "PONDICHERRY": 34,
            "PUNJAB": 3,
            "RAJASTHAN": 8,
            "SIKKIM": 11,
            "TAMIL NADU": 33,
            "TRIPURA": 16,
            "UTTAR PRADESH": 9,
            "UTTARAKHAND": 5,
            "WEST BENGAL": 19,
        }

        df_state["State_id"] = df_state["State_name"].apply(lambda x: state_id_map[x])

        fig = px.choropleth_mapbox(
            df_state,
            locations="State_id",
            geojson=india_states,
            featureidkey="properties.state_code",
            color="Population",
            hover_name="State_name",
            hover_data=["Population"],
            mapbox_style="carto-positron",
            color_continuous_scale="Viridis",
            center={"lat": 22, "lon": 88},
            zoom=3,
            opacity=1,
        )

        # Update layout with additional configurations
        fig.update_layout(
            font=dict(family="Arial, Helvetica, sans-serif", size=14),
            title_text="State-wise Population Distribution",
            title_x=0.5,
            coloraxis_colorbar=dict(
                title="Total Population",
            ),
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
        )

        fig.update_layout(
            coloraxis_colorbar_x=-0.25,
        )

        return fig

    layout = go.Layout(width=10, height=10)

    fig1 = go.Figure(layout=layout)
    return fig1


# Function to plot age group distribution
def plot_age_group_distribution(df, state="all"):
    if state == "all":
        age_group_data = (
            df[["Age_Group_0_29", "Age_Group_30_49", "Age_Group_50"]]
            .sum()
            .reset_index()
        )
        age_group_data.columns = ["Age Group", "Population"]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=age_group_data["Age Group"],
                    y=age_group_data["Population"],
                    marker_color=px.colors.qualitative.Set2,
                )
            ]
        )

        fig.update_layout(
            title_text="Population Distribution by Age Group in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    age_group_data = (
        df[["Age_Group_0_29", "Age_Group_30_49", "Age_Group_50"]].sum().reset_index()
    )
    age_group_data.columns = ["Age Group", "Population"]

    fig = go.Figure(
        data=[
            go.Bar(
                x=age_group_data["Age Group"],
                y=age_group_data["Population"],
                marker_color=px.colors.qualitative.Set2,
            )
        ]
    )

    fig.update_layout(
        title_text=f"Population Distribution by Age Group in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot literacy rate
def plot_literacy_rate(df, state="all"):
    if state == "all":
        literate = df["Literate"].sum()
        illiterate = df["Population"].sum() - literate

        literacy_data = pd.DataFrame(
            {
                "Category": ["Literate", "Illiterate"],
                "Population": [literate, illiterate],
            }
        )

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=literacy_data["Category"],
                    values=literacy_data["Population"],
                    textinfo="label+percent",
                    marker=dict(colors=["#2ca02c", "#d62728"]),
                )
            ]
        )

        fig.update_layout(
            title_text="Literacy Rate in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    literate = df["Literate"].sum()
    illiterate = df["Population"].sum() - literate

    literacy_data = pd.DataFrame(
        {"Category": ["Literate", "Illiterate"], "Population": [literate, illiterate]}
    )

    fig = go.Figure(
        data=[
            go.Pie(
                labels=literacy_data["Category"],
                values=literacy_data["Population"],
                textinfo="label+percent",
                marker=dict(colors=["#2ca02c", "#d62728"]),
            )
        ]
    )

    fig.update_layout(
        title_text=f"Literacy Rate in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot worker distribution
def plot_worker_distribution(df, state="all"):
    if state == "all":
        workers = df["Workers"].sum()
        non_workers = df["Population"].sum() - workers

        worker_data = pd.DataFrame(
            {
                "Category": ["Workers", "Non-Workers"],
                "Population": [workers, non_workers],
            }
        )

        fig = go.Figure(
            data=[
                go.Bar(
                    x=worker_data["Category"],
                    y=worker_data["Population"],
                    marker_color=["#1f77b4", "#ff7f0e"],
                )
            ]
        )

        fig.update_layout(
            title_text="Worker vs. Non-Worker Population in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    workers = df["Workers"].sum()
    non_workers = df["Population"].sum() - workers

    worker_data = pd.DataFrame(
        {"Category": ["Workers", "Non-Workers"], "Population": [workers, non_workers]}
    )

    fig = go.Figure(
        data=[
            go.Bar(
                x=worker_data["Category"],
                y=worker_data["Population"],
                marker_color=["#1f77b4", "#ff7f0e"],
            )
        ]
    )

    fig.update_layout(
        title_text=f"Worker vs. Non-Worker Population in {state}",
        title_x=0.5,
    )

    return fig


# Function to plot worker types distribution
def plot_worker_types_distribution(df, state="all"):
    if state == "all":
        worker_types_data = (
            df[
                [
                    "Cultivator_Workers",
                    "Agricultural_Workers",
                    "Household_Workers",
                ]
            ]
            .sum()
            .reset_index()
        )
        worker_types_data.columns = ["Worker Type", "Population"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=worker_types_data["Worker Type"],
                    values=worker_types_data["Population"],
                    textinfo="label+percent",
                    marker=dict(colors=["#1f77b4", "#ff7f0e", "#2ca02c"]),
                )
            ]
        )

        fig.update_layout(
            title_text="Distribution of Worker Types in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    worker_types_data = (
        df[
            [
                "Cultivator_Workers",
                "Agricultural_Workers",
                "Household_Workers",
            ]
        ]
        .sum()
        .reset_index()
    )
    worker_types_data.columns = ["Worker Type", "Population"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=worker_types_data["Worker Type"],
                values=worker_types_data["Population"],
                textinfo="label+percent",
                marker=dict(colors=["#1f77b4", "#ff7f0e", "#2ca02c"]),
            )
        ]
    )

    fig.update_layout(
        title_text=f"Distribution of Worker Types in {state}",
        title_x=0.5,
    )

    return fig


def plot_worker_gender_types_distribution(df, state="all"):
    if state == "all":
        worker_gender_data = df[["Male_Workers", "Female_Workers"]].sum().reset_index()
        worker_gender_data.columns = ["Gender", "Population"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=worker_gender_data["Gender"],
                    values=worker_gender_data["Population"],
                    textinfo="label+percent",
                    marker=dict(colors=["#1f77b4", "#ff7f0e"]),
                )
            ]
        )

        fig.update_layout(
            title_text="Distribution of Worker Gender in India",
            title_x=0.5,
        )

        return fig
    df = df[df["State_name"] == state]
    worker_gender_data = df[["Male_Workers", "Female_Workers"]].sum().reset_index()
    worker_gender_data.columns = ["Gender", "Population"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=worker_gender_data["Gender"],
                values=worker_gender_data["Population"],
                textinfo="label+percent",
                marker=dict(colors=["#1f77b4", "#ff7f0e"]),
            )
        ]
    )

    fig.update_layout(
        title_text=f"Distribution of Worker Gender in {state}",
        title_x=0.5,
    )

    return fig


def plot_statewise_or_districtwise_population(df, state="all"):
    if state == "all":
        df_state = df.groupby("State_name")["Population"].sum().reset_index()
        fig = go.Figure(
            data=[
                go.Bar(
                    x=df_state["State_name"],
                    y=df_state["Population"],
                )
            ]
        )

        fig.update_layout(
            title_text="State-wise Population",
            title_x=0.5,
        )

        return fig
    df_district = df.groupby("District_name")["Population"].sum().reset_index()
    fig = go.Figure(
        data=[
            go.Bar(
                x=df_district["District_name"],
                y=df_district["Population"],
            )
        ]
    )

    fig.update_layout(
        title_text="District-wise Population",
        title_x=0.5,
    )

    return fig


def worker_vs_literate(df, state="all"):
    if state == "all":
        # Summarize the data at the state level
        df_state = df.groupby("State_name")[["Literate", "Workers"]].sum().reset_index()
        trace = go.Scatter(
            x=df_state["Literate"],
            y=df_state["Workers"],
            text=df_state["State_name"],
            mode="markers",
            marker=dict(
                color=df_state.index,
                colorscale="Viridis",
                showscale=False,
                size=df_state["Literate"] / 1000000,
            ),
        )
        fig = go.Figure(data=[trace])
        fig.update_layout(
            title="Worker vs Literate State Wise",
            xaxis_title="Literate",
            yaxis_title="Workers",
        )
        return fig

    # Filter data for the specific state
    df_state = df[df["State_name"] == state]
    # Group by district to summarize data at the district level
    df_district = (
        df_state.groupby("District_name")[["Literate", "Workers"]].sum().reset_index()
    )
    trace = go.Scatter(
        x=df_district["Literate"],
        y=df_district["Workers"],
        text=df_district["District_name"],
        mode="markers",
        marker=dict(
            color=df_district.index,
            colorscale="Viridis",
            showscale=False,
            size=(df_district["Literate"] % len(df_district)) * 1.5,
        ),
    )
    fig = go.Figure(data=[trace])
    fig.update_layout(
        title=f"Worker vs Literate in {state} District Wise",
        xaxis_title="Literate",
        yaxis_title="Workers",
    )
    return fig
