import dash
from dash import html
import libs.private_lib.hello as private

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Main App"),
    html.Div(private.say_hello())
])

if __name__ == "__main__":
    app.run_server(debug=True)
    
