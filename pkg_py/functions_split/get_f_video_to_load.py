

def get_f_video_to_load(video_working_list):
    import os
    for f in video_working_list:
        f = f.strip()
        if os.path.exists(f):
            return f
    return None
