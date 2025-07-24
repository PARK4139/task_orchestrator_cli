

def play_wav_f(f):
    import os
    import pyglet
    # import pkg_py.system_object.static_logic as system_object.static_logic
    f = system_object.static_logic.F_POP_SOUND_POP_SOUND_WAV
    if os.path.exists(f):
        source = pyglet.media.load(f)
        source.play()
    pass
