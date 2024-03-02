
from dash.testing.application_runners import import_app
from dash.testing.browser import Browser

def test_header_presence(dash_duo: Browser):
    # Starts the Dash app in a test browser
    dash_duo.start_server(import_app("task4.app"))

    header = dash_duo.find_element("h1")

    # Assert that the header is present and visible
    assert header.is_displayed(), "Header is not present"

def test_visualization_presence(dash_duo: Browser):
    dash_duo.start_server(import_app("task4.app"))

    graph = dash_duo.find_element("#sales-graph")

    # Assert that the graph is present and visible
    assert graph.is_displayed(), "Graph (visualisation) is not present"

def test_region_picker_presence(dash_duo: Browser):
    dash_duo.start_server(import_app("task4.app"))

    # Use the ID of the RadioItems component to find it
    region_picker = dash_duo.find_element("#region-selector")

    # Assert that the region picker is present and visible
    assert region_picker.is_displayed(), "Region picker is not present"
