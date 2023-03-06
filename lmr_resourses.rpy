init:
    $ mods["lmr_1945"]=u'{font=mods/lmr/fonts/Bayshore.ttf}{size=80}{color=#B35DD6}Love Of Mine{/color}{/size}{/font}'

    $ lmr_renpy_credits = "Love Of Mine\nБлагодарю Вас за прохождение данной модификации!\nP.S. эта заставка будет длинной, дабы вы насладились песней :3\nМодификация была написана под впечатлением от игры Love, Money, Rock-and-Roll\nЯ постарался повторить практически весь интерфейс ЛМР\nНа разработку ушли недели и сотни часов\nВсе спрайты и части для меню были вырезанны вручную\nНекоторые изображения могут быть мылом, из-за неудачного улучшения качества ИИ\nВсе права на визуальную часть остаются у Soviet Games\nИгровые файлы модификации не распространяются ни под каким предлогом\nВсе права на музыкальную часть остаются у их исполнителей\nМузыка из модификации\nLinking Park - One More Light\nLinking Park - Battle Symphony\nLinking Park - Nobody Can Save Me\nLinking Park - Sharp Edges\nLinking Park - Heavy\nLinking Park - Good Goodbye\nLinking Park - Invisible\nColdplay - Let Somebody Go\nМузыка из главного меню\nImagine Dragons - Selene\nImagine Dragons - Shots\nImagine Dragons - Cha-Ching(Till We Grow Older)\nМузыка из аутро\nImagine Dragons - Love Of Mine (Night Visions Demo)\nБлагодарности\nСпасибо Soviet Games за отличный способ выражать себя в простом коде\nСпасибо Imagine Dragons за их песни и мотивацию писать новые моды\nОтдельные благодарности\nWlad Goose - спасибо за помощь с оптимизацией кода / предоставлением нужных кусков кода / поиск мелочей для мода / участии в создании на среднем этапе\ndaboorlie - спасибо за помощь с декорацией и видоизминением оригинальных ЦГ из ЛМР\nОтдельное спасибо моему чату в телеграмме, который поддерживал меня на всём пути создания Love Of Mine\nВесь сценарий был написан ровно за 18 часов реального времени\nНа воссоздание всех меню ушло приблизительно 60 часов\nНа добычу всей визуальной части ушло приблизительно 30 часов\nНа превращение сценария код ушло более 5 часов\nХоть история и получилась крайне короткой, но это мой первый опыт в переписывании и переделывании части одной визуальной новеллы в другую\nМотивацию я нашёл от поддержки друзей и прекрасной музыки, которую я вставил в мод и слушал на репите всё то время, пока делал мод\nМне захотелось сделать первый, почти полноценный мод на ЛМР, инструментом для этого выступила мастерская БЛ\nЯ очень надеюсь, что вам понравилась визуальная и текстовая часть мода, особенно моргание всех спрайтов и эмоций в игре :3\nLove Of Mine - это не просто короткая история, не лишь возможноть стать лучше в любимом деле, это крупинки эмоций, которые я получил после прохождения рута Кэтрин в оригинальной игре\nЯ испытал крайне сильные эмоции, взглянул на фанатов ЛМР и БЛ, увидел ужас в мастерской и понял, что я первым должен обуздать этот проект\nДля меня это огромная честь сделать что-то подобное самым первым\nУверен, после этого мода множество других хороших мододелов решат перенять мой опыт, я буду только рад\n\nЭтот мод показывает хорошую концовку Кэтрин с другой стороны\nПокажут ли это лепестки? Узнаем, ведь мы совсем не близко, как Николай\n\nСпасибо за время уделённое моду!\n\nМодификация была создана MaTTveIg, при поддержке Wlad Goose"

    $ lmr_bar_value = 0

    $ nik_kun = Character(
        u'Николай', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#E9967A")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ lmr_thk = Character(
        name = None,  
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2) ], 
        what_drop_shadow_color = "000",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ nik_kun_boy = Character(
        u'Парень', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#E9967A")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ cat_girl = Character(
        u'Девушка', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#7B59EA")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ cat_lmr = Character(
        u'Кэтрин', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#7B59EA")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ ito_lmr = Character(
        u'Ито', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#ABB2B9")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ himi_sun = Character(
        u'Химицу', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#F8C471")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )

    $ teenager = Character(
        u'Школьник', 
        color="FFFFFF", 
        what_color="FFFFFF", 
        drop_shadow = [ (2, 2) ], 
        drop_shadow_color = "000", 
        what_drop_shadow = [ (2, 2), (2, 3), (1, 2) ], 
        what_drop_shadow_color = "000",
        who_outlines = [(3, "#808B96")],
        who_font = "mods/lmr/fonts/Arsenal-Bold.otf",
        what_font = "mods/lmr/fonts/ca-slalom-compressed-light.otf"
    )


    $ sakura_blossom = "mods/lmr/sounds/music/sakura_blossom.wav"
    $ batlle_symphony = "mods/lmr/sounds/music/batlle_symphony.mp3"
    $ one_more_light = "mods/lmr/sounds/music/one_more_light.mp3"
    $ sharp_edges = "mods/lmr/sounds/music/sharp_edges.mp3"
    $ nobody_can_save_me = "mods/lmr/sounds/music/nobody_can_save_me.mp3"
    $ good_godbye = "mods/lmr/sounds/music/good_godbye.mp3"
    $ invisible = "mods/lmr/sounds/music/invisible.mp3"
    $ heavy = "mods/lmr/sounds/music/heavy.mp3"
    $ let_smbd_go = "mods/lmr/sounds/music/let_smbd_go.mp3"


    $ room_mc_morning = "mods/lmr/sounds/ambience/room_mc_morning.wav"
    $ tokyo_street_day = "mods/lmr/sounds/ambience/tokyo_street_day.wav"
    $ garden_sunset = "mods/lmr/sounds/ambience/garden_sunset.wav"


    $ intercom_opened = "mods/lmr/sounds/sfx/intercom_opened.wav"


    image menumain_anim_day_1 = Movie(play = "mods/lmr/videos/menumain_anim_day.ogv", loop = True, size = (1920, 1080))
    image menumain_anim_sunset_1 = Movie(play = "mods/lmr/videos/menumain_anim_sunset.ogv", loop = True, size = (1920, 1080))
    image menumain_anim_night_1 = Movie(play = "mods/lmr/videos/menumain_anim_night.ogv", loop = True, size = (1920, 1080))
    image lmr_intro = Movie(play = "mods/lmr/videos/lmr_intro.ogv", loop = False, size = (1920, 1080))
    image lmr_autro = Movie(play = "mods/lmr/videos/lmr_autro.webm", loop = False, size = (1920, 1080))


    image lmr_house = im.Scale("mods/lmr/backgrounds/lmr_house.png",1920,1080)
    image lmr_street_local = im.Scale("mods/lmr/backgrounds/lmr_street_local.png",1920,1080)
    image lmr_street_day = im.Scale("mods/lmr/backgrounds/lmr_street_day.png",1920,1080)
    image lmr_house_of_himitsu = im.Scale("mods/lmr/backgrounds/lmr_house_of_himitsu.png",1920,1080)
    image lmr_centre_day = im.Scale("mods/lmr/backgrounds/lmr_centre_day.png",1920,1080)
    image lmr_school_close = im.Scale("mods/lmr/backgrounds/lmr_school_close.png",1920,1080)
    image lmr_bar_day = im.Scale("mods/lmr/backgrounds/lmr_bar_day.png",1920,1080)
    image lmr_school_corridor = im.Scale("mods/lmr/backgrounds/lmr_school_corridor.png",1920,1080)
    image lmr_corridor_day = im.Scale("mods/lmr/backgrounds/lmr_corridor_day.png",1920,1080)
    image lmr_garden_sunset = im.Scale("mods/lmr/backgrounds/lmr_garden_sunset.png",1920,1080)
    image lmr_house_of_himitsu = im.Scale("mods/lmr/backgrounds/lmr_house_of_himitsu.png",1920,1080)
    image lmr_cat_house_day = im.Scale("mods/lmr/backgrounds/lmr_cat_house_day.png",1920,1080)
    image lmr_lunapark_day = im.Scale("mods/lmr/backgrounds/lmr_lunapark_day.png",1920,1080)
    image lmr_bridge_night = im.Scale("mods/lmr/backgrounds/lmr_bridge_night.png",1920,1080)
    image lmr_water_night = im.Scale("mods/lmr/backgrounds/lmr_water_night.png",1920,1080)


    image lmr_sakura = Movie(play = "mods/lmr/backgrounds/lmr_sakura.webm", loop = True, size = (1980, 1080))
    image lmr_roomday = Movie(play = "mods/lmr/backgrounds/lmr_roomday.ogv", loop = True, size = (1980, 1080))
    image lmr_kitchenday = Movie(play = "mods/lmr/backgrounds/lmr_kitchenday.ogv", loop = True, size = (1980, 1080))
    image lmr_city = Movie(play = "mods/lmr/backgrounds/lmr_city.webm", loop = True, size = (1980, 1080))


    image fullposter2 = im.Scale("mods/lmr/gallery/fullposter2.png",1920,1080)
    image fullposter3 = im.Scale("mods/lmr/gallery/fullposter3.png",1920,1080)
    image fullposter4 = im.Scale("mods/lmr/gallery/fullposter4.png",1920,1080)
    image fullposter5 = im.Scale("mods/lmr/gallery/fullposter5.png",1920,1080)
    image fullposter6 = im.Scale("mods/lmr/gallery/fullposter6.png",1920,1080)


    image fullmain_screen_lmr = im.Scale("mods/lmr/gui/fullmain_screen_lmr.png",1920,1080)


init python:
    def mainmenu_timeline():
        import datetime
        current_time = datetime.datetime.now()
        return current_time.hour    

    config.mouse = {"default" : [("mods/lmr/gui/default_cursor.png", 0, 0)]}

    lmrgal = Gallery()

    lmrgal.locked_button = "mods/lmr/gui/hover_lmr.png"

    lmrgal.button("cg1")
    lmrgal.condition("persistent.cg1")
    lmrgal.image("mods/lmr/gallery/fullposter1.jpg")

    lmrgal.button("cg2")
    lmrgal.condition("persistent.cg2")
    lmrgal.image("mods/lmr/gallery/fullposter2.png")

    lmrgal.button("cg3")
    lmrgal.condition("persistent.cg3")
    lmrgal.image("mods/lmr/gallery/fullposter3.png")

    lmrgal.button("cg4")
    lmrgal.condition("persistent.cg4")
    lmrgal.image("mods/lmr/gallery/fullposter4.png")

    lmrgal.button("cg5")
    lmrgal.condition("persistent.cg5")
    lmrgal.image("mods/lmr/gallery/fullposter5.png")

    lmrgal.button("cg6")
    lmrgal.condition("persistent.cg6")
    lmrgal.image("mods/lmr/gallery/fullposter6.png")

style lmr_bars:
    right_bar "mods/lmr/gui/lmr_bar.png"
    thumb "mods/lmr/gui/lmr_htumb.png"
    thumb_offset 9.5
    xysize (560, 75)












image cat_doesntmatter_full_1_1:
    "mods/lmr/sprites/position1_1/cat_doesntmatter.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position1_1/cat_doesntmatter_blink.png"
    pause 0.25
    repeat

image cat_smile_full_1_1:
    "mods/lmr/sprites/position1_1/cat_smile.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position1_1/cat_smile_blink.png"
    pause 0.25
    repeat

image cat_sohappy_full_1_2:
    "mods/lmr/sprites/position1_2/cat_sohappy.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position1_2/cat_sohappy_blink.png"
    pause 0.25
    repeat

image cat_angry_full_2_1:
    "mods/lmr/sprites/position2_1/cat_angry.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position2_1/cat_angry_blink.png"
    pause 0.25
    repeat

image cat_sad_full_2_1:
    "mods/lmr/sprites/position2_1/cat_sad.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position2_1/cat_sad_blink.png"
    pause 0.25
    repeat

image cat_surprise_2_1:
    "mods/lmr/sprites/position2_1/cat_surprise.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position2_1/cat_surprise_blink.png"
    pause 0.25
    repeat

image cat_sad_2_2:
    "mods/lmr/sprites/position2_2/cat_sad.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/position2_2/cat_sad_blink.png"
    pause 0.25
    repeat

image ito_full:
    "mods/lmr/sprites/ito/ito_normal.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/ito/ito_blink.png"
    pause 0.25
    repeat

image himi_sad_full:
    "mods/lmr/sprites/himi/himi_sad.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/himi/himi_sad_blink.png"
    pause 0.25
    repeat

image himi_smile_full:
    "mods/lmr/sprites/himi/himi_smile.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/himi/himi_smile_blink.png"
    pause 0.25
    repeat

image himi_normal_full:
    "mods/lmr/sprites/himi/himi_normal.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/himi/himi_normal_blink.png"
    pause 0.25
    repeat

image himi_what_full:
    "mods/lmr/sprites/himi/himi_what.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/himi/himi_what_blink.png"
    pause 0.25
    repeat

image himi_sohappy_full:
    "mods/lmr/sprites/himi/himi_sohappy.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/himi/himi_sohappy_blink.png"
    pause 0.25
    repeat

image himi_disagree_full:
    "mods/lmr/sprites/himi/himi_disagree.png"
    choice:
        pause 3
    choice:
        pause 1.5
    choice:
        pause 5
    "mods/lmr/sprites/himi/himi_disagree_blink.png"
    pause 0.25
    repeat