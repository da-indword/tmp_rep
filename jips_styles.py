from jips_colors import *
 
# Стили ipywidgets (для Jupyter (ipynb))
css_styles = '''
        <style>
            .all_widgets {
                margin-top: 15px; 
            }                
            .text_under_selects {                
                line-height: 0.5;
            }                
            .cell-output-ipywidget-background {
                background-color: transparent !important; 
            }                

            .one-pixel-select-style select {
                background-color: transparent !important; 
                border: transparent !important; 
            }                

            .my-label-style label {
'''
css_styles += f'''
                color: {all_colors[thems_colors]['font_color4']} !important;
                font-size: 16px;
'''
# селектор select html форм соответсвует виджету select
css_styles += ''' 
            }               
            .select-style select {                
'''
css_styles += f'''
                background-color: {all_colors[thems_colors]['back_color4']} !important;
                color: {all_colors[thems_colors]['font_color4']} !important;
                font-size: 16px;
'''
# чтобы добавить стиль для виджета BoundedIntText, используем 
# селектор input html форм, который, видимо, является родительским для BoundedIntText
css_styles += '''
            }
            input {                
'''
css_styles += f'''
                background-color: {all_colors[thems_colors]['back_color3']} !important;
                color: {all_colors[thems_colors]['font_color4']} !important;
                font-size: 16px;
'''
# селектор option:checked html форм позволяет создать стиль для 
# выделенной option виджетов Select
css_styles += '''
            }
            .option-select-style option:checked {                
'''
css_styles += f'''    
                background-color: {all_colors[thems_colors]['back_color3']} !important;
                color: {all_colors[thems_colors]['font_color5']} !important;
'''
css_styles += '''
            }
            .usual-text{
                font-size: 120%;
'''
css_styles += f'''    
                color: {all_colors[thems_colors]['font_color4']} ;
'''
css_styles += '''    
            }
            .usual-colored-text{
                font-size: 120%;
'''
css_styles += f'''    
                color: {all_colors[thems_colors]['font_color7']} ;
'''
# селекторы textarea, input html форм позволяют создать стили для 
# виджетов Textarea и BoundedIntText
css_styles += '''
            }
            textarea, input {
                font-family: system-ui;  
            }                
        </style>
'''        


ipywidgets_styles = {
        'warnings_style': dict(
            text_color = all_colors[thems_colors]['font_color2'],  
            font_size = '150%'    
        ), 

        'captions_style': dict(
            text_color = all_colors[thems_colors]['font_color7'],     
            font_size = '150%'    
        ), 

        'non_active_captions_style': dict(
            text_color = all_colors[thems_colors]['font_color9'],     
            font_size = '150%'    
        ), 

        'buttons_style': dict(
            font_size = '14pt',
            button_color = all_colors[thems_colors]['back_color6'],
            text_color = all_colors[thems_colors]['font_color8']     
        ), 

        'sent_id_style': dict(
            text_color = all_colors[thems_colors]['font_color6'],
            font_size = '20px'    
        ), 

        'sent_style': dict(
            text_color = all_colors[thems_colors]['font_color4'],
            font_size = '120%' 
        ), 

        'selected_sent_style': dict(
            text_color = all_colors[thems_colors]['font_color8'],
            font_size = '16px'    
        ), 

        'selected_sent_id_style': dict(
            text_color = all_colors[thems_colors]['font_color8'],
            font_size = '20px'    
        ), 

        'text_area_style': dict(
            font_size = '14pt',
            # Здесь этот цвет нужен для того, чтобы цвет шрифта контрастировал с цветом фона
            text_color = all_colors[thems_colors]['font_color4'],
            background = all_colors[thems_colors]['back_color4']            
        ), 

        'description_after_select_style': dict(
            text_color = all_colors[thems_colors]['font_color10'],            
            font_size = '12px',             
        ), 

        'star_in_text_style': dict(
            text_color = all_colors[thems_colors]['font_color11'],            
            font_size = '16px'    
        ),         

        'int_sliders_style': dict(
            handle_color = all_colors[thems_colors]['back_color2'], 

        ),         

}


df_styles = {
    
    'hover': {  # for row hover use <tr> instead of <td>
        'selector': 'tr:hover',                
        'props': [('background-color', all_colors[thems_colors]['back_color3'])]
    }, 

    'token_df_hover': {  
        'selector': 'tr:hover',                
        'props': [
            ('border', 'dotted ' + all_colors[thems_colors]['font_color14']), 
            # dotted dashed           
        ]         

    }, 

    # 'index_names': {
    #     'selector': '.index_name',
    #     # 'props': 'font-weight: normal; text-align: center; color: #99f7b4; '
    #     'props': [
    #         ('font-weight', 'normal'), 
    #         ('text-align', 'center'), 
    #         ('color', all_colors[thems_colors]['font_color5'])
    #     ]         
    # }, 

    'index_names': {
        'selector': '.index_name',
        'props': [
            ('font-weight', 'normal'), 
            ('font-size', '8pt'), 
            ('text-align', 'center'), 
            ('color', all_colors[thems_colors]['font_color4'])
        ]         
    }, 

    'token_df_index_names': {
        'selector': '.index_name',
        'props': [
            ('font-weight', 'normal'), 
            ('text-align', 'center'), 
            ('font-size', '10pt'), 
            ('color', all_colors[thems_colors]['font_color4'])            
        ]         
    }, 

    'headers': {
        'selector': 'th:not(.index_name)',
        # 'props': 'background-color: #01222A; color: #99f7b4; font-size: 12pt; text-align: center; '
        'props': [
            ('background-color', all_colors[thems_colors]['back_color4']), 
            ('color', all_colors[thems_colors]['font_color5']), 
            ('font-size', '12pt'), 
            ('text-align', 'center'),
        ]
    }, 

    # 'headers': {
    #     'selector': 'th',
    #     # 'props': 'background-color: #01222A; color: #99f7b4; font-size: 12pt; text-align: center; '
    #     'props': [
    #         ('background-color', all_colors[thems_colors]['back_color4']), 
    #         ('color', all_colors[thems_colors]['font_color12']), 
    #         ('font-size', '12pt'), 
    #         ('text-align', 'center'),
    #     ]
    # }, 

    'headers_wo_index_name': {
        'selector': 'th:not(.index_name)',
        # 'props': 'background-color: #01222A; color: #99f7b4; font-size: 12pt; text-align: center; '
        'props': [
            ('background-color', all_colors[thems_colors]['back_color4']), 
            ('color', all_colors[thems_colors]['font_color12']), 
            ('font-size', '12pt'), 
            ('text-align', 'center'),
        ]
    }, 

    'token_df_headers': {
        'selector': 'th:not(.index_name)',
        'props': [
            ('background-color', all_colors[thems_colors]['back_color4']), 
            ('color', all_colors[thems_colors]['font_color5']), 
            ('font-size', '15pt'), 
            ('text-align', 'center'),
        ]
    }, 

    'th_td': {
        'selector': 'th, td',
        'props': 'border-style: solid; border-width: 1px; text-align: center'            
    }, 

    # 'rows': {
    #     'selector': 'tr',
    #     'props': [
    #         ('background-color', all_colors[thems_colors]['back_color5']),
    #         ('text-align', 'center'),
    #     ]         
    # },                

    'rows': {
        'selector': 'tr',
        'props': [
            # ('background-color', all_colors[thems_colors]['back_color4']),
            ('background-color', all_colors[thems_colors]['back_color9']), 
            ('text-align', 'center'),
        ]         
    },                

}


not_equal_drs_back_color = all_colors[thems_colors]['back_color1']
actual_not_equal_drs_font_color = all_colors[thems_colors]['font_color1']
actual_equal_drs_font_color = all_colors[thems_colors]['font_color2']
not_actual_not_equal_drs_font_color = all_colors[thems_colors]['font_color3']
not_actual_equal_drs_font_color = all_colors[thems_colors]['font_color4']

highlight_font_size = '12pt'
headers_font_size = '14pt'
small_font_size = '10pt'


conditional_df_styles = {
    'actual_equal_drs_style': f'color: {actual_equal_drs_font_color}; text-align: center; ', 
    'actual_not_equal_drs_style': f'''
        background-color: {not_equal_drs_back_color}; font-size: {highlight_font_size};
        font-weight: bolder; text-align: center; color: {actual_not_equal_drs_font_color};
        ''', 
    'not_actual_not_equal_drs_style': f'''
        background-color: {not_equal_drs_back_color}; font-size: {highlight_font_size};  
        font-weight: bolder; text-align: center; color: {not_actual_not_equal_drs_font_color}; 
        ''',     
    'token_df_not_equal_drs_style': f'''
        font-size: {highlight_font_size};  
        font-weight: bolder; text-align: center; color: {actual_not_equal_drs_font_color}; 
        ''',     
    'not_actual_equal_drs_style': f'color: {not_actual_equal_drs_font_color}; ',
    'cols_headers': f'''
        background-color: {all_colors[thems_colors]['back_color4']}; 
        font-size: {highlight_font_size};  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color5']}; 
        ''',     
    'rows_headers': f'''
        background-color: {all_colors[thems_colors]['back_color4']}; 
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color5']}; 
        ''',     
    'subtable_headers': f'''
        background-color: {all_colors[thems_colors]['back_color4']}; 
        font-size: {headers_font_size};  
        font-weight: bolder; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color5']}; 
        ''',     
    'subtable_headers_rows': f'''
        background-color: {all_colors[thems_colors]['back_color4']};         
        ''',     
    # 'row_header_level0_label_is_not_feats': f'''
    #     background-color: {all_colors[thems_colors]['back_color4']};         
    #     ''',     
    # 'row_header_level0_label_is_child_feats': f'''
    #     background-color: {all_colors[thems_colors]['back_color4']};         
    #     ''',     
    # 'row_header_level0_label_is_head_feats': f'''
    #     background-color: {all_colors[thems_colors]['back_color4']};         
    #     ''',     

    'rows_labels_font': f'''
        color: {all_colors[thems_colors]['font_color5']}; 
        ''',     

    'row_header_level0_label_is_not_feats': f'''
        background-color: {all_colors[thems_colors]['back_color6']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color5']}; 

        ''',     
    'row_header_level0_label_is_child_feats': f'''
        background-color: {all_colors[thems_colors]['back_color4']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color5']}; 

        ''',     
    'row_header_level0_label_is_head_feats': f'''
        background-color: {all_colors[thems_colors]['back_color8']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color5']}; 

        ''',     

    'not_feats_not_equal_row': f'''
        background-color: {all_colors[thems_colors]['back_color6']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color13']}; 

        ''',     
    'child_feats_not_equal_row': f'''
        background-color: {all_colors[thems_colors]['back_color4']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color13']}; 
        ''',     

    'head_feats_not_equal_row': f'''
        background-color: {all_colors[thems_colors]['back_color6']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color13']}; 
        ''',     

    'not_feats_row': f'''
        background-color: {all_colors[thems_colors]['back_color6']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color4']}; 

        ''',     
    'child_feats_row': f'''
        background-color: {all_colors[thems_colors]['back_color4']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color4']}; 
        ''',     

    'child_feats_row': f'''
        background-color: {all_colors[thems_colors]['back_color6']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        color: {all_colors[thems_colors]['font_color4']}; 
        ''',     

    'not_feats': f'''
        background-color: {all_colors[thems_colors]['back_color4']};  
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        ''',     

    # 'not_feats': f'''
    #     background-color: {all_colors[thems_colors]['back_color6']};         
    #     font-size: {small_font_size };  
    #     font-weight: normal; 
    #     text-align: center; 
    #     ''',     

    'child_feats': f'''
        background-color: {all_colors[thems_colors]['back_color12']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        ''',     

    'head_feats': f'''
        background-color: {all_colors[thems_colors]['back_color6']};         
        font-size: {small_font_size };  
        font-weight: normal; 
        text-align: center; 
        ''',     

    'models_results_are_not_equal': f'''
        color: {all_colors[thems_colors]['font_color2']}; 
        ''',     

    'models_results_are_equal': f'''
        color: {all_colors[thems_colors]['font_color4']};         
        ''',     

}
        


