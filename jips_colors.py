# Для автоматического определения, не тёмная ли тема в Windows
import darkdetect
if darkdetect.theme() == 'Dark': 
    thems_colors = 'dark_theme'

all_colors = {
    'dark_theme': {
        'back_color1': '#48ab82', # (not_equal_drs_back_color)        
        'back_color2': '#6df771',  # (ipywidget_slider.handle_color)
        'back_color3': '#03464F', # df_tr_hover
        'back_color4': '#01222A', # (df_th_headers, Textarea back)
        'back_color5': '#003440', # df_rows
        'back_color6': '#023c40', # (dark df color 6)
        'back_color7': '#05272b', # (dark df color 7)
        'back_color8': '#05292efc', # (dark df color 8)
        'back_color9': '#012c36', # (dark df color 9) 
        'back_color10': '#042a33', # (dark df color 10)        
        'back_color11': '#04333d', # (dark df color 11) # или 023440, 063945, 0a404d, 063945
        'back_color12': '#073036fc', # (dark df color 12)
        'back_color13': '#003642fc', # (dark df color 13)

        'font_color1': '#9c0808', # (actual_not_equal_drs_font_color)
        'font_color2': '#f73c02', # (actual_equal_drs_font_color)
        'font_color3': '#06345F', # (not_actual_not_equal_drs_font_color)
        'font_color4': 'white', # (usual font color)
        'font_color5': '#99f7b4', # (index_names_font_color)
        'font_color6': '#98FB98', # (separated sents ids)
        'font_color7': '#5dfc78', # (help font)        
        'font_color8': '#fad348', # (button text, title font)       
        'font_color9': '#18a86c', # (non active caption font)
        'font_color10': '#fcf87e', # (text under select widgets)
        'font_color11': '#f55e07', # (orange3)        
        'font_color12': '#fcd27e', # (token_df index_names_font_color)
        'font_color13': '#ff7221fc', # (token_df not equal font color)
        'font_color14': '#912107', # (dark red)        
        
        
        # Эти цвета тоже подходят: 
        # not_equal_drs_back_color: #48ab82, #4fb879, #4bd199, #54b079, #4b9982, #26bf91,
        # not_actual_not_equal_drs_font_color: #012236, #04233F, 
        # actual_not_equal_drs_font_color: #a32702, #9c0202, #9c0808
        # df_tr_hover: #094c5e, #073f4e, #003841, #03505D, #153E52, #093A41, #073C47, #04485B, #003A4A, #154659, #05384A, #164552, #0B3C43, 
        # button color: #003440 #03464F 
        # button text, title font: #ed3f09 #011445 #fad348 #fc530a 

    }, 

    'light_theme': {

    }
}
