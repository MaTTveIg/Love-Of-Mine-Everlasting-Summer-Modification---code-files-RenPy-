label lmr_returner:
    $ renpy.quit()

label lmr_1945:

    python:

        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("lmr_quick_menu", None)]
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("lmr_say",None)]
        renpy.display.screen.screens[("quit",None)] = renpy.display.screen.screens[("lmr_leave",None)]
        renpy.display.screen.screens[("MainMenu",None)] = renpy.display.screen.screens[("lmr_leavemenu",None)]

    $ current_time = mainmenu_timeline()
    if 5 <= current_time < 16:
        scene menumain_anim_day_1
        $ renpy.music.play("mods/lmr/sounds/music/mainmenu_music_day.mp3", channel = "music", loop=True)
    elif 16 <= current_time < 20:
        scene menumain_anim_sunset_1
        $ renpy.music.play("mods/lmr/sounds/music/mainmenu_music_sunset.mp3", channel = "music", loop=True)
    elif 20 < current_time <= 23:
        scene menumain_anim_night_1
        $ renpy.music.play("mods/lmr/sounds/music/mainmenu_music_night.mp3", channel = "music", loop=True)
    elif 0 <= current_time < 5:
        scene menumain_anim_night_1
        $ renpy.music.play("mods/lmr/sounds/music/mainmenu_music_night.mp3", channel = "music", loop=True)

    call screen lmr_mainmenu with fade
    pause
