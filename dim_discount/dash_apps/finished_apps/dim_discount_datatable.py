import pandas as pd
import plotly 
import plotly.express as px

import dash
import dash_table 

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from django_pandas.io import read_frame

from django_plotly_dash import DjangoDash
from dash_table.Format import Format, Align

from dim_discount.models import Dim_discount

from datetime import datetime as dt

import dash_bootstrap_components as dbc

#app = dash.Dash('datatable')

app = DjangoDash('dim_discount_datatable', external_stylesheets=[dbc.themes.BOOTSTRAP],
                # meta_tags=[
                #             {'name': 'viewport',
                #             'content': 'width=device-width, initial-scale=1.0'}
                #           ]
                )

dim_discount_df = Dim_discount.objects.all()
dim_discount_df = read_frame(dim_discount_df)
df = dim_discount_df
#df["product_group"] = df["product_group"].astype(str).astype(int)

now_year = dt.today().strftime('%Y'),
now_month = dt.today().strftime('%m'),
now_day = dt.today().strftime('%d'),

# getting product name for drop down options
options = []
for discount_name in df.discount_name:
    options.append({'label': discount_name, 'value': discount_name})


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
                html.H1("""Select Color Description""",
                    className = 'm-0 text-left text-dark'
                    #style={'margin-right': '3em'}
                ),

                width =5

        ),
        dbc.Col(html.Div(""), width=3),
        dbc.Col(html.Div(""), width=4),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='demo-dropdown',
                options=options,
                multi=True
            ),
        ], width=4)



    ]),

    html.Br(),

    dbc.Row([
        html.H2('Select date range', className='align-middle display-5 m-0 text-left text-dark h-75 font-weight-bolder', id='my-p-element'
             , style={'margin-right': '3em'}),
        dbc.Col([
            dcc.DatePickerRange(
                id='my-date-picker-range',  # ID to be used for callback
                calendar_orientation='horizontal',  # vertical or horizontal
                day_size=39,  # size of calendar image. Default is 39
                #start_date_placeholder_text="1/1/2000",
                end_date_placeholder_text="1/1/2099",  # text that appears when no end date chosen
                #end_date_placeholder_text=dt(int(now_year[0]),int(now_month[0]), int(now_day[0])).date(),
                with_portal=False,  # if True calendar will open in a full screen overlay portal
                first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
                reopen_calendar_on_clear=True,
                is_RTL=False,  # True or False for direction of calendar
                clearable=True,  # whether or not the user can clear the dropdown
                number_of_months_shown=1,  # number of months shown when calendar is open
                min_date_allowed=dt(2000, 1, 1),  # minimum date allowed on the DatePickerRange component
                max_date_allowed=dt(2099, 1, 1),  # maximum date allowed on the DatePickerRange component
                initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
                start_date=dt(2018, 8, 7).date(),
                #end_date=dt(int(now_year[0]),int(now_month[0]), int(now_day[0])).date(),
                display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
                month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
                minimum_nights=2,  # minimum number of days between start and end date
                persistence=True,
                persisted_props=['start_date'],
                persistence_type='session',  # session, local, or memory. Default is 'local'
                updatemode='singledate',  # singledate or bothdates. Determines when callback is triggered
                style=dict(
                    width='40%',
                    display='inline-block',
                    verticalAlign="middle"
                    )
                )
                ],
                style=dict(display='flex')
                ),  
    ]),

    dbc.Row([
        html.H2('Select date range', className='align-middle display-5 m-0 text-left text-dark h-75 font-weight-bolder', id='my-p-element'
             , style={'margin-right': '3em'}),
        dbc.Col([
            dcc.DatePickerRange(
                id='my-date-picker-range',  # ID to be used for callback
                calendar_orientation='horizontal',  # vertical or horizontal
                day_size=39,  # size of calendar image. Default is 39
                #start_date_placeholder_text="1/1/2000",
                end_date_placeholder_text="1/1/2099",  # text that appears when no end date chosen
                #end_date_placeholder_text=dt(int(now_year[0]),int(now_month[0]), int(now_day[0])).date(),
                with_portal=False,  # if True calendar will open in a full screen overlay portal
                first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
                reopen_calendar_on_clear=True,
                is_RTL=False,  # True or False for direction of calendar
                clearable=True,  # whether or not the user can clear the dropdown
                number_of_months_shown=1,  # number of months shown when calendar is open
                min_date_allowed=dt(2000, 1, 1),  # minimum date allowed on the DatePickerRange component
                max_date_allowed=dt(2099, 1, 1),  # maximum date allowed on the DatePickerRange component
                initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
                start_date=dt(2018, 8, 7).date(),
                #end_date=dt(int(now_year[0]),int(now_month[0]), int(now_day[0])).date(),
                display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
                month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
                minimum_nights=2,  # minimum number of days between start and end date
                persistence=True,
                persisted_props=['start_date'],
                persistence_type='session',  # session, local, or memory. Default is 'local'
                updatemode='singledate',  # singledate or bothdates. Determines when callback is triggered
                style=dict(
                    width='40%',
                    display='inline-block',
                    verticalAlign="middle"
                    )
                )
                ],
                style=dict(display='flex')
                ),  
    ]),

    dbc.Row([

        html.H2('Select date range', className='align-middle display-5 m-0 text-left text-dark h-75 font-weight-bolder', id='my-p-element'
             , style={'margin-right': '3em'}),
        dbc.Col([
            dcc.DatePickerRange(
                id='my-date-picker-range',  # ID to be used for callback
                calendar_orientation='horizontal',  # vertical or horizontal
                day_size=39,  # size of calendar image. Default is 39
                #start_date_placeholder_text="1/1/2000",
                end_date_placeholder_text="1/1/2099",  # text that appears when no end date chosen
                #end_date_placeholder_text=dt(int(now_year[0]),int(now_month[0]), int(now_day[0])).date(),
                with_portal=False,  # if True calendar will open in a full screen overlay portal
                first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
                reopen_calendar_on_clear=True,
                is_RTL=False,  # True or False for direction of calendar
                clearable=True,  # whether or not the user can clear the dropdown
                number_of_months_shown=1,  # number of months shown when calendar is open
                min_date_allowed=dt(2000, 1, 1),  # minimum date allowed on the DatePickerRange component
                max_date_allowed=dt(2099, 1, 1),  # maximum date allowed on the DatePickerRange component
                initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
                start_date=dt(2018, 8, 7).date(),
                #end_date=dt(int(now_year[0]),int(now_month[0]), int(now_day[0])).date(),
                display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
                month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
                minimum_nights=2,  # minimum number of days between start and end date
                persistence=True,
                persisted_props=['start_date'],
                persistence_type='session',  # session, local, or memory. Default is 'local'
                updatemode='singledate',  # singledate or bothdates. Determines when callback is triggered
                 style=dict(
                    width='40%',
                    display='inline-block',
                    verticalAlign="middle"
                    )
                )
                ],
                style=dict(display='flex')
                ),  
    ]),


    dbc.Row([
        dbc.Col([
            dcc.Interval(
                id='interval-component',
                interval=2000,
                n_intervals=0
    ),
    ])
        
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
                html.Div(
                    children = dash_table.DataTable(
                        id='discount_table',
                        # columns =[{'id': c, 'name': c} for c in df.columns],
                        columns=[
                            dict(id='discount_key', format=Format().align(Align.left))
                        ,   dict(id='discount_name') # , type='numeric'
                        ,   dict(id='discount_customer_id') # , type='numeric'
                        ,   dict(id='discount_customer_name')
                        ,   dict(id='discount_account_type')
                        ,   dict(id='discount_product_id')
                        ,   dict(id='discount_product_name')
                        ,   dict(id='discount_product_discount_category') 
                        ,   dict(id='discount_model')
                        ,   dict(id='discount_color')
                        ,   dict(id='discount_discount_group')
                        ,   dict(id='discount_discount_from')
                        ,   dict(id='discount_discount_to')
                        ,   dict(id='discount_eff')
                        ,   dict(id='discount_factor')                        

                        ,   dict(id='row_is_current')
                        ,   dict(id='row_start_date')
                        ,   dict(id='row_end_date')
                        ,   dict(id='row_change_reason')
                        ,   dict(id='import_version')
                        ,   dict(id='import_batch') 
                        ,   dict(id='import_user') 
                                ],

                        style_data={
                            'whiteSpace': 'normal',
                            'width': 'auto',
                            'height': 'auto',
                            'lineHeight': '15px'
                        },
                        #------------------------------------------------------------------------------------------------
                        # Vertical Scroll with fixed header
                        #------------------------------------------------------------------------------------------------
                    
                        #page_action='none', #render all of the data at once           
                        style_table={        
                            'height':'600px', # Vertical Scroll 
                            'overflowY': 'auto', #'scroll'
                            'overflowX': 'auto'
                            }, 
                        style_cell={
                            # all three widths are needed
                            'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                            'textAlign':'Right',
                        },
                        # style_cell_conditional=[
                        #     {
                        #         'if':{'column_id': c},
                        #         'textAlign': 'left'
                        #     } for c in ['description']
                        # ],
                        #------------------------------------------------------------------------------------------------
                        # Table as list (without vertical grid lines)
                        #------------------------------------------------------------------------------------------------

                        # style_as_list_view=False,

                        #------------------------------------------------------------------------------------------------
                        # Styling Table Header
                        #------------------------------------------------------------------------------------------------

                        # style_as_list_view=True,
                        # style_cell={'padding': '5px'}, # style_cell refers to the whole table
                        # style_header={
                        #       'backgroundColor':'white',
                        #       'fontWeight': 'bold',
                        #       'border': '2px solid black'
                        # },

                        fixed_rows={'headers':True},

                        #------------------------------------------------------------------------------------------------
                        # Striped Rows
                        #------------------------------------------------------------------------------------------------
                            # style_header = {
                            #   'backgroundColor': '#deebf7', #rgb(230, 230, 230)
                            #   'fontWeight': 'bold'
                            # },
                            # style_data_conditional=[  # style_data.c refers only to data rows
                            #       {
                            #           'if':{'row_index':'odd'},
                            #           'backgroundColor':'#f7fbff' #rgb(248, 248, 248)
                            #       }
                            # ],

                        #------------------------------------------------------------------------------------------------
                        # Dark Theme with Cells
                        #------------------------------------------------------------------------------------------------
                            # style_header={'backgroundColor':'rgb(30,30,30)'},
                            # style_cell={
                            #     'backgroundColor':'rgb(50,50,50)',
                            #     'color':'white',
                            #     'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            # },

                        #------------------------------------------------------------------------------------------------
                        # Highlighting Certain Rows
                        #------------------------------------------------------------------------------------------------

                            # style_data_conditional=[{
                            #     "if":{"row_index":4},
                            #     "backgroundColor":"#3D9970",
                            #     'color':'white',
                            #     "fontWeight":"bold",
                            #     'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            # }],

                        #------------------------------------------------------------------------------------------------
                        # Highlighting Certain Columns
                        #------------------------------------------------------------------------------------------------
                        
                            # style_data_conditional=[{
                            #     "if":{"column_id":'description'},
                            #     "backgroundColor":"#3D9970",
                            #     'color':'white',
                            #     "fontWeight":"bold",
                            #     'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            # }],

                        #------------------------------------------------------------------------------------------------
                        # Highlighting Certain Cells
                        #------------------------------------------------------------------------------------------------
                                
                            # style_data_conditional=[{
                            #     "if":{"column_id":'description'},
                            #     "backgroundColor":"#3D9970",
                            #     'color':'white',
                            #     "fontWeight":"bold",
                            #     'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            # }],

                        #------------------------------------------------------------------------------------------------
                        # Highlighting Certain Cells
                        #------------------------------------------------------------------------------------------------
            
                            # style_data_conditional=[{
                            #     "if":{"column_id":'description'},
                            #     "backgroundColor":"#3D9970",
                            #     'color':'white',
                            #     "fontWeight":"bold",
                            #     'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                            # }],

                        #------------------------------------------------------------------------------------------------
                        # Highlighting Certain Cells
                        #------------------------------------------------------------------------------------------------
            
                        # style_data_conditional = [
                        #     {
                        #         'if':{
                        #             'column_id': 'productkey',
                        #             'filter_query': '{productkey} eq 16'
                        #         },
                        #         'backgroundColor':'#3D9970',
                        #         'color': 'white',
                        #     },
                        #     {
                        #         'if': {
                        #             'column_id':'description',
                        #             'filter_query':'{description} eq "SHUTTER FRAMES"'
                        #         },
                        #         'backgroundColor': '#3D9970',
                        #         'color': 'white',  
                        #     },
                        #     {
                        #         'if':{
                        #             'column_id': 'mindeposit',
                        #             'filter_query': '{mindeposit} >39'
                        #         },
                        #         'backgroundColor': '#3D9970',
                        #         'color': 'white',
                        #     },
                        # ],

                        #------------------------------------------------------------------------------------------------
                        # Adding Borders
                        #------------------------------------------------------------------------------------------------
                            # style_data={'border': '1px solid red'},
                            # style_header={ 'border':'1px solid black'},

                        #------------------------------------------------------------------------------------------------
                        # Multi-Headers
                        #------------------------------------------------------------------------------------------------
                        
                            # columns=[
                            #     {"name": ["","Year"], "id": "year"},
                            #     {"name": ["City","Montreal"], "id":"montreal"},
                            #     {"name": ["City", "Toronto"], "id": "toronto"},
                            #     {"name": ["City", "Ottawa"], "id": "ottawa"}, 
                            #     {"name": ["City", "Vancouver"], "id": "vancouver"}, 
                            #     {"name": ["Climate", "Temperature"], "id": "temp"}, 
                            #     {"name": ["Climate", "Humidity"], "id": "humidity"}, 
                            # ],
                            # data=[
                            #     {
                            #         "year": i,
                            #         "montreal": i * 10,
                            #         "toronto": i * 100,
                            #         "ottawa": i * -1,
                            #         "vancouver": i * -10,
                            #         "temp": i * -100,
                            #         "humidity": i * 5,
                            #     }
                            #     for i in range(10)
                            #  ], 
                            #  merge_duplicate_headers=True,

                        #------------------------------------------------------------------------------------------------
                        # Styling Editable Columns
                        #------------------------------------------------------------------------------------------------
                            # columns=[
                            #     {'id': c, 'name': c, 'editable': (c == 'Humidity')}
                            #     for c in df.columns
                            # ],
                            # style_data_conditional=[{           # style_data refers only to data rows
                            #     'if': {'column_editable': False},
                            #     'backgroundColor': 'rgb(30, 30, 30)',
                            #     'color': 'white'
                            # }],
                            # style_header_conditional=[{         # style_header refers only to Header
                            #     'if': {'column_editable': False},
                            #     'backgroundColor': 'rgb(30, 30, 30)',
                            #     'color': 'white'
                            # }],

                        #----------------------------------------------------------------
                        # Styles Priority
                        #----------------------------------------------------------------
                            # There is a specific order of priority for the style_* properties. If there are
                            # multiple style_* props, the one with higher priority will take precedence.
                            # Within each prop, rules for higher indices will be prioritized over those for lower indices.
                            # Previously applied styles of equal priority win over later ones (applied top to bottom, left to right).
                            #
                            # These are the priorities of style_* props, in decreasing order:
                            #
                            # 1. style_data_conditional
                            # 2. style_data
                            # 3. style_filter_conditional
                            # 4. style_filter
                            # 5. style_header_conditional
                            # 6. style_header
                            # 7. style_cell_conditional
                            # 8. style_cell

                        #----------------------------------------------------------------
                        # Virtualization
                        #----------------------------------------------------------------
                            # virtualization=True, use when you have over 1000 and below 10000 rows not all data loads at once
            
                        #----------------------------------------------------------------
                        # Import Data from table
                        #----------------------------------------------------------------
            
                        data=df.to_dict('records'),
                            editable=False,
                        #filter_action="native",
                        sort_action="native",
                        sort_mode="multi",
                        #row_selectable="multi",
                        row_deletable=False,
                        selected_rows=[],
                        page_action="native",
                        page_size=10,
                        # if dataset has greater than 10,000 rows, look into using back end pagination with callbacks
                        # https://dash/plotly.com/datatable/callbacks
                        page_current= 0,


                        #page_size= 6,
                        # page_action='none',
                        # style_cell={
                        # 'whiteSpace': 'normal'
                        # },
                        # fixed_rows={ 'headers': True, 'data': 0 },
                        # virtualization=False,
                        # style_cell_conditional=[
                        #     {'if': {'column_id': 'country'},
                        #         'width': '40%', 'textAlign': 'left'},
                        #     {'if': {'column_id': 'deaths'},
                        #         'width': '30%', 'textAlign': 'left'},
                        #     {'if': {'column_id': 'cases'},
                        #         'width': '30%', 'textAlign': 'left'},
                        #     ]

                        export_format="csv",
                        )
    
                 )
         ])

        
    ]),

    dbc.Row([

        
    ]),

    dbc.Row([

        
    ]),

], fluid=True, style={'columnCount': 1, 'rowCount': 4})
#],style={'width':'100%'})

if __name__ == '__main__':
    app.run_server(debug=True)


# app.clientside_callback(
    
#     """
#     function (selected,n_clicks,data,columns) {
#         if (dash_clientside.callback_context.triggered.some(
#             ti => ti.prop_id === 'editing-rows-button.n_clicks'
#         )) {
#             data = data.slice();
#             newRow = {}
#             for (i in columns) {
#                 newRow[columns[i]['name']] = null
#             }
#             data.push(newRow)
#         }
#         console.log(dash_clientside.callback_context);
#         console.log(n_clicks)
#         console.log(data)
#         return data
#     }
#     """
#     ,

#     Output('table', 'data'),
#     [Input('table', 'active_cell'), Input('editing-rows-button', 'n_clicks')],
#     [Input('table', 'data'), State('table', 'columns')]
# )

@app.callback(
    Output('discount_table', 'data'),
    [Input('discount_table','active_cell')
    ,Input('my-date-picker-range', 'start_date')
    ,Input('my-date-picker-range', 'end_date')
    ,Input('demo-dropdown', 'value')
    ])

def update_table(interval, start_date, end_date, value):
    dim_discounts_df = Dim_discount.objects.all()
    dim_discounts_df = read_frame(dim_discounts_df)
    df = dim_discounts_df

    if value:
        df = df[df['discount_name'].isin(value)]
    else:
        pass
    # start_date = start_date.to_datetime()
    # end_date = end_date.to_datetime()
    if ((start_date and end_date)):
        df = df.loc[(df['row_end_date']>=start_date) & (df['row_end_date']<=end_date + dt.timedelta(days=10))]

    # for valu in value:
    #     df = df.loc[df['description']==valu]




    #df["product_group"] = df["product_group"].astype(str)#.astype(int)
    tabledata=df.to_dict('records')
    return tabledata
    print(interval)
