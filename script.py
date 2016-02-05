import os
import datetime
from math import *
from PIL import Image, ImageDraw, ImageFont
import json

def key_sort_hosts(key):
    return int(hosts_of_heaven[key]['order'])

def position_str(deg_fl,positive = '',negative = '',type_return = 'str'):
        deg = abs(int(deg_fl))
        min = round(abs(deg_fl - int(deg_fl))*60)
        sec = 0
        NSEW = positive if deg_fl>0 else negative
        if type_return == 'str':
            return  str(deg) + '\u00b0' + NSEW + str(min) + '\u2032'
        elif type_return == 'min':
            return min
        elif type_return == 'deg':
            return deg
        else:
            return ''

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
                dict_settings_return['hosts_of_heaven'][key]['min'] = position_str(dict_settings_return['hosts_of_heaven'][key]['angle'],type_return='min')

    for key in dict_settings_default:
        if dict_settings.get(key):
            update_dict(dict_settings_default[key],dict_settings[key],key)
        else:
            dict_settings_return[key] = dict_settings_default[key] if type(dict_settings_default[key]) == type({}) else dict_settings_default[key]
    #format date/time
    date_of_birth_str = dict_settings_return['png']['date_of_birth']

    day = date_of_birth_str[:date_of_birth_str.find('/')]
    date_of_birth_str = date_of_birth_str[date_of_birth_str.find('/')+1:]
    month = date_of_birth_str[:date_of_birth_str.find('/')]
    year = date_of_birth_str[date_of_birth_str.find('/')+1:]
    date_of_birth_str = dict_settings_return['png']['time_of_birth']
    hour = date_of_birth_str[:date_of_birth_str.find(':')]
    min = date_of_birth_str[date_of_birth_str.find(':')+1:]
    dict_settings_return['png'].update({'date_time_of_birth':datetime.datetime(int(year),int(month),int(day),int(hour),int(min)).strftime("%a, %b %d, %Y  Time: %I:%M%p")})

    longitude_str = position_str(dict_settings_return['png']['longitude'],'W','E')
    latitude_str = position_str(dict_settings_return['png']['latitude'],'N','S')
    dict_settings_return['png'].update({'position_of_birth':'Lat: ' + latitude_str + ', Long: '+longitude_str})

    return dict_settings_return

def draw_birth_chart(path='', uid='', png={}):
    font = ImageFont.truetype(os.path.join(path, 'static', png['font_name']), 18)
    font_small = ImageFont.truetype(os.path.join(path, 'static', png['font_name']), 12)
    font_astro = ImageFont.truetype(os.path.join(path, 'static', png['font_name']), png['font_size_sign'])
    font_houses = ImageFont.truetype(os.path.join(path, 'static', png['font_name']), png['font_size_specification'])
    image = Image.new("RGBA", (png['pict_width'],png['pict_height']), (255,255,255,255))
    draw = ImageDraw.Draw(image)

    def draw_birth_chart_settings():
        #print birthchart ->start
        '''print birthchart settings'''
        str_date = str(datetime.datetime.now())
        font_title = ImageFont.truetype(os.path.join(path, 'static', 'fonts/Roboto-Bold.ttf'), 24)
        draw.text((png['padding']/2,png['padding']/4),png['name'],font=font_title,fill=(0,0,0,255))

        font_title = ImageFont.truetype(os.path.join(path, 'static', 'fonts/RobotoCondensed-Light.ttf'), 14)
        draw.text((png['padding']/3*2,png['padding']),png['date_time_of_birth'],font=font_title,fill=(0,0,0,255))
        draw.text((png['padding']/3*2,png['padding']*3/2+3),png['city_birth'],font=font_title,fill=(0,0,0,255))
        draw.text((png['padding']/3*2,png['padding']*2-2),png['position_of_birth'],font=font_title,fill=(0,0,0,255))
        draw.text((png['padding']/3*2,png['padding']*5/2),'Equal House System',font=font_title,fill=(0,0,0,255))

        draw.line ((png['pict_height'] + png['padding'],png['pict_height'] - png['padding'],png['pict_height']+png['padding'],png['padding']),fill=png['color_house_circle'])

        '''print hosts setings'''
        i = 0

        font_title = ImageFont.truetype(os.path.join(path, 'static', 'fonts/Roboto-Regular.ttf'), 24)
        y = png['padding']
        x = png['pict_height']+png['padding']+20
        draw.text((x-10,y/4),'Birth information',font=font_title,fill=(0,0,0,255))
        font_title = ImageFont.truetype(os.path.join(path, 'static', 'fonts/Roboto-Regular.ttf'), 14)
        for key in hosts:
            draw.text((x,y + i*20-3),hosts_of_heaven[key]['symbol'],font=font_houses,fill=hosts_of_heaven[key]['color'])
            draw.text((x+20,y + i*20),hosts_of_heaven[key]['name'],font=font_title,fill='Black')
            host_deg = hosts_of_heaven[key]['deg']
            delta_f = 0 if len(str(host_deg)) == 2 else 7
            draw.text((x+100+delta_f,y + i*20),str(hosts_of_heaven[key]['deg']) +'\u00b0',font=font_title,fill='Black')
            zodiac_str = zodiac_signs[hosts_of_heaven[key]['zodiac']]['abbreviation']
            zodiac_color = zodiac_signs[hosts_of_heaven[key]['zodiac']]['color']
            draw.text((x+130,y + i*20),zodiac_str,font=font_title,fill=zodiac_color)
            draw.text((x+160,y + i*20),str(hosts_of_heaven[key]['min']) +'\u2032',font=font_title,fill='Black')
            i+=1

        y = y + i*20
        i = 0
        delta_out = 0

        for key in sorted([int(x) for x in houses]):
            draw.text((x+delta_out,y + i*20),houses[str(key)]['symbol'],font=font_title,fill='Black')
            host_deg = houses[str(key)]['deg']
            delta_f = 0 if len(str(host_deg)) == 2 else 7
            draw.text((x+25+delta_f +delta_out,y + i*20),str(houses[str(key)]['deg']) +'\u00b0',font=font_title,fill='Black')
            zodiac_str = zodiac_signs[houses[str(key)]['zodiac']]['abbreviation']
            zodiac_color = zodiac_signs[houses[str(key)]['zodiac']]['color']
            draw.text((x+50 +delta_out,y + i*20),zodiac_str,font=font_title,fill=zodiac_color)
            draw.text((x+80 +delta_out,y + i*20),str(houses[str(key)]['min']) +'\u2032',font=font_title,fill='Black')

            if int(key)%2 == 0:
                delta_out = 120
            else:
                delta_out = 0
                i+=1

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
        font_astro = ImageFont.truetype(os.path.join(path, 'static', png['font_name']), png['font_size_planet'])
        i = 0
        r_planet_sign_circle = (png['r_degrees_circle'] + png['r_planet_circe'])/2
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

    def calc_aspects(angle,its_stets):
        for key in aspects:
            if aspects[key]['display'] == False:
                continue
            if (abs(aspects[key]['quantity']-angle)) < (aspects[key]['orbis_for_planets'] if its_stets==0 else aspects[key]['orbis_for_stets']):
                return key
        return None

    def draw_aspects():
        canvas_aspects = {}

        start_y = png['padding']
        font_title = ImageFont.truetype(os.path.join(path, 'static', 'fonts/Roboto-Regular.ttf'), 24)
        draw.text((png['pict_height']+png['padding']+270,start_y/4),'Natal aspects: ',font=font_title,fill='Black')
        font_title = ImageFont.truetype(os.path.join(path, 'static', 'fonts/Roboto-Regular.ttf'), 16)
        font_title_small = ImageFont.truetype(os.path.join(path, 'static', 'fonts/Roboto-Regular.ttf'), 12)
        aspect_number = 0
        i_count = 0
        for i in hosts:
            #print('i = ' + i + ' =>' + str(hosts_of_heaven[i]['angle']))
            i_count+=1
            planet_displayed = False
            for j in hosts[i_count:]:
                to = hosts_of_heaven[i]['angle'] #Point of departure
                tp = hosts_of_heaven[j]['angle'] #Point of arrival
                ad = 0 							 #Angular distance
                if tp < to:
                    ad = tp + 360 - to
                else:
                    ad = tp - to
                if ad > 180:
                    ad = 360 - ad

                aspect_of_2_planets = calc_aspects(ad,int(hosts_of_heaven[i]['stet'])*int(hosts_of_heaven[j]['stet']))

                if aspect_of_2_planets!=None:
                    #draw a line
                    draw.line((hosts_of_heaven[i]['x_y'],hosts_of_heaven[j]['x_y']),fill=aspects[aspect_of_2_planets]['color'])
                    x = int((hosts_of_heaven[i]['x']+hosts_of_heaven[j]['x'])/2)
                    y = int((hosts_of_heaven[i]['y']+hosts_of_heaven[j]['y'])/2)
                    draw.text((x,y),aspects[aspect_of_2_planets]['symbol'],font=font_small,fill=aspects[aspect_of_2_planets]['color'])
                    canvas_aspects[aspects[aspect_of_2_planets]['name'] + ' ' + hosts_of_heaven[j]['name'] + '<->' + hosts_of_heaven[i]['name']] ={
                                'description': 	aspects[aspect_of_2_planets]['name'] + ' ' + hosts_of_heaven[j]['name'] + '<->' + hosts_of_heaven[i]['name'] + '.Position: X = ' + str(x) + '; Y = ' + str(y) + '. Color - ' + str(aspects[aspect_of_2_planets]['color']),
                                'title':		aspects[aspect_of_2_planets]['name'] + ' ' + hosts_of_heaven[j]['name'] + '<->' + hosts_of_heaven[i]['name'],
                                'top':			y/png['pict_height']*100 - 1,
                                'left':			x/png['pict_height']*100 - 1,
                                'size':			2.5}


                    #x=png['pict_height']+350
                    x = png['pict_height']+png['padding']+20 + 270
                    y = start_y +aspect_number*20

                    if planet_displayed == False:
                        planet_displayed = True
                        aspect_number+=1
                        draw.text((x,y),hosts_of_heaven[i]['name'],font=font_title,fill=hosts_of_heaven[i]['color'])
                        y = start_y +aspect_number*20


                    draw.text((x+10,y),hosts_of_heaven[i]['symbol'],font=font_small,fill='Black')
                    draw.text((x+22,y),aspects[aspect_of_2_planets]['symbol'],font=font_small,fill='Black')
                    draw.text((x+34,y),hosts_of_heaven[j]['symbol'],font=font_small,fill='Black')
                    draw.text((x+46,y),hosts_of_heaven[j]['name'],font=font_title_small,fill='Black')
                    deg_min = str(position_str(ad,type_return = 'deg')) + "\u00b0 " + str(position_str(ad,type_return = 'min'))+ "\u2032 "
                    draw.text((x+110,y),deg_min,font=font_title_small,fill='Black')


                    aspect_number+=1
        draw.line ((png['pict_height'] + png['padding']+260,png['pict_height'] - png['padding'],png['pict_height']+png['padding']+260,png['padding']),fill=png['color_house_circle'])
        canvas_map.update(canvas_aspects)

    for i in sorted(houses):
        house_angle = houses[i]['angle']

        for j in zodiac_signs:
            sign_angle_start = (zodiac_signs[j]['order']-1)*30 + zodiaks_angle
            sign_angle_end = (zodiac_signs[j]['order'])*30 + zodiaks_angle

            if house_angle>=sign_angle_start and house_angle<sign_angle_end:
                houses[i]['zodiac'] = j
                zodiac_angle = zodiac_signs[j]['order']*30 + zodiaks_angle
        house_angel_in_zodiac = zodiac_angle - house_angle
        if house_angel_in_zodiac < 0:
            house_angel_in_zodiac = 360+house_angel_in_zodiac
        houses[i]['deg'] = position_str(house_angel_in_zodiac,type_return = 'deg')
        houses[i]['min'] = position_str(house_angel_in_zodiac,type_return = 'min')

    for i in hosts_of_heaven:
        host_angle = 360 - hosts_of_heaven[i]['angle']+zodiaks_angle
        if host_angle > 360:
            host_angle = host_angle - 360

        for j in zodiac_signs:
            sign_angle_start = (zodiac_signs[j]['order']-1)*30 + zodiaks_angle
            sign_angle_end = (zodiac_signs[j]['order'])*30 + zodiaks_angle

            if sign_angle_start < 0:
                sign_angle_start_1 = 360+(zodiac_signs[j]['order']-1)*30 + zodiaks_angle
                sign_angle_end_1 = 360

                sign_angle_start_2 = 0
                sign_angle_end_2 = (zodiac_signs[j]['order'])*30 + zodiaks_angle

                if (host_angle >= sign_angle_start_1 and host_angle < 360):
                    hosts_of_heaven[i]['zodiac'] = j
                elif host_angle>=0 and host_angle < sign_angle_end_2:
                    hosts_of_heaven[i]['zodiac'] = j
            else:
                if host_angle >= sign_angle_start and host_angle < sign_angle_end:
                    hosts_of_heaven[i]['zodiac'] = j

    canvas_map = {}
    draw_birth_chart_settings()
    draw_canvas()
    draw_sign()
    draw_planets()
    draw_aspects()

    for key in hosts_of_heaven:
        radian = radians(-hosts_of_heaven[key]['angle']+ zodiaks_angle + 180)
        #draw a planet dot on degree circle
        x = int(png['center_circle'] + cos(radian)*png['r_degrees_circle'])
        y = int(png['center_circle'] + sin(radian)*png['r_degrees_circle'])
        draw.ellipse([x-5,y-5,x+5,y+5], outline=hosts_of_heaven[key]['color'], fill = hosts_of_heaven[key]['color'])

        #draw a planet dot on planet circle
        x = int(png['center_circle'] + cos(radian)*png['r_planet_circe'])
        y = int(png['center_circle']+ sin(radian)*png['r_planet_circe'])
        draw.ellipse([x-5,y-5,x+5,y+5], outline=hosts_of_heaven[key]['color'], fill = hosts_of_heaven[key]['color'])

    image.save(os.path.join(path, 'static/results', 'img'+str(uid)+'.png'), "PNG")
    return {'param': canvas_map}