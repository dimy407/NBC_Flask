"""
https://books.google.com.ua/books?id=YaT9CAAAQBAJ&pg=PT615&lpg=PT615&dq=asc+desc+fcnhjkjubz+%D1%8D%D1%82%D0%BE&source=bl&ots=Uog0i09a3P&sig=UPeWcK1S4aGGoZ6aHhZW_wS_UTM&hl=ru&sa=X&ved=0ahUKEwiEga6PnJLKAhVG9HIKHWkXADkQ6AEIHDAA#v=onepage&q=asc%20desc%20fcnhjkjubz%20%D1%8D%D1%82%D0%BE&f=false

Не смасштабированы картинки
Не развернуты картинки	  
Не раскрашены карти
Найти иконки Chiron, Noth Nordб Pluto
Не нарисованы маленькие знаки зодиака
		  """

import os
import datetime
from math import *
from PIL import Image, ImageDraw, ImageFont
import json, sys


def update_parameters(p):
    """
    hh = {
        "zodiaks_angle": 15,
        "zodiac_signs": {
            "Aries": {
                "title": "Aries",
                "color": [237, 28, 36]
            }
        },
        "hosts_of_heaven": {
            "Sun": {
                "title": "Sun",
                "color": [255, 190, 0],
                "stet": 1,
                "angle": 34.9
            }
        },
        "aspects_settings": {
            "conjunction": {
                "title": "conjunction",
                "display": 1
            }
        }
    }

    if hh['zodiaks_angle'] != 0:
        p['zodiaks_angle'] = hh['zodiaks_angle']

    if len(hh['hosts_of_heaven']) > 0:
        i=0
        while i < len(hh['hosts_of_heaven']):


    try:
        f = open('F:/Prj/py/NBC_Flask/static/results/settings.json')
        new_param = json.loads(f.read())
    except:
        print("Неожиданная ошибка:", sys.exc_info()[0])
        return
        # raise
		
    """
    r = 1


def draw_img(path=''):
    # Settings -> start

    pict_width = 1500
    pict_height = 900
    padding = 45

    center_circle = pict_height / 2;  # we need only one coordinate, because circle in square
    r_house_circle = (pict_height - 2 * padding) / 2
    delta = int(pict_height * 0.15)
    r_degrees_circle = r_house_circle - delta  # it's circle for draw a graduated scale of degrees
    r_planet_circe = r_house_circle / 2.5
    zodiac_percentage_circle = 0.70

    color_house_circle = (0, 0, 0, 55)
    color_planet_circle = (0, 0, 0, 128)
    color_zodiak_circle = (255, 0, 0)

    font_size_sign = int(pict_height * 0.06)
    font_size_planet = int(pict_height * 0.03)
    font_size_specification = int(pict_height * 0.015)
    font_name = path + "/static/fonts/seguisym.ttf"
    font = ImageFont.truetype(font_name, 18)
    font_small = ImageFont.truetype(font_name, 12)
    font_astro = ImageFont.truetype(font_name, font_size_sign)
    font_houses = ImageFont.truetype(font_name, font_size_specification)

    zodiaks_angle = 12.45  # angle change fo degree
    zodiac_signs = [

        # ♈ Овен
        {'name': "Aries", 'symbol': '\u2648', 'color': (237, 28, 36)},  # 'icon': Image.open('zodiac/Aries.png')		},

        # ♓ Рыбы
        {'name': "Pisces", 'symbol': '\u2653', 'color': (0, 162, 232)},  # 'icon': Image.open('zodiac/Pisces.png')		},

        # ♒ Водолей
        {'name': "Aquarius", 'symbol': '\u2652', 'color': (255, 201, 14)},
        # 'icon': Image.open('zodiac/Aquarius.png')	},

        # ♑ Козерог
        {'name': "Capricorn", 'symbol': '\u2651', 'color': (237, 28, 36)},
        # 'icon': Image.open('zodiac/Capricorn.png')	},

        # ♐ Стрелец
        {'name': "Sagittarius", 'symbol': '\u2650', 'color': (237, 28, 36)},
        # 'icon': Image.open('zodiac/Sagittarius.png')},

        # ♏ Скорпиона
        {'name': "Scorpio", 'symbol': '\u264F', 'color': (0, 162, 232)},  # 'icon': Image.open('zodiac/Scorpio.png')	},

        # ♎ Весы
        {'name': "Libra", 'symbol': '\u264E', 'color': (181, 230, 29)},  # 'icon': Image.open('zodiac/Libra.png')		}

        # ♍ Дева
        {'name': "Virgo", 'symbol': '\u264D', 'color': (185, 122, 87)},  # 'icon': Image.open('zodiac/Virgo.png')		},

        # ♌ Лев
        {'name': "Leo", 'symbol': '\u264C', 'color': (237, 28, 36)},  # 'icon': Image.open('zodiac/Leo.png')		},

        # ♋ Рак
        {'name': "Cancer", 'symbol': '\u264B', 'color': (0, 162, 232)},  # 'icon': Image.open('zodiac/Cancer.png')		},

        # ♊ Близнецы
        {'name': "Gemini", 'symbol': '\u264A', 'color': (255, 201, 14)},  # 'icon': Image.open('zodiac/Gemini.png')		},

        # ♉ Телец
        {'name': "Taurus", 'symbol': '\u2649', 'color': (185, 122, 87)},  # 'icon': Image.open('zodiac/Taurus.png')		},

    ]

    hosts_of_heaven = [

        # ☉ Солнце (U+2609 Sun)
        {'name': "Sun", 'stet': 1, 'symbol': '\u2609', 'angle': 34.9, 'color': (255, 190, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},  # ,		'icon': Image.open('stars/Sun.png')						},#

        # ♄ Сатурн (U+2644 Saturn)
        {'name': "Saturn", 'stet': 0, 'symbol': '\u2644', 'angle': 306.6, 'color': (64, 32, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Saturn_symbol.png')			},

        # ♀ Венера (U+2640 Female sign)
        {'name': "Venus", 'stet': 0, 'symbol': '\u2640', 'angle': 30.0, 'color': (0, 204, 204), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Venus_symbol.png')			},

        # ♂ Марс (U+2642 Male sign)
        {'name': "Mars", 'stet': 0, 'symbol': '\u2642', 'angle': 67.5, 'color': (204, 0, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Mars_symbol.png')			},

        # ☊ Восходящий Узел или просто Узел (U+260A Ascending Node)
        {'name': "North Node", 'stet': 0, 'symbol': '\u260A', 'angle': 184.6, 'color': (0, 0, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (255, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('stars/North_Node.png')				},

        # ♃ Юпитер (U+2643 Jupiter)
        {'name': "Jupiter", 'stet': 0, 'symbol': '\u2643', 'angle': 97.2, 'color': (255, 190, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Jupiter_symbol.png')		},

        # ☽ Луна (U+263D First Quarter Moon)
        {'name': "Moon", 'stet': 1, 'symbol': '\u263D', 'angle': 44.9, 'color': (191, 191, 191), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('satellits/Moon_symbol_crescent.png')},

        # ♅ Уран (U+2645 Uranus)
        {'name': "Uranus", 'stet': 0, 'symbol': '\u2645', 'angle': 243.3, 'color': (204, 0, 204), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (255, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Uranus_symbol.png')			},

        # ⚸ Chiron
        {'name': "Chiron", 'stet': 0, 'symbol': '\u26B7', 'angle': 282.9, 'color': (0, 0, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Chiron_symbol.png')			},

        # ♆ Нептун (U+2646 Neptune)
        {'name': "Neptune", 'stet': 0, 'symbol': '\u2646', 'angle': 298.7, 'color': (0, 128, 89), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Neptune_symbol.png')		},

        # ☿ Меркурий (U+263F Mercury)
        {'name': "Mercury", 'stet': 0, 'symbol': '\u263F', 'angle': 21.2, 'color': (184, 204, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Mercury_symbol.png')		},

        # ♇ Плутон (U+2647 Pluto)
        {'name': "Pluto", 'stet': 0, 'symbol': '\u2647', 'angle': 345.8, 'color': (128, 0, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,		'icon': Image.open('planets/Pluto_symbol.png')			},

        # ⚸ Чёрная Луна или Лилит (U+26B8 Black Moon Lilith)
        {'name': "Lilith", 'stet': 0, 'symbol': '\u26B8', 'angle': 251.8, 'color': (128, 0, 0), 'deg': 0, 'min': 0,
         'x_y': (0, 0), 'number_color': (0, 0, 0), 'x': 0, 'y': 0},
        # ,	'icon': Image.open('planets/Pluto_symbol.png')			}
    ]

    aspects_settings = [

        #	Соединение	Гармоничный
        {'name': "conjunction", 'display': True, 'symbol': '\u260C', 'quantity': 0, 'orbis_for_planets': 5,
         'orbis_for_stets': 12, 'significant': 10, 'color': 'red'},  # 'significant':10 - Naren said that he needed it,

        # Полунонагон Кармический
        {'name': "seminonagon", 'display': False, 'symbol': '20\u00B0', 'quantity': 20, 'orbis_for_planets': 1,
         'orbis_for_stets': 1, 'significant': 1, 'color': 'Black'},
        # 'significant':5, I read in a textbook, it is important
        # Lines will be transpicuous
        # Полусекстиль Гармоничный
        {'name': "semisextile", 'display': True, 'symbol': '\u26Ba', 'quantity': 30, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 10, 'color': 'Gray'},  # 'significant': 1; it dosn't important
        # No lines
        # Полуквинтиль (дециль)	Semiquintile
        {'name': "decile", 'display': False, 'symbol': '36\u00B0', 'quantity': 36, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 1, 'color': 'Black'},

        # Нонагон
        {'name': "nonagon", 'display': False, 'symbol': '40\u00B0', 'quantity': 40, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 1, 'color': 'Black'},

        # Полуквадрат
        {'name': "semisquare", 'display': False, 'symbol': '45\u00B0', 'quantity': 45, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 5, 'color': 'Black'},

        # Секстиль
        {'name': "sextil", 'display': True, 'symbol': '\u26B9', 'quantity': 60, 'orbis_for_planets': 4,
         'orbis_for_stets': 4, 'significant': 10, 'color': 'Blue'},

        # Квинтиль
        {'name': "quintile", 'display': True, 'symbol': 'Q', 'quantity': 72, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 5, 'color': 'Black'},

        # Бананогон
        {'name': "bananogon", 'display': False, 'symbol': '80\u00B0', 'quantity': 80, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 1, 'color': 'Black'},

        # Квадрат
        {'name': "square", 'display': True, 'symbol': '\u25A1', 'quantity': 90, 'orbis_for_planets': 5,
         'orbis_for_stets': 5, 'significant': 10, 'color': 'Cyan'},

        # Сентагон
        {'name': "sentagon", 'display': False, 'symbol': '100\u00B0', 'quantity': 100, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 5, 'color': 'Black'},

        # Полутораквинтиль (тридециль)	Sesquiquintile
        {'name': "tridetsil", 'display': False, 'symbol': '108\u00B0', 'quantity': 108, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 1, 'color': 'Black'},

        # Трин
        {'name': "trine", 'display': True, 'symbol': '\u25B3', 'quantity': 120, 'orbis_for_planets': 6,
         'orbis_for_stets': 6, 'significant': 10, 'color': 'Gold'},

        # Полутораквадрат
        {'name': "sesquisquare", 'display': False, 'symbol': '135\u00B0', 'quantity': 135, 'orbis_for_planets': 3,
         'orbis_for_stets': 3, 'significant': 5, 'color': 'Black'},

        # Биквинтиль	Biquintil
        {'name': "biquintil", 'display': False, 'symbol': 'bQ', 'quantity': 144, 'orbis_for_planets': 2,
         'orbis_for_stets': 2, 'significant': 1, 'color': 'Black'},

        # Квиконс	or Inconjunct
        {'name': "quincunx", 'display': True, 'symbol': '\u26Bb', 'quantity': 150, 'orbis_for_planets': 3,
         'orbis_for_stets': 3, 'significant': 10, 'color': 'Chocolate'},

        # Опозиция
        {'name': "opposition", 'display': True, 'symbol': '\u260D', 'quantity': 180, 'orbis_for_planets': 5,
         'orbis_for_stets': 5, 'significant': 10, 'color': 'Pink'},
    ]
    # Settings <- end


    image = Image.new("RGBA", (pict_width, pict_height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)

    # print birthchart ->start
    draw.text((pict_height + 150, padding / 3), 'Birth chart parameters',
              font=ImageFont.truetype(font_name, font_size_planet), fill=color_house_circle)
    draw.line((pict_height + 120, pict_height - padding, pict_height + 120, padding), fill=color_house_circle)

    draw.text((pict_height + 150, padding / 3 + 40), 'Zodiac positions: ' + str(zodiaks_angle) + ' deg',
              font=font_houses, fill='Black')

    i = 0
    start_y = padding / 3 + 70
    while i < len(hosts_of_heaven):
        draw.text((pict_height + 150, start_y + i * 20), hosts_of_heaven[i]['name'], font=font_houses, fill='Black')
        draw.text((pict_height + 230, start_y + i * 20), hosts_of_heaven[i]['symbol'], font=font_houses, fill='Black')
        draw.text((pict_height + 250, start_y + i * 20), str(hosts_of_heaven[i]['angle']), font=font_houses,
                  fill='Black')
        i += 1

    start_y = start_y + i * 20 + 20
    draw.text((pict_height + 150, start_y), 'Aspects parameters*', font=font_houses, fill='Black')
    draw.text((pict_height + 330, start_y), 'quant.', font=font_houses, fill='Black')
    draw.text((pict_height + 375, start_y), '+/-', font=font_houses, fill='Black')
    i = 0
    start_y = start_y + i * 20 + 20
    while i < len(aspects_settings):
        if aspects_settings[i]['display'] == False:
            draw.text((pict_height + 150, start_y + i * 20), 'off', font=font_houses, fill='Black')
        else:
            draw.text((pict_height + 150, start_y + i * 20), 'on', font=font_houses, fill='Black')
        draw.text((pict_height + 170, start_y + i * 20), aspects_settings[i]['name'], font=font_houses, fill='Black')
        draw.text((pict_height + 260, start_y + i * 20), aspects_settings[i]['symbol'], font=font_houses, fill='Black')

        draw.text((pict_height + 340, start_y + i * 20), str(aspects_settings[i]['quantity']) + str('\u00B0'),
                  font=font_houses, fill='Black')
        draw.text((pict_height + 380, start_y + i * 20), str(aspects_settings[i]['orbis_for_planets']) + str('\u00B0'),
                  font=font_houses, fill='Black')

        if aspects_settings[i]['orbis_for_planets'] != aspects_settings[i]['orbis_for_stets']:
            draw.text((pict_height + 400, start_y + i * 20),
                      'for stets: ' + str(aspects_settings[i]['orbis_for_stets']) + str('\u00B0'), font=font_houses,
                      fill='Black')
        i += 1

    draw.text((pict_height + 150, start_y + i * len(aspects_settings) + 60), '* on - aspect displays, off - hidden ',
              font=font_houses, fill='Black')

    # print birthchart <-end


    # Calculation -> start
    i = 0
    while i < len(hosts_of_heaven):
        hosts_of_heaven[i]['deg'] = int(hosts_of_heaven[i]['angle'] % 30)
        hosts_of_heaven[i]['min'] = int(hosts_of_heaven[i]['angle'] % 1 * 10)
        i += 1
    # Calculation -> end

    # draw 5 circles
    # outer house circle
    x1 = padding
    x2 = pict_height - padding
    draw.ellipse([x1, x1, x2, x2], outline=color_house_circle)
    # outer zodiak circle
    x1 = padding + delta / 6
    x2 = pict_height - padding - delta / 6
    draw.ellipse([x1, x1, x2, x2], outline=color_zodiak_circle)
    # inner zodiak circle
    x1 = padding + delta * zodiac_percentage_circle
    x2 = pict_height - padding - delta * zodiac_percentage_circle
    draw.ellipse([x1, x1, x2, x2], outline=color_zodiak_circle)
    # inner house circle
    x1 = padding + delta
    x2 = pict_height - padding - delta
    draw.ellipse([x1, x1, x2, x2], outline=color_house_circle)
    # planets circle
    x1 = center_circle - r_planet_circe
    x2 = center_circle + r_planet_circe
    draw.ellipse([x1, x1, x2, x2], outline=color_planet_circle)

    str_date = str(datetime.datetime.now())
    draw.text((5, 5), str_date, font=font, fill=(0, 0, 0, 255))
    # draw a house circle
    """The scale is based on the 4-degree circles:
	1. The circle which is marked (base circle)
	2. The circle with degrees
	3. Circle with tens of degrees
	4. The outer circle (30 degrees)"""
    angle = zodiaks_angle
    radian = 0
    while angle < 360 + zodiaks_angle:
        # find a line coordinate
        radian = radians(angle)
        # start point coordinate
        r_start_point = 0;
        if (angle - zodiaks_angle) % 10 == 0:
            r_start_point = r_degrees_circle + delta / 6
        else:
            r_start_point = r_degrees_circle + delta / 12
        # start point coordinate
        x1 = center_circle + cos(radian) * r_start_point
        y1 = center_circle + sin(radian) * r_start_point
        if (angle - zodiaks_angle) % 30 == 0:
            draw.ellipse([x1 - 1, y1 - 1, x1 + 1, y1 + 1], outline=color_house_circle, fill=color_house_circle)
        # end point coordinate
        x2 = center_circle + cos(radian) * r_degrees_circle
        y2 = center_circle + sin(radian) * r_degrees_circle
        # draw a line
        draw.line((x1, y1, x2, y2), fill=color_house_circle)
        angle += 1

    # need another cycle, because may zodiaks_angle a non-integer
    angle = 0
    radian = 0
    while angle < 360:
        radian = radians(angle)
        # start point coordinate
        r_start_point = 0;
        if angle % 10 == 0:
            r_start_point = r_degrees_circle + delta / 6
        else:
            r_start_point = r_degrees_circle + delta / 12
        # start point coordinate
        x1 = center_circle + cos(radian) * r_start_point
        y1 = center_circle + sin(radian) * r_start_point

        if angle == 0:
            draw.text((center_circle * 2 - padding + 3, y1), 'DESC', font=font_houses, fill=color_house_circle)
        elif angle == 90:
            draw.text((x1 - 5, y1 + delta - 12), 'I C', font=font_houses, fill=color_house_circle)
        elif angle == 180:
            draw.text((x1 - delta - 5, y1 - 16), 'ASC', font=font_houses, fill=color_house_circle)
        elif angle == 270:
            draw.text((x1 - 14, y1 - delta), 'M C', font=font_houses, fill=color_house_circle)

        r_start_point = r_house_circle + padding / 2  # it should be optimized
        x1 = center_circle + cos(-radian) * r_start_point
        y1 = center_circle + sin(-radian) * r_start_point

        if angle % 30 == 0:
            x11 = center_circle + cos(radian) * (r_house_circle + 30)
            y11 = center_circle + sin(radian) * (r_house_circle + 30)
            x22 = center_circle + cos(radian) * (r_house_circle - 2)
            y22 = center_circle + sin(radian) * (r_house_circle - 2)
            draw.line((x11, y11, x22, y22), fill=color_house_circle)
        offset = 5
        if angle == 195:
            draw.text((x1 - offset, y1 - offset), 'I', font=font, fill='black')
        elif angle == 225:
            draw.text((x1 - offset, y1 - offset), 'II', font=font, fill='black')
        elif angle == 255:
            draw.text((x1 - offset, y1 - offset), 'III', font=font, fill='black')
        elif angle == 285:
            draw.text((x1 - offset, y1 - offset), 'IV', font=font, fill='black')
        elif angle == 315:
            draw.text((x1 - offset, y1 - offset), 'V', font=font, fill='black')
        elif angle == 345:
            draw.text((x1 - offset, y1 - offset), 'VI', font=font, fill='black')
        elif angle == 15:
            draw.text((x1 - offset, y1 - offset), 'VII', font=font, fill='black')
        elif angle == 45:
            draw.text((x1 - offset, y1 - offset), 'VIII', font=font, fill='black')
        elif angle == 75:
            draw.text((x1 - offset, y1 - offset), 'IX', font=font, fill='black')
        elif angle == 105:
            draw.text((x1 - offset, y1 - offset), 'X', font=font, fill='black')
        elif angle == 135:
            draw.text((x1 - offset, y1 - offset), 'XI', font=font, fill='black')
        elif angle == 165:
            draw.text((x1 - offset, y1 - offset), 'XII', font=font, fill='black')
        angle += 15

    # draw a signs
    canvas_map = {}
    i = 0
    r_sign_circle = r_degrees_circle + delta * 0.6
    while i < len(zodiac_signs):
        # draw a start line of zodiaks segments
        radian = radians(i * 30 + zodiaks_angle)
        r_start_point = padding + delta / 6 - pict_height / 2
        r_end_point = padding + delta * zodiac_percentage_circle - pict_height / 2
        # start point coordinate
        x1 = center_circle + cos(radian) * r_start_point
        y1 = center_circle + sin(radian) * r_start_point
        # end point coordinate
        x2 = center_circle + cos(radian) * r_end_point
        y2 = center_circle + sin(radian) * r_end_point
        # draw a line
        draw.line((x1, y1, x2, y2), fill=color_zodiak_circle)

        radian = radians(i * 30 + zodiaks_angle - 15)

        r_start_point = (r_start_point + r_end_point) / 2
        # start point coordinate
        x1 = center_circle + cos(radian) * r_start_point
        y1 = center_circle + sin(radian) * r_start_point
        # Here need new code, becouse its imperic
        canvas_map[zodiac_signs[i]['name']] = {
            'description': 'Position: X = ' + str(x1) + '; Y = ' + str(y1) + '. Color - ' + str(
                    zodiac_signs[i]['color']),
            'title': zodiac_signs[i]['name'],
            'top': y1 / pict_height * 100 - 9 / 2,
            'left': x1 / pict_height * 100 - 9 / 2,
            'size': 9}
        draw.text((x1 - pict_height * 0.06 / 3 * 2 + 10, y1 - pict_height * 0.06 / 3 * 2), zodiac_signs[i]['symbol'],
                  font=font_astro, fill=zodiac_signs[i]['color'])
        # if i == 0:
        #		draw.text((x1+20,y1+20),str(zodiaks_angle),font=font_small,fill=zodiac_signs[i]['color'])
        i += 1

    # draw a planet
    font_astro = ImageFont.truetype(font_name, font_size_planet)
    i = 0
    r_planet_sign_circle = (r_degrees_circle + r_planet_circe) / 2
    while i < len(hosts_of_heaven):
        radian = radians(-hosts_of_heaven[i]['angle'] + zodiaks_angle + 180)

        # draw a planet dot on planet circle
        x = int(center_circle + cos(radian) * r_planet_circe)
        y = int(center_circle + sin(radian) * r_planet_circe)

        hosts_of_heaven[i]['x'] = x
        hosts_of_heaven[i]['y'] = y
        hosts_of_heaven[i]['x_y'] = (x, y)

        # draw a planet sign
        x = int(center_circle + cos(radian) * r_planet_sign_circle) - font_size_planet / 2
        y = int(center_circle + sin(radian) * r_planet_sign_circle) - font_size_planet / 2
        canvas_map[hosts_of_heaven[i]['name']] = {
            'description': 'Position: X = ' + str(x) + '; Y = ' + str(y) + '. Color - ' + str(
                    hosts_of_heaven[i]['color']),
            'title': hosts_of_heaven[i]['name'],
            'top': y / pict_height * 100,
            'left': x / pict_height * 100,
            'size': 3}
        draw.text((x, y), hosts_of_heaven[i]['symbol'], font=font_astro, fill=hosts_of_heaven[i]['color'])
        # image.paste(hosts_of_heaven[i]['icon'],(x-25,y-25),hosts_of_heaven[i]['icon'])

        # draw a digit sign
        x = int(center_circle + cos(radian) * (
            r_planet_sign_circle + r_degrees_circle + 10) / 2)  # тут надо будет подобрать проценты
        y = int(center_circle + sin(radian) * (r_planet_sign_circle + r_degrees_circle + 10) / 2)
        draw.text((x - 9, y - 9), str(hosts_of_heaven[i]['deg']), font=font, fill=hosts_of_heaven[i]['number_color'])

        x = int(center_circle + cos(radian) * (r_planet_sign_circle + r_planet_circe) / 2)
        y = int(center_circle + sin(radian) * (r_planet_sign_circle + r_planet_circe) / 2)
        draw.text((x - 6, y - 6), str(hosts_of_heaven[i]['min']), font=font_small,
                  fill=hosts_of_heaven[i]['number_color'])

        i += 1

    # Draw aspects
    draw.text((pict_height + 20, padding / 3), 'Aspects', font=font_astro, fill=color_house_circle)
    draw.line((pict_height + 10, pict_height - padding, pict_height + 10, padding), fill=color_house_circle)

    font_astro = ImageFont.truetype(font_name, font_size_specification)
    i = 0
    number_aspects_10 = 0
    number_aspects_5 = 0
    number_aspects_1 = 0

    while i < len(hosts_of_heaven):
        j = i

        while j < len(hosts_of_heaven):
            if i != j:
                to = hosts_of_heaven[i]['angle']  # Point of departure
                tp = hosts_of_heaven[j]['angle']  # Point of arrival
                ad = 0  # Angular distance
                if tp < to:
                    ad = tp + 360 - to
                else:
                    ad = tp - to
                if ad > 180:
                    ad = 360 - ad
                y = 600 + j * (1.5 * font_size_specification) + padding
                k = 0
                while k < len(aspects_settings):
                    # it's stets?
                    if hosts_of_heaven[i]['stet'] * hosts_of_heaven[j]['stet'] == 1:
                        orbis = aspects_settings[k]['orbis_for_stets']
                    else:
                        orbis = aspects_settings[k]['orbis_for_planets']

                    if abs(ad - aspects_settings[k]['quantity']) <= orbis:
                        str_aspect = hosts_of_heaven[i]['symbol'] + " " + aspects_settings[k]['symbol'] + " " + \
                                     hosts_of_heaven[j]['symbol']
                        # Center line
                        x_center = (hosts_of_heaven[i]['x'] + hosts_of_heaven[j]['x']) / 2
                        y_center = (hosts_of_heaven[i]['y'] + hosts_of_heaven[j]['y']) / 2
                        color_aspects = aspects_settings[k]['color']
                        if aspects_settings[k]['significant'] == 10:
                            number_aspects_10 += 1
                            y = number_aspects_10 * (1.5 * font_size_specification) + padding
                            x = pict_height + padding
                            canvas_map[aspects_settings[k]['name'] + ' ' + hosts_of_heaven[j]['name'] + '<->' +
                                       hosts_of_heaven[i]['name']] = {
                                'description': aspects_settings[k]['name'] + ' ' + hosts_of_heaven[j]['name'] + '<->' +
                                               hosts_of_heaven[i]['name'] + '.Position: X = ' + str(x) + '; Y = ' + str(
                                        y) + '. Color - ' + str(aspects_settings[k]['color']),
                                'title': aspects_settings[k]['name'] + ' ' + hosts_of_heaven[j]['name'] + '<->' +
                                         hosts_of_heaven[i]['name'],
                                'top': y_center / pict_height * 100 - 1,
                                'left': x_center / pict_height * 100 - 1,
                                'size': 2.5}
                            draw.text((x_center - 8, y_center - 8), aspects_settings[k]['symbol'], font=font_astro,
                                      fill=color_aspects)
                        elif aspects_settings[k]['significant'] == 5:
                            number_aspects_5 += 1
                            y = number_aspects_5 * (1.5 * font_size_specification) + padding
                            x = pict_height + padding + 75
                        elif aspects_settings[k]['significant'] == 1:
                            number_aspects_1 += 1
                            y = number_aspects_1 * (1.5 * font_size_specification) + padding
                            x = pict_height + padding + 150
                        if aspects_settings[k]['display'] == True:
                            draw.text((x, y), str_aspect, font=font_astro, fill=color_aspects)
                            draw.line((hosts_of_heaven[i]['x_y'], hosts_of_heaven[j]['x_y']), fill=color_aspects)
                    k += 1
            j += 1
        i += 1

    i = 0
    while i < len(hosts_of_heaven):
        radian = radians(-hosts_of_heaven[i]['angle'] + zodiaks_angle + 180)
        # draw a planet dot on degree circle
        x = int(center_circle + cos(radian) * r_degrees_circle)
        y = int(center_circle + sin(radian) * r_degrees_circle)
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], outline=hosts_of_heaven[i]['color'],
                     fill=hosts_of_heaven[i]['color'])

        # draw a planet dot on planet circle
        x = int(center_circle + cos(radian) * r_planet_circe)
        y = int(center_circle + sin(radian) * r_planet_circe)
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], outline=hosts_of_heaven[i]['color'],
                     fill=hosts_of_heaven[i]['color'])

        i += 1

    canvas = {'param': canvas_map}

    # print(canvas)
    # j = json.dumps(canvas)
    # f = open('F:/Prj/py/NBC_Flask/static/results/test.json', 'w')
    # f.write(j)
    # f.close()
    image.save(path + "/static/results/test.png", "PNG")
    return canvas

# os.system(r'"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -url test.png')  # -url test.png
