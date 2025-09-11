# 파일 확장자 상수 정의
# 대소문자 대응을 위해 소문자로 통일하여 저장

# 이미지 파일 확장자
IMAGE_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', 
    '.svg', '.ico', '.raw', '.heic', '.heif', '.tga', '.ppm', 
    '.pgm', '.pbm', '.xpm', '.xbm', '.pcx', '.dib', '.jfif'
}

# 비디오 파일 확장자
VIDEO_EXTENSIONS = {
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', 
    '.m4v', '.3gp', '.ogv', '.ts', '.mts', '.m2ts', '.vob',
    '.asf', '.rm', '.rmvb', '.divx', '.xvid', '.h264', '.h265'
}

# 오디오 파일 확장자
AUDIO_EXTENSIONS = {
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a',
    '.opus', '.amr', '.ra', '.mid', '.midi', '.aiff', '.au',
    '.cda', '.wv', '.ape', '.alac', '.dts', '.ac3'
}

# 문서 파일 확장자
DOCUMENT_EXTENSIONS = {
    '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages',
    '.tex', '.md', '.markdown', '.html', '.htm', '.xml', '.json',
    '.csv', '.xls', '.xlsx', '.ppt', '.pptx', '.key', '.odp'
}

# 아카이브 파일 확장자
ARCHIVE_EXTENSIONS = {
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.lzma',
    '.cab', '.arj', '.ace', '.lha', '.lzh', '.uue', '.xxe',
    '.z', '.lz', '.lz4', '.zstd', '.br'
}

# 코드 파일 확장자
CODE_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.scss',
    '.java', '.cpp', '.c', '.h', '.hpp', '.cs', '.php', '.rb',
    '.go', '.rs', '.swift', '.kt', '.scala', '.pl', '.sh', '.bat',
    '.ps1', '.vbs', '.sql', '.r', '.m', '.dart', '.lua'
}

# 데이터 파일 확장자
DATA_EXTENSIONS = {
    '.json', '.xml', '.csv', '.sql', '.db', '.sqlite', '.sqlite3',
    '.xlsx', '.xls', '.ods', '.yaml', '.yml', '.toml', '.ini',
    '.cfg', '.conf', '.log', '.dat', '.bin', '.dbf', '.mdb'
}

# 모든 확장자를 하나의 딕셔너리로 통합
FILE_EXTENSIONS = {
    'images': IMAGE_EXTENSIONS,
    'videos': VIDEO_EXTENSIONS,
    'audios': AUDIO_EXTENSIONS,
    'documents': DOCUMENT_EXTENSIONS,
    'archives': ARCHIVE_EXTENSIONS,
    'code': CODE_EXTENSIONS,
    'data': DATA_EXTENSIONS
}

# 대소문자 대응을 위한 헬퍼 함수
def get_extensions_with_case_variations(extensions_set):
    """
    확장자 세트에 대소문자 변형을 추가하여 반환
    
    Args:
        extensions_set: 확장자 세트 (예: {'.jpg', '.png'})
    
    Returns:
        대소문자 변형이 포함된 확장자 세트
    """
    result = set(extensions_set)
    for ext in extensions_set:
        if ext.startswith('.'):
            # 대문자 변형 추가
            result.add(ext.upper())
            # 첫 글자만 대문자 변형 추가 (예: .Jpg)
            result.add(ext[0] + ext[1:].upper())
    
    return result

# 대소문자 대응이 포함된 확장자 세트들
IMAGE_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(IMAGE_EXTENSIONS)
VIDEO_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(VIDEO_EXTENSIONS)
AUDIO_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(AUDIO_EXTENSIONS)
DOCUMENT_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(DOCUMENT_EXTENSIONS)
ARCHIVE_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(ARCHIVE_EXTENSIONS)
CODE_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(CODE_EXTENSIONS)
DATA_EXTENSIONS_CASE_INSENSITIVE = get_extensions_with_case_variations(DATA_EXTENSIONS)

# 대소문자 대응이 포함된 통합 딕셔너리
FILE_EXTENSIONS_CASE_INSENSITIVE = {
    'images': IMAGE_EXTENSIONS_CASE_INSENSITIVE,
    'videos': VIDEO_EXTENSIONS_CASE_INSENSITIVE,
    'audios': AUDIO_EXTENSIONS_CASE_INSENSITIVE,
    'documents': DOCUMENT_EXTENSIONS_CASE_INSENSITIVE,
    'archives': ARCHIVE_EXTENSIONS_CASE_INSENSITIVE,
    'code': CODE_EXTENSIONS_CASE_INSENSITIVE,
    'data': DATA_EXTENSIONS_CASE_INSENSITIVE
}
