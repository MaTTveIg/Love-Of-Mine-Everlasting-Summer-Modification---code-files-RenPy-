screen lmr_say:
    window:
        background None
        id "window"
        if persistent.font_size == "small":
            imagebutton:
                auto ("mods/lmr/hud/log_%s.png")
                xpos -10
                ypos 870
                action ShowMenu("text_history")
            add ("mods/lmr/hud/lmr_dialogue_box.png"):
                xpos -5
                ypos 670
            imagebutton:
                auto ("mods/lmr/hud/hide_%s.png")
                xpos 1780
                ypos 815
                action HideInterface()
            imagebutton:
                auto ("mods/lmr/hud/menu_%s.png")
                xpos 1840
                ypos 815
                action ShowMenu('lmr_quick_menu')
            if not config.skipping:
                imagebutton:
                    auto ("mods/lmr/hud/skip_%s.png")
                    xpos 1740
                    ypos 880
                    action Skip()
            else:
                imagebutton:
                    auto ("mods/lmr/hud/skip_%s.png")
                    xpos 1740
                    ypos 880
                    action Skip()
            text what:
                id "what"
                xpos 220
                ypos 845
                xmaximum 1400
                size 45
                line_spacing 0.5
            if who:
                text who:
                    id "who"
                    xpos 150
                    ypos 750
                    size 60
                    line_spacing 3

screen lmr_quick_menu:


    modal True tag menu
    key "mousedown_1":
        action Return()
    key "game_menu":
        action Return()

    if (time_of_day == 'night'):
        add "mods/lmr/gui/lmr_qm_night.png" xalign 0.5 yalign 0.5
    elif (time_of_day == 'day'):
        add "mods/lmr/gui/lmr_qm_day.png" xalign 0.5 yalign 0.5
    elif (time_of_day == 'sunset'):
        add "mods/lmr/gui/lmr_qm_sunset.png" xalign 0.5 yalign 0.5
    vbox:

        style_prefix "quick"

        imagemap:
            cache True
            auto ("mods/lmr/gui/lmr_qm_%s.png")

            hotspot (805, 360, 500, 80) action Jump("lmr_1945")
            hotspot (800, 443, 500, 65) action ShowMenu("lmr_preferences_audio")
            hotspot (777, 509, 500, 80) action ShowMenu("lmr_leave")

screen lmr_mainmenu:


    modal True tag menu

    key "mousedown_1":
        action NullAction()
    key "game_menu":
        action NullAction()

    add "mods/lmr/gui/lmr_mainmenu_box.png"
    add "mods/lmr/gui/lmr_logo.png" xpos 650 ypos 50


    imagemap:
        cache True

        auto "mods/lmr/gui/main_menu_buttons_%s.png"

        hotspot (860, 555, 220, 84) action Jump("lmr_maingame")
        hotspot (860, 600, 214, 70) action ShowMenu("lmr_preferences_audio")
        hotspot (860, 660, 162, 70) action ShowMenu("lmrgallery")
        hotspot (860, 710, 150, 70) action Jump("lmr_returner")

    imagebutton:
        auto ("mods/lmr/gui/lmr_soviet_games_%s.png")
        xpos 1000
        ypos 835
        action OpenURL("https://www.sovietgames.su/")
    imagebutton:
        auto ("mods/lmr/gui/lmr_info_%s.png")
        xpos 675
        ypos 835
        action ShowMenu("lmr_info")

screen lmrgallery:
    tag menu

    add "mods/lmr/gallery/base.jpg"
    add "mods/lmr/gui/lmr_gallery_hover.png"
    add "mods/lmr/gui/lmr_illustration_idle.png"
    add "mods/lmr/gui/bgHeader.png" xpos 365 ypos 250

    key "mousedown_1":
        action NullAction()
    key "game_menu":
        action NullAction()

    hbox xpos 600 ypos 300:
        if persistent.cg1 == True:
            add lmrgal.make_button("cg1", "mods/lmr/gallery/poster1.jpg")
        else:
            add "mods/lmr/gui/hover_lmr.png"

    hbox xpos 1000 ypos 300:
        if persistent.cg2 == True:
            add lmrgal.make_button("cg2", "mods/lmr/gallery/poster2.png")
        else:
            add "mods/lmr/gui/hover_lmr.png"

    hbox xpos 1400 ypos 300:
        if persistent.cg3 == True:
            add lmrgal.make_button("cg3", "mods/lmr/gallery/poster3.png")
        else:
            add "mods/lmr/gui/hover_lmr.png"

    hbox xpos 600 ypos 500:
        if persistent.cg4 == True:
            add lmrgal.make_button("cg4", "mods/lmr/gallery/poster4.png")
        else:
            add "mods/lmr/gui/hover_lmr.png"

    hbox xpos 1000 ypos 500:
        if persistent.cg5 == True:
            add lmrgal.make_button("cg5", "mods/lmr/gallery/poster5.png")
        else:
            add "mods/lmr/gui/hover_lmr.png"

    hbox xpos 1400 ypos 500:
        if persistent.cg6 == True:
            add lmrgal.make_button("cg5", "mods/lmr/gallery/poster6.png")
        else:
            add "mods/lmr/gui/hover_lmr.png"

    imagebutton:
        auto ("mods/lmr/gui/back_arrow_%s.png")
        xpos 1640
        ypos 920
        action Return()

    imagemap:
        cache True
        auto ("mods/lmr/gui/lmr_audio_%s.png")

        hotspot (315, 490, 260, 74) action ShowMenu("lmr_preferences_audio")

    imagemap:
        cache True
        auto ("mods/lmr/gui/lmr_game_%s.png")

        hotspot (285, 535, 300, 110) action ShowMenu("lmr_preferences_game")

screen lmr_preferences_game:


    modal True tag menu

    key "mousedown_1":
        action NullAction()
    key "game_menu":
        action NullAction()

    add "mods/lmr/gallery/base.jpg"
    add "mods/lmr/gui/lmr_settings_game.png"
    add "mods/lmr/gui/lmr_game_idle.png"
    add "mods/lmr/gui/Audioheader.png" xpos 340 ypos 250

    bar:
        style "lmr_bars"
        value Preference("text speed")
        range 100
        left_bar "mods/lmr/gui/lmr_bar.png"
        xpos 590
        ypos 420

    bar:
        style "lmr_bars"
        value Preference("auto-forward time")
        range 100
        left_bar "mods/lmr/gui/lmr_bar.png"
        xpos 590
        ypos 560

    imagebutton:
        auto ("mods/lmr/gui/back_arrow_%s.png")
        xpos 1640
        ypos 920
        action Return()

    imagemap:
        cache True
        auto ("mods/lmr/gui/lmr_illustration_%s.png")

        hotspot (300, 610, 300, 95) action ShowMenu("lmrgallery")

    imagemap:
        cache True
        auto ("mods/lmr/gui/lmr_audio_%s.png")

        hotspot (310, 480, 260, 85) action ShowMenu("lmr_preferences_audio")

screen lmr_preferences_audio:


    modal True tag menu

    key "mousedown_1":
        action NullAction()
    key "game_menu":
        action NullAction()

    add "mods/lmr/gallery/base.jpg"
    add "mods/lmr/gui/lmr_settings_music.png"
    add "mods/lmr/gui/lmr_audio_idle.png"
    add "mods/lmr/gui/Audioheader.png" xpos 340 ypos 250

    bar:
        style "lmr_bars"
        value Preference("music volume")
        range 100
        left_bar "mods/lmr/gui/lmr_bar.png"
        xpos 800
        ypos 380

    bar:
        style "lmr_bars"
        value Preference("sound volume")
        range 100
        left_bar "mods/lmr/gui/lmr_bar.png"
        xpos 800
        ypos 480

    bar:
        style "lmr_bars"
        value Preference("voice volume")
        range 100
        left_bar "mods/lmr/gui/lmr_bar.png"
        xpos 800
        ypos 580

    imagebutton:
        auto ("mods/lmr/gui/back_arrow_%s.png")
        xpos 1640
        ypos 920
        action Return()

    imagemap:
        cache True
        auto ("mods/lmr/gui/lmr_illustration_%s.png")

        hotspot (300, 610, 316, 95) action ShowMenu("lmrgallery")

    imagemap:
        cache True
        auto ("mods/lmr/gui/lmr_game_%s.png")

        hotspot (285, 535, 300, 110) action ShowMenu("lmr_preferences_game")

screen lmr_leave:


    modal True tag menu

    key "mousedown_1":
        action NullAction()
    key "game_menu":
        action NullAction()

    imagemap:
        ground "mods/lmr/gui/lmr_leavegame.png"
        auto "mods/lmr/gui/lmr_yesno_%s.png"
        cache True

        hotspot (830, 600, 208, 66) action Jump("lmr_returner")
        hotspot (1035, 610, 210, 61) action Return()

screen lmr_leavemenu:


    modal True tag menu

    key "mousedown_1":
        action NullAction()
    key "game_menu":
        action NullAction()

    imagemap:
        ground "mods/lmr/gui/lmr_leavemenu.png"
        auto "mods/lmr/gui/lmr_yesno_%s.png"
        cache True

        hotspot (830, 600, 208, 66) action ShowMenu("main_menu")
        hotspot (1035, 610, 210, 61) action Return()

screen lmr_info:


    modal True tag menu
    add "mods/lmr/gallery/base_art.jpg"

    imagebutton:
        auto ("mods/lmr/gui/back_arrow_%s.png")
        xpos 1640
        ypos 920
        action ShowMenu("lmr_mainmenu")
