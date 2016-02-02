import os
import datetime
from math import *
from PIL import Image, ImageDraw, ImageFont
import json


def load_settings(path='', uid=''):
    file = open(os.path.join(path, 'static/results', 'settings_default.json'), 'r').read()
    dict_settings_default = json.loads(file)

    file = open(os.path.join(path, 'static/results', 'settings'+str(uid)+'.json'), 'r').read()
    dict_settings = json.loads(file)

    dict_settings_return = {}

    def update_dict(dict,dict2,branch):
        def format_list_to_tuple(dict):
            for key in dict:
                if type(dict[key]) == list:
                    dict[key] = tuple(dict[key])
                elif type(dict[key]) == type({}):
                    for key1 in dict[key]:
                        if type(dict[key][key1]) == list:
                            dict[key][key1] = tuple(dict[key][key1])

        if type(dict) == type({}):
            for key in dict:
                if type(dict[key]) == type({}):
                    dict[key].update(dict2.get(key,dict[key]))
                else:
                    dict[key] = dict2.get(key,dict[key])
            format_list_to_tuple(dict)
            dict_settings_return.update({branch:dict})
        else:
            dict_settings_return.update({branch:dict2 if dict2 else dict})

        if branch=='hosts_of_heaven':
            for key in dict_settings_return['hosts_of_heaven']:
                dict_settings_return['hosts_of_heaven'][key]['deg'] = int(dict_settings_return['hosts_of_heaven'][key]['angle'] % 30)
                dict_settings_return['hosts_of_heaven'][key]['min'] = int(dict_settings_return['hosts_of_heaven'][key]['angle'] % 1 *10)

    for key in dict_settings_default:
        if dict_settings.get(key):
            update_dict(dict_settings_default[key],dict_settings[key],key)
        else:
            dict_settings_return[key] = dict_settings_default[key] if type(dict_settings_default[key]) == type({}) else dict_settings_default[key]

    return dict_settings_return


def draw_birth_chart(path='', uid=''):
    font = ImageFont.truetype(png['font_name'], 18)
    font_small = ImageFont.truetype(png['font_name'], 12)
    font_astro = ImageFont.truetype(png['font_name'], png['font_size_sign'])
    font_houses = ImageFont.truetype(png['font_name'], png['font_size_specification'])
    image = Image.new("RGBA", (png['pict_width'],png['pict_height']), (255,255,255,255))
    draw = ImageDraw.Draw(image)

    def draw_birth_chart_settings():
        #print birthchart ->start
        '''print birthchart settings'''
        draw.text((png['pict_height']+150,png['padding']/3),'Birth chart parameters',font=ImageFont.truetype(png['font_name'], png['font_size_planet']),fill=png['color_house_circle'])
        draw.line ((png['pict_height'] + 120,png['pict_height'] - png['padding'],png['pict_height']+120,png['padding']),fill=png['color_house_circle'])
        draw.text((png['pict_height']+150,png['padding']/3 + 40),'Zodiac positions: ' + str(zodiaks_angle) + ' deg',font=font_houses,fill='Black')

        '''print hosts setings'''
        i = 0
        start_y = png['padding']/3 + 70
        for key in sorted(hosts_of_heaven):
            draw.text((png['pict_height']+150,start_y + i*20),hosts_of_heaven[key]['name'],font=font_houses,fill='Black')
            draw.text((png['pict_height']+230,start_y + i*20),hosts_of_heaven[key]['symbol'],font=font_houses,fill='Black')
            draw.text((png['pict_height']+250,start_y + i*20),str(hosts_of_heaven[key]['angle']),font=font_houses,fill='Black')
            i+=1

        '''print aspects settings'''
        start_y = start_y + i*20 + 20
        draw.text((png['pict_height']+150,start_y),'Aspects parameters*',font=font_houses,fill='Black')
        draw.text((png['pict_height']+330,start_y),'quant.',font=font_houses,fill='Black')
        draw.text((png['pict_height']+375,start_y),'+/-',font=font_houses,fill='Black')

        i=0
        start_y = start_y + i*20 + 20
        for key in sorted(aspects):
            if aspects[key]['display'] == False:
                draw.text((png['pict_height']+150,start_y + i*20),'off',font=font_houses,fill='Black')
            else:
                draw.text((png['pict_height']+150,start_y + i*20),'on',font=font_houses,fill='Black')
            draw.text((png['pict_height']+170,start_y + i*20),aspects[key]['name'],font=font_houses,fill='Black')
            draw.text((png['pict_height']+260,start_y + i*20),aspects[key]['symbol'],font=font_houses,fill='Black')

            draw.text((png['pict_height']+340,start_y + i*20),str(aspects[key]['quantity'])+str('\u00B0'),font=font_houses,fill='Black')
            draw.text((png['pict_height']+380,start_y + i*20),str(aspects[key]['orbis_for_planets'])+str('\u00B0'),font=font_houses,fill='Black')

            if aspects[key]['orbis_for_planets'] != aspects[key]['orbis_for_stets']:
                draw.text((png['pict_height']+400,start_y + i*20),'for stets: ' + str(aspects[key]['orbis_for_stets'])+str('\u00B0'),font=font_houses,fill='Black')
            i+=1
        draw.text((png['pict_height']+150,start_y + i*len(aspects) + 60),'* on - aspect displays, off - hidden ',font=font_houses,fill='Black')

    def draw_canvas():
        # draw 5 circles
        # outer house circle
        x1 = png['padding']
        x2 = png['pict_height'] - png['padding']
        draw.ellipse([x1,x1,x2,x2], outline=png['color_house_circle'])
        # outer zodiak circle
        x1 = png['padding']  + png['delta']/6
        x2 = png['pict_height'] - png['padding']  - png['delta']/6
        draw.ellipse([x1,x1,x2,x2], outline=png['color_zodiak_circle'])
        # inner zodiak circle
        x1 = png['padding']  + png['delta']*png['zodiac_percentage_circle']
        x2 = png['pict_height'] - png['padding']  - png['delta']*png['zodiac_percentage_circle']
        draw.ellipse([x1,x1,x2,x2], outline=png['color_zodiak_circle'])
        # inner house circle
        x1 = png['padding'] + png['delta']
        x2 = png['pict_height'] - png['padding'] - png['delta']
        draw.ellipse([x1,x1,x2,x2], outline=png['color_house_circle'])
        #planets circle
        x1 = png['center_circle'] - png['r_planet_circe']
        x2 = png['center_circle'] + png['r_planet_circe']
        draw.ellipse([x1,x1,x2,x2], outline=png['color_planet_circle'])

        str_date = str(datetime.datetime.now())
        draw.text((5,5),str_date,font=font,fill=(0,0,0,255))

            #draw a house circle
        """The scale is based on the 4-degree circles:
        1. The circle which is marked (base circle)
        2. The circle with degrees
        3. Circle with tens of degrees
        4. The outer circle (30 degrees)"""
        angle = zodiaks_angle
        radian = 0
        while angle < 360 + zodiaks_angle:
            #find a line coordinate
            radian = radians(angle)
            #start point coordinate
            r_start_point = 0;
            if (angle - zodiaks_angle)% 10 == 0:
                r_start_point = png['r_degrees_circle'] + png['delta']/6
            else:
                r_start_point = png['r_degrees_circle'] + png['delta']/12
            #start point coordinate
            x1 = png['center_circle'] + cos(radian)*r_start_point
            y1 = png['center_circle'] + sin(radian)*r_start_point
            if (angle - zodiaks_angle) % 30 == 0:
                draw.ellipse([x1-1,y1-1,x1+1,y1+1], outline=png['color_house_circle'], fill=png['color_house_circle'])
            #end point coordinate
            x2 = png['center_circle'] + cos(radian)*png['r_degrees_circle']
            y2 = png['center_circle'] + sin(radian)*png['r_degrees_circle']
            #draw a line
            draw.line ((x1,y1,x2,y2),fill=png['color_house_circle'])
            angle += 1

        #need another cycle, because may zodiaks_angle a non-integer
        angle = 0
        radian = 0
        while angle < 360:
            radian = radians(angle)
            #start point coordinate
            r_start_point = 0;
            if angle% 10 == 0:
                r_start_point = png['r_degrees_circle'] + png['delta']/6
            else:
                r_start_point = png['r_degrees_circle'] + png['delta']/12
            #start point coordinate
            x1 = png['center_circle'] + cos(radian)*r_start_point
            y1 = png['center_circle'] + sin(radian)*r_start_point

            if angle == 0:
                draw.text((png['center_circle']*2 -png['padding'] + 3,y1),'DESC',font=font_houses,fill=png['color_house_circle'])
            elif angle == 90:
                draw.text((x1-5 ,y1 + png['delta'] - 12),'I C',font=font_houses,fill=png['color_house_circle'])
            elif angle == 180:
                draw.text((x1 - png['delta'] - 5,y1-16),'ASC',font=font_houses,fill=png['color_house_circle'])
            elif angle == 270:
                draw.text((x1 - 14 ,y1 - png['delta']),'M C',font=font_houses,fill=png['color_house_circle'])

            r_start_point = png['r_house_circle'] + png['padding']/2 #it should be optimized
            x1 = png['center_circle'] + cos(-radian)*r_start_point
            y1 = png['center_circle'] + sin(-radian)*r_start_point

            if angle % 30 == 0:
                x11 = png['center_circle'] + cos(radian)*(png['r_house_circle']+30)
                y11 = png['center_circle'] + sin(radian)*(png['r_house_circle']+30)
                x22 = png['center_circle'] + cos(radian)*(png['r_house_circle']-2)
                y22 = png['center_circle'] + sin(radian)*(png['r_house_circle']-2)
                draw.line ((x11,y11,x22,y22),fill=png['color_house_circle'])
            offset = 5
            if angle == 195:
                draw.text((x1-offset ,y1-offset),'I',font=font,fill='black')
            elif angle == 225:
                draw.text((x1-offset,y1-offset),'II',font=font,fill='black')
            elif angle == 255:
                draw.text((x1-offset,y1-offset),'III',font=font,fill='black')
            elif angle == 285:
                draw.text((x1-offset,y1-offset),'IV',font=font,fill='black')
            elif angle == 315:
                draw.text((x1-offset,y1-offset),'V',font=font,fill='black')
            elif angle == 345:
                draw.text((x1-offset,y1-offset),'VI',font=font,fill='black')
            elif angle == 15:
                draw.text((x1-offset,y1-offset),'VII',font=font,fill='black')
            elif angle == 45:
                draw.text((x1-offset,y1-offset),'VIII',font=font,fill='black')
            elif angle == 75:
                draw.text((x1-offset,y1-offset),'IX',font=font,fill='black')
            elif angle == 105:
                draw.text((x1-offset,y1-offset),'X',font=font,fill='black')
            elif angle == 135:
                draw.text((x1-offset,y1-offset),'XI',font=font,fill='black')
            elif angle == 165:
                draw.text((x1-offset,y1-offset),'XII',font=font,fill='black')
            angle += 15

    def draw_sign():
        #draw a signs
        canvas_sign = {}
        i = 0
        r_sign_circle = png['r_degrees_circle'] + png['delta']*0.6
        for key in zodiac_signs:
            #draw a start line of zodiaks segments
            radian = radians(zodiac_signs[key]['order']*30 + zodiaks_angle)
            r_start_point = png['padding']  + png['delta']/6 - png['pict_height']/2
            r_end_point = png['padding']  + png['delta']*png['zodiac_percentage_circle'] - png['pict_height']/2
            #start point coordinate
            x1 = png['center_circle'] + cos(radian)*r_start_point
            y1 = png['center_circle'] + sin(radian)*r_start_point
            #end point coordinate
            x2 = png['center_circle'] + cos(radian)*r_end_point
            y2 = png['center_circle'] + sin(radian)*r_end_point
            #draw a line
            draw.line ((x1,y1,x2,y2),fill=png['color_zodiak_circle'])

            radian = radians(zodiac_signs[key]['order']*30 + zodiaks_angle - 15)

            r_start_point = (r_start_point + r_end_point)/2
            #start point coordinate
            x1 = png['center_circle'] + cos(radian)*r_start_point
            y1 = png['center_circle'] + sin(radian)*r_start_point
            # Here need new code, becouse its imperic
            canvas_sign[zodiac_signs[key]['name']] = {
                'description': 	'Position: X = ' + str(x1) + '; Y = ' + str(y1) + '. Color - ' + str(zodiac_signs[key]['color']),
                'title':		zodiac_signs[key]['name'],
                'top':			y1/png['pict_height']*100 - 9/2,
                'left':			x1/png['pict_height']*100 - 9/2,
                'size':			9}
            draw.text((x1 - png['pict_height']*0.06/3*2 +10,y1 - png['pict_height']*0.06/3*2),zodiac_signs[key]['symbol'],font=font_astro,fill=zodiac_signs[key]['color'])
        canvas_map.update(canvas_sign)

    def draw_planets():
        #draw a planet
        canvas_planets = {}
        font_astro = ImageFont.truetype(png['font_name'], png['font_size_planet'])
        i = 0
        r_planet_sign_circle = (png['r_degrees_circle'] + png['r_planet_circe'])/2
        #while i < len(hosts_of_heaven):
        for key in hosts_of_heaven:
            radian = radians(-hosts_of_heaven[key]['angle'] + zodiaks_angle + 180)

            #draw a planet dot on planet circle
            x = int(png['center_circle'] + cos(radian)*png['r_planet_circe'])
            y = int(png['center_circle']+ sin(radian)*png['r_planet_circe'])

            hosts_of_heaven[key]['x'] = x
            hosts_of_heaven[key]['y'] = y
            hosts_of_heaven[key]['x_y'] = (x,y)

            #draw a planet sign
            x = int(png['center_circle'] + cos(radian)*r_planet_sign_circle)- png['font_size_planet']/2
            y = int(png['center_circle'] + sin(radian)*r_planet_sign_circle)- png['font_size_planet']/2
            canvas_planets[hosts_of_heaven[key]['name']] ={
                'description': 	'Position: X = ' + str(x) + '; Y = ' + str(y) + '. Color - ' + str(hosts_of_heaven[key]['color']),
                'title':		hosts_of_heaven[key]['name'],
                'top':			y/png['pict_height']*100,
                'left':			x/png['pict_height']*100,
                'size':			3}
            draw.text((x,y),hosts_of_heaven[key]['symbol'],font=font_astro,fill=hosts_of_heaven[key]['color'])
            #image.paste(hosts_of_heaven[i]['icon'],(x-25,y-25),hosts_of_heaven[i]['icon'])

            #draw a digit sign
            x = int(png['center_circle'] + cos(radian)*(r_planet_sign_circle + png['r_degrees_circle'] + 10)/2)#тут надо будет подобрать проценты
            y = int(png['center_circle'] + sin(radian)*(r_planet_sign_circle + png['r_degrees_circle'] + 10)/2)
            draw.text((x-9,y-9),str(hosts_of_heaven[key]['deg']),font=font,fill=hosts_of_heaven[key]['number_color'])

            x = int(png['center_circle'] + cos(radian)*(r_planet_sign_circle + png['r_planet_circe'])/2)
            y = int(png['center_circle'] + sin(radian)*(r_planet_sign_circle + png['r_planet_circe'])/2)
            draw.text((x-6,y-6),str(hosts_of_heaven[key]['min']),font=font_small,fill=hosts_of_heaven[key]['number_color'])
        canvas_map.update(canvas_planets)

    canvas_map = {}
    draw_birth_chart_settings()
    draw_canvas()
    draw_sign()
    draw_planets()
    
    image.save(os.path.join(path, 'static/results', 'img'+str(uid)+'.png'), "PNG")
    return {'param': canvas_map}
"""
pathH = 'f:/Prj/py/NBC_Flask'

settings = load_settings(pathH)
zodiaks_angle = settings['zodiaks_angle'] # angle change fo degree
zodiac_signs = settings['zodiac']
hosts_of_heaven = settings['hosts_of_heaven']
aspects = settings['aspects']
png = settings['png']

h = draw_birth_chart(pathH)
"""