

def play_wav_f(f):
    import os
    import pyglet
    import pkg_py.pk_system_object.static_logic as pk_system_object.static_logic
    f = pk_system_object.static_logic.F_POP_SOUND_POP_SOUND_WAV
    if os.path.exists(f):
        source = pyglet.media.load(f)
        source.play()
    pass
