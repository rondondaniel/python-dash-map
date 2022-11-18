import dash
import dash_leaflet as dl
import json

data = {
    "features":
        [
            {
                "geometry":
                    {
                        "coordinates":
                            
                                [
                                    [
                                        [-28.65234 , 58.44773],
                                        [-23.33496, 52.9354],
                                        [-14.32617 , 53.01478]
                                    ],
                                    [
                                        [-14.32617, 53.01478],
                                        [-10.37109, 58.1707], 
                                        [-0.65918, 59.68993],
                                    ],
                                ],
                            
                        "type":"MultiLineString"
                    },
                    "type":"Feature"
            }
        ],
    "type":"FeatureCollection"
}

app = dash.Dash()
app.layout = dl.Map([dl.TileLayer(), dl.GeoJSON(data=data)], style={'width': '1000px', 'height': '500px','margin': "auto", "display": "block"})

if __name__ == '__main__':
   app.run_server(debug=True,host="0.0.0.0", dev_tools_ui=False)   