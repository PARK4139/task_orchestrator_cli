




def play_wav_f(f):
    from sources.objects.task_orchestrator_cli_files import F_POP_SOUND_POP_SOUND_WAV
    import os
    import pyglet
    f = F_POP_SOUND_POP_SOUND_WAV
    if os.path.exists(f):
        source = pyglet.media.load(f)
        source.play()
    pass
