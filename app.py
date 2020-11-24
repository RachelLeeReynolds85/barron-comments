from flask import Flask, jsonify, render_template
import csv
import os
from bs4 import BeautifulSoup
import json
import plotly
import plotly.express as px

app = Flask(__name__)

def get_search_results():
    with open (os.path.join("testing", "html_dump.html"), "r", encoding="utf-8") as file:
            contents = file.read()
            soup = BeautifulSoup(contents, "lxml")

    search_results = soup.find_all("div", class_="item")
    search_results_html = str(search_results).strip("[").strip("]")

    with open("search_results.html", "w+", encoding="utf-8") as f:
        f.write(search_results_html)
    
    return search_results_html

def load_data():
    with open(os.path.join("barron-comments.csv")) as file:
        dict_reader = csv.DictReader(file)
        return list(dict_reader)


def create_plot():
    data = load_data()

    trace1 = {
    "x": [d["event_id"] for d in data],
    "y": [d["covid_names_score"] for d in data],
    "mode": "lines+markers",
    "name": "How many names there are for COVID",
    # "yaxis": "y1",
    "line": {"color": "black"},
    "text": [d["covid_names_txt"] for d in data],
    "hovertemplate": "%{text} names",
    "hoverlabel": {"namelength": 0},
    }

    trace2 = {
        "x": [d["event_id"] for d in data],
        "y": [d["sick_duration_score_min"] for d in data],
        "mode": "lines+markers",
        "name": "How quickly Barron got better",
        "line": {"color": "blue"},
        "text": [d["sick_duration_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace3 = {
        "x": [d["event_id"] for d in data],
        "y": [d["age_score"] for d in data],
        "mode": "lines+markers",
        "name": "Barron's age",
        "line": {"color": "red"},
        "text": [d["age_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace4 = {
        "x": [d["event_id"] for d in data],
        "y": [d["health_score"] for d in data],
        "mode": "lines+markers",
        "name": "'Health' comments",
        "line": {"color": "green"},
        "text": [d["health_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace5 = {
        "x": [d["event_id"] for d in data],
        "y": [d["strong_score"] for d in data],
        "mode": "lines+markers",
        "name": "'Strong' comments",
        "line": {"color": "orange"},
        "text": [d["strong_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace6 = {
        "x": [d["event_id"] for d in data],
        "y": [d["young_score"] for d in data],
        "mode": "lines+markers",
        "name": "'Young' comments",
        "line": {"color": "purple"},
        "text": [d["young_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace7 = {
        "x": [d["event_id"] for d in data],
        "y": [d["tall_score"] for d in data],
        "mode": "lines+markers",
        "name": "'Tall' comments",
        "line": {"color": "teal"},
        "text": [d["tall_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace8 = {
        "x": [d["event_id"] for d in data],
        "y": [d["attractive_score"] for d in data],
        "mode": "lines+markers",
        "name": "Attractiveness comments",
        "line": {"color": "gold"},
        "text": [d["attractive_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace9 = {
        "x": [d["event_id"] for d in data],
        "y": [d["good_score"] for d in data],
        "mode": "lines+markers",
        "name": "'Good' comments",
        "line": {"color": "gray"},
        "text": [d["good_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    trace10 = {
        "x": [d["event_id"] for d in data],
        "y": [d["smart_score"] for d in data],
        "mode": "lines+markers",
        "name": "'Smart' comments",
        "line": {"color": "fuchsia"},
        "text": [d["smart_txt"] for d in data],
        "hovertemplate": "%{text}",
        "hoverlabel": {"namelength": 0},
    }

    plot_data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]

    plot_layout = {
        # "title": "Barron Comments Timeline",
        # "width": 1500,
        "height": 700,
        "margin": {
            "l": 10,
            "r": 100,
            "t": 50,
            "b": 275,
        },
        "legend": {
            "yanchor": "top",
            "y": 0.99,
            "xanchor": "left",
            "x": 0.15
        },
        "xaxis": {
            # "title": {
            #     "text": "Event",
            #     "font": {"color": "black"},
            # },
            "tickfont": {
                "color": "black",
            },
            "showgrid": True,
            "zeroline": False,
            "tickmode": "array",
            "tickvals": [d["event_id"] for d in data],
            "ticktext": [d["event_date"] + " " + d["event_type"] + ", " + d["event_location"] for d in data],
            "range": [0.5, 19],
            "tickangle": 60,
        },
        "yaxis": {
            "showgrid": False,
            "visible": False,
            "zeroline": False,
        },
    }

    plot_config = {
        "responsive": True,
    }

    data = json.dumps(plot_data, cls=plotly.utils.PlotlyJSONEncoder)
    layout = json.dumps(plot_layout, cls=plotly.utils.PlotlyJSONEncoder)
    config = json.dumps(plot_config, cls=plotly.utils.PlotlyJSONEncoder)

    return data, layout, config


@app.route("/")
def home():
    data, layout, config = create_plot()
    speeches = get_search_results()
    return render_template("index.html", data=data, layout=layout, config=config, speeches=speeches)


if __name__ == "__main__":
    app.run(debug=True)