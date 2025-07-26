



def convert_mkv_to_wav(file_mkv):
    ensure_command_excuted_to_os_like_person_as_admin(rf'ffmpeg -i "{file_mkv}" -ab 160k -ac 2 -ar 44100 -vn {get_pn(file_mkv)}.wav')
