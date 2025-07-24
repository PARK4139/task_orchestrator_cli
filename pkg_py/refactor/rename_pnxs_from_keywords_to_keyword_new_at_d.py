from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.pk_print import pk_print


def rename_pnxs_from_keywords_to_keyword_new_at_d(d, mode, with_walking, debug_mode=True):
    import inspect
    import re

    func_n = inspect.currentframe().f_code.co_name

    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]

    d_list = None
    working_list = None
    if with_walking == True:
        d_list, working_list = get_sub_pnx_list(pnx=d, txt_to_exclude_list=txt_to_exclude_list)
    else:
        d_list, working_list = get_sub_pnx_list(pnx=d, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    if mode == "f":
        pnxs = working_list
    elif mode == "d":
        pnxs = d_list
    else:
        pk_print(str_working=rf'''mode={mode}  {'%%%FOO%%%' if LTA else ''}''')
        return

    # pnxs에 "System Volume Information" 있으면 제외
    keywords_remove_pnxs_unnecessary = [
        "System Volume Information",
        "$RECYCLE.BIN",
    ]

    working_list = get_list_from_f(f=rf'{D_PKG_TXT}\collect_magnets_from_nyaa_si.txt')
    working_list = get_list_removed_element_contain_prompt(working_list=working_list, prompt="#")
    working_list = get_list_deduplicated(working_list=working_list)
    working_list = get_list_removed_empty(working_list=working_list)
    working_list = get_list_striped_element(working_list=working_list)
    pattern = re.compile(r"(\[.*?\])\s*(.*)")
    # filtered_list = []
    duplicated_stamp_list: list[tuple[str, str]] = []
    stamp_title_list: list[tuple[str, str]] = []
    for item in working_list:
        match = pattern.match(item)
        if match:
            # filtered_list.append((match.group(1), match.group(2)))
            stamp = match.group(1).strip()
            title = match.group(2).strip()
            if title != "":
                title_with_stamp = rf"{stamp} {title}"
                stamp_title_list.append((title, title_with_stamp))

            duplicated_stamp = rf"{stamp} {stamp}"
            duplicated_stamp_list.append((duplicated_stamp, stamp))

    duplicated_stamp_list = get_list_deduplicated(working_list=duplicated_stamp_list)

    keywords = [
                   # '_.. ', # referece : . 으로 끝나는 것 안된다.
                   # '"', # referece : 한글자 는 매우 유의해야한다.

                   # from x to ''
                   # ('_____', ''),
                   ('[jhp##]', ''),
                   ('[시작문자]', ''),
                   ('[끝문자]', ''),
                   ('[중복문자]', ''),

                   # from x to '_'
                   # ('_____', '_'),
                   ('[Multiple Subtitle]', '_'),
                   ('[1080p]', '_'),
                   ('[ x265-10Bit Ver_]', '_'),
                   (' - TV + SP', '_'),
                   ('RARBG', '_'), ('H264-3Li', '_'), ('_.UHD_.x264', '_'), ('_.x264-ORBS[rarbg]', '_'),
                   ('_.NF_DDP5.1.x264-AO', '_'), ('.x264.DTS-WAF', '_'), ('.PORTUGUESE_VXT', '_'), ('_.x264-CM', '_'),
                   ('_x265-', '_'), ('.ORIGINAL.UNRATED.CUT', '_'), ('_x265-', '_'), ('_-LCHD', '_'),
                   ('[5.1]', '_'),
                   (' dvdscr whd ', '_'), ('dvdrip', '_'), ('_H264.AAC', '_'), ('.iNTERNAL_-XME', '_'),
                   ('10bit.HDR.DV_.8CH.x265.HEVC-PSA', '_'),
                   ('Our.Blues.', '우리들의 블루스'),
                   ('.KOR.', '[한국]'), ('.KOR.FHDRip.H264.AAC-RTM', '_'), ('.10bit_6CH.x265.HEVC-PSA', '_'),
                   ('_.NF_DDP5.1.x264-NTG', '_'), ('_.DTS-SWTYBLZ', '_'), ('_.H264.AAC-VXT', '_'),
                   ('(_10bit Tigole)', '_'), ('WEB-DL.XviD.AC3-FGT', '_'), ('_.H264.AAC-VXT', '_'),
                   ('.Remux.DTS-HD.5.1', '_'),
                   ('.10bit_6CH.x265.HEVC-PSA', '_'), ('.AAC.5.1', '_'), ('AAC.5.1-POOP', '_'), ('_DD5.1', '_'),
                   ('_.AAC-Hon3y', '_'), ('.NF_DD5.1.x264-SiGMA', '_'), ('_HEVC_EAC3 5.1 Silence', '_'),
                   ('.1080p_H265.AAC-RGB', '_'), ('_H265.AAC-RGB', '_'), ('.DUBBED.', '_'), ('.1080p_x265-VXT', '_'),
                   ('ENSUBBED', '_'), ('1080p_.x264', '_'), ('1080p _ x264', '_'), (' _ _ ', '_'),
                   ('[YTS.AM]', '_'),
                   ('.2018.1080p', '[2018]'), ('.2018.', '[2018]'), ('.x265-VXT', '_'), ('.x265-', '_'),
                   ('_.bit_.ch.x_psa_', '_'), ('BluRay', '_'), ('_x264-', '_'), ('x264-SPARKS', '_'),
                   ('BluRay_HEVC_HDR AAC 7.1 Tigole', '_'), ('pkg_movie_horor', '[호러영화]'),
                   ('pkg_movie_image', '[영화이미지]'), ('pkg_movie_korean', '[한국영화]'),
                   ('pkg_movie_marvel_and_dc', '[marvel dc]'), ('pkg_movie_space', '[우주영화]'), ('pkg_sound', '[영화사운드]'),
                   ('x264-HANDJOB', '_'),
                   (' x265 ', '_'), (' HEVC ', '_'), (' 10bit ', '_'), (' EAC3 5.1 ', '_'), ('WEBRip.x264-RARBG', '_'),
                   ('WEB-DL.DD5.1.H264-FGT', '_'), ('KORSUB', '_'), ('DTS-FGT', '_'), ('BluRay.x265-RARBG', '_'),
                   ('#_movie_ #', '_'), ('[FOXM.TO]', '_'), ('[WEBRip]', '_'), ('[YTS.MX]', '_'),
                   ('[720p]', '_'),
                   ('[1080p]', '_'), ('[BluRay]', '_'), ('DTS-JYK', '_'), ('RARBG', '_'), ('BRRip', '_'),
                   ('.SPANISH.', '_'), ('.WEBRip.', '_'), ('-RARBG', '_'), ('[BLURAY]', '_'),
                   ('.BluRay.x265-RARBG', '_'), ('BluRay.H264.AAC-RARBG', '_'), ('KORSUB.WEBRip.H264.AAC', '_'),
                   ('.KOR.HDTC.H264.AAC_', '_'), ('y2meta.com', '_'), ('[YTS.AG]', '_'), ('[4K] _ [5.1]', '_'),
                   ('.WEB.AMZ_.AVC.DD5.1.x264-PANAM', '_'),
                   ('1080p.KORSUB.WEBRip.H264.AAC', '_'),
                   ('(1080p BluRay x265 RZeroX)', '_'),

                   # from x to y
                   # ('_____', '_____'),
                   ('_Toaru_Majutsu_no_Index_', 'Toaru Majutsu no Index'),
                   ('To Aru Kagaku', 'Toaru Kagaku'), ('To Aru Majutsu', 'Toaru Majutsu'),
                   ('[UTW-Mazui]', 'pk_ani'), ('[SubsPlease]', 'pk_ani'), ('[Erai-raws]', 'pk_ani'),
                   ('[Judas]', 'pk_ani'), ('[UTW-Mazui]', 'pk_ani'),
                   ('pk_ani', 'pk_ani '),  # todo : 추후삭제
                   ('pk_ani  ', 'pk_ani '),  # todo : 추후삭제
                   ('청설 Hear Me Our Summer, 2024', 'pk_movie 청설'),
                   ('pk_movie pk_movie', 'pk_movie'),
                   ('헨리', '(Henry)'),
                   ('The.Way.of.the.Househusband.', '극주부도 '),
                   ('극주부도', 'gokushufudo'),
                   ('크레이븐 더 헌터 Kraven the Hunter ,2024', '[마블영화]Kraven the Hunter 2024'),
                   ('아메바 소녀들과 학교괴담 개교기념일 ,2024', '아메바 소녀들과 학교괴담 개교기념일 2024'),
                   ('아마존 활명수 Amazon Bullseye, 2024', '아마존 활명수 2024'),
                   ('스콜피온 킹 The Scorpion King, 2002', 'Scorpion King 2002'),
                   ('브리드 Breathe, 2024.720p', 'Breathe 2024'),
                   ('정글의 법칙', '정글의_법칙'), ('정글의_법칙', '정글의법칙'),
                   ('로멘틱', '로맨틱'), ('로맨틱 이탈리아', '로맨틱이탈리아'),
                   ('[SEOA]', '[서아]'),
                   ('텐트 밖은 유럽', '텐트밖은유럽'),
                   ('Strange.Darling.2023', 'Strange Darling 2023'),
                   ('Crayon.Shinchan', 'Crayon Shinchan'),
                   ('공포의 기억 The Beast Within ,2024', 'The Beast Within 2024'),
                   ('A Herbivorous Dragon of 5000 Years Gets Unfairly Villainized',
                    'Yowai 5000-nen no Soushoku Dragon Iwarenaki Jaryuu Nintei'),
                   ('Meg.2.The.Trench.', 'Meg 2 The Trench'), ('[중복문자][중복문자][중복문자]', '[중복문자]'),
                   ('[중복문자][중복문자]', '[중복문자]'), (' 720p ', '[720p]'), ('The.', 'The '),
                   # The.mp3 라면 The mp3 가 되어 버려 문제가 될 우려가 됨
                   ('movie_ ', '영화'), ('.kra mvi ', '[한국영화]'), ('.kra mvi,', '[한국영화]'), ('포드 v 페라리', 'ford v ferrari'),
                   ('1080p', '[1080p]'), ('PMC 더 벙커 Take Point', '더 벙커[한국영화]'), ('.CHINESE.', '[중국]'),
                   ('.JAPANESE.', '[일본]'), ('공포_movie', '[공포영화]'), ('_movie_', '_영화_'), ('[한국_movie_]', '[한국영화]'),
                   ('[공포_movie_]', '[공포영화]'), ('kra mvi, ', '[한국영화]'), ('#일본_movie_', '[일본영화]'),
                   ('문경.2024', '문경 2024'),
                   # ('www.btranking.top - 최초배포', 'www.btranking.top - 최초배포.url'), # . 이 f명에 2개 있는 경우에 이동되지 않는데, 이동되도록 처리시도
                   # ('www.btranking.top - 최초배포.url.url', 'www.btranking.top - 최초배포.url'),# . 이 f명에 2개 있는 경우에 이동되지 않는데, 이동되도록 처리시도
                   # ('[TGx]Downloaded from torrentgalaxy.to .txt', '[TGx]Downloaded from torrentgalaxy_to .txt'),# . 이 f명에 2개 있는 경우에 이동되지 않는데, 이동되도록 처리시도
                   ('베놈 라스트 댄스', 'Venom The Last Dance'), ('Jeongnyeon The Star is Born', '정년이'), ('정년이.정년이', '정년이'),
                   ('Mungyeong.More.than.Roads', '문경'), ('#2023 #', '[PARK]'),
                   ('#2025 #', '[PARK]'), ('#2024 #', '[PARK]'), ('#2024 ', '[PARK]'), ('#영화  ', '[PARK]'),
                   ('#예능 ', '[PARK]'), ('#[PARK]', '[PARK]'), ('바운디', ' Vaundy'), ('mkr_', '[PARK]'),
                   ('#노래 #', '[PARK]'), ('_tvN_', '_'),
                   ('[Utaite_ sound ]', '[utaite]'), ('[Piano_Music]', '[piano]'), ('순수음성', '[순수음성]'), ('``', '[PARK]'),
                   ('[PARK]음악[PARK]', '[PARK]'), ('[PARK]', ' [PARK] '), ('[PARK]', ' '), ('. ', '_'), ('.___', '_'),
                   ('._', '_'), ('     ', ' '), ('    ', ' '), ('   ', ' '), ('  ', ' '),
                   ('______', '_'),
                   ('_____', '_'), ('____', '_'), ('___', '_'), ('__', '_'), ('2024.720p.WEBRip.H264.AAC', '[PARK]'),
                   ('`marvel `hero`', '[marvel]'), ('로키 시즌2', 'Loki 2'), ('왓 이프', 'what if'),
                   ('애니메이션', ' pk_ani'), ('애니', ' pk_ani'),
                   ('사진', '이미지'), ('이미지', '이미지'), ('그림', '이미지'), ('스샷', '이미지'), ('[우주_영화_]', '[우주영화]'),
                   ('[일본_영화_]', '[일본영화]'), ('#일본 _movie', '[일본영화]'), ('[한국_영화_]', '[한국영화]'),
                   ('Harry_Potter', 'Harry Potter'), ('music', ' sound '), ('sing', ' sound '), ('song', ' sound '),
                   ('``눈물', ' [눈물] '), ('언리얼 엔진', ' unreal engine '), ('언리얼엔진', ' unreal engine '),
                   ('언리얼5', ' unreal engine 5'),
                   ('언리얼 5', ' unreal engine 5'), ('緑黄色社会', '녹황색시사회'), ('_kra_', '[korea]'), ('_jpn_', '[japan]'),
                   ('``음악``', ' sound '), ('[고음질]', '_'),
                   ('【 ', '['), ('】 ', ']'), ('【 ', '['), ('】 ', ']'), ('( ', '['), ('『 ', '['), ('」 ', ']'),
                   ('《 ', '['), ('》 ', ']'),
                   ('[𝙇𝙤𝙤𝙠𝘽𝙤𝙤𝙠]', '[룩북]'), ('LOOKBOOK', '[룩북]'),
                   # 일본어 & 로마자소리 맵핑
                   # 순서가 요음 먼저 맵핑해야함
                   # 히라가나 요음
                   ("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo"), ("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho"),
                   ("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho"), ("にゃ", "nya"), ("にゅ", "nyu"), ("にょ", "nyo"),
                   ("ひゃ", "hya"), ("ひゅ", "hyu"), ("ひょ", "hyo"), ("みゃ", "mya"),
                   ("みゅ", "myu"),
                   ("みょ", "myo"), ("りゃ", "rya"), ("りゅ", "ryu"), ("りょ", "ryo"), ("ぎゃ", "gya"),
                   ("ぎゅ", "gyu"), ("ぎょ", "gyo"), ("じゃ", "ja"), ("じゅ", "ju"), ("じょ", "jo"), ("びゃ", "bya"),
                   ("びゅ", "byu"), ("びょ", "byo"), ("ぴゃ", "pya"), ("ぴゅ", "pyu"), ("ぴょ", "pyo"),
                   # 히라가나 모음 # k행  s행  t행  n행  h행  m행  y행  r행  w행
                   ("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o"), ("か", "ka"), ("き", "ki"),
                   ("く", "ku"), ("け", "ke"), ("こ", "ko"), ("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"),
                   ("そ", "so"), ("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to"),
                   ("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no"), ("は", "ha"), ("ひ", "hi"),
                   ("ふ", "fu"), ("へ", "he"), ("ほ", "ho"), ("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"),
                   ("も", "mo"), ("や", "ya"), ("ゆ", "yu"), ("よ", "yo"), ("ら", "ra"), ("り", "ri"), ("る", "ru"),
                   ("れ", "re"), ("ろ", "ro"), ("わ", "wa"), ("を", "wo"),
                   ("ん", "n"),  # 히라가나 특수
                   # 가타가나 요음
                   ("キャ", "kya"), ("キュ", "kyu"), ("キョ", "kyo"), ("シャ", "sha"), ("シュ", "shu"), ("ショ", "sho"),
                   ("チャ", "cha"), ("チュ", "chu"), ("チョ", "cho"), ("ニャ", "nya"), ("ニュ", "nyu"), ("ニョ", "nyo"),
                   ("ヒャ", "hya"), ("ヒュ", "hyu"), ("ヒョ", "hyo"), ("ミャ", "mya"),
                   ("ミュ", "myu"),
                   ("ミョ", "myo"), ("リャ", "rya"), ("リュ", "ryu"), ("リョ", "ryo"), ("ギャ", "gya"),
                   ("ギュ", "gyu"), ("ギョ", "gyo"), ("ジャ", "ja"), ("ジュ", "ju"), ("ジョ", "jo"), ("ビャ", "bya"),
                   ("ビュ", "byu"), ("ビョ", "byo"), ("ピャ", "pya"), ("ピュ", "pyu"), ("ピョ", "pyo"), ('ア', 'a'),
                   ('イ', 'i'), ('ウ', 'u'), ('エ', 'e'), ('オ', 'o'), ('カ', 'ka'), ('キ', 'ki'),
                   ('ク', 'ku'), ('ケ', 'ke'), ('コ', 'ko'), ('サ', 'sa'), ('シ', 'shi'), ('ス', 'su'), ('セ', 'se'),
                   ('ソ', 'so'), ('タ', 'ta'), ('チ', 'chi'), ('ツ', 'tsu'), ('テ', 'te'), ('ト', 'to'), ('ナ', 'na'),
                   ('ニ', 'ni'), ('ヌ', 'nu'), ('ネ', 'ne'), ('ノ', 'no'), ('ハ', 'ha'), ('ヒ', 'hi'), ('フ', 'fu'),
                   ('ヘ', 'he'), ('ホ', 'ho'), ('マ', 'ma'), ('ミ', 'mi'), ('ム', 'mu'), ('メ', 'me'),
                   ('モ', 'mo'), ('ヤ', 'ya'), ('ユ', 'yu'), ('ヨ', 'yo'), ('ラ', 'ra'), ('リ', 'ri'), ('ル', 'ru'),
                   ('レ', 're'), ('ロ', 'ro'), ('ワ', 'wa'), ('ヲ', 'wo'), ('ン', 'n'),
                   ("ン", "n"),  # 가타가나 특수
                   # 간자체
                   ("𝐘", "Y"), ("𝐱", "x"), ("𝐖", "W"), ("𝐑", "R"), ("𝐫", "r"), ("P", "P"), ("𝐨", "o"), ("𝐧", "n"),
                   ("𝐦", "m"), ("𝐥", "l"), ("𝐤", "k"), ("𝐠", "g"), ("𝐟", "f"), ("𝐞", "e"), ("𝐃", "D"), ("𝐁", "B"),
                   ("𝐀", "A"), ('𝐲', 'y'), ('𝐕', 'V'), ('𝐮', 'u'), ('𝐭', 't'), ('ｔ', 't'), ('𝐒', 'S'),
                   ('𝐬', 's'),
                   ('𝐏', 'P'), ('𝐨', 'o'), ('ｏ', 'o'), ('𝐧', 'n'), ('ｌ', 'l'), ('ｋ', 'k'), ('𝐢', 'i'), ('i', 'i'),
                   ('ｅ', 'e'), ('𝐝', 'd'), ('𝐜', 'c'), ('ｃ', 'c'), ('𝐚', 'a'),
                   # 특수문자
                   ('🌕', '_'), ('🔥', '_'), ('🗡️', '_'), ('💜', '_'), ('🎤', '_'), ('☆️', '_'), ('★', '_'), ('🛸', '_'),
                   ('🚬', '_'), ('🚪', '_'), ('🚨', '_'), ('🚘', '_'), ('🙆', '_'), ('😭', '_'), ('😥', '_'), ('😢', '_'),
                   ('😈', '_'), ('😆', '_'), ('😅', '_'), ('🧖', '_'), ('🧐', '_'), ('🦝', '_'), ('🥺', '_'),
                   ('🥩', '_'), ('🥜', '_'), ('🤸', '_'), ('🤴', '_'), ('🤫', '_'), ('🤡', '_'), ('🤘', '_'), ('🤗', '_'),
                   ('🤔', '_'),
                   ('🤓', '_'), ('🖐', '_'), ('🔹', '_'), ('🔮', '_'), ('🔍', '_'), ('📚', '_'), ('📁', '_'), ('💻', '_'),
                   ('💸', '_'), ('💪', '_'), ('💥', '_'), ('💡', '_'), ('💛', '_'), ('💚', '_'), ('💙', '_'), ('💖', '_'),
                   ('💔', '_'), ('💎', '_'), ('💍', '_'), ('💁', '_'), ('👹', '_'), ('👭', '_'), ('👗', '_'),
                   ('👖', '_'),
                   ('👍', '_'), ('👌', '_'), ('👋', '_'), ('👊', '_'), ('👄', '_'), ('🐶', '_'), ('🐠', '_'), ('🐟', '_'),
                   ('🏻', '_'), ('🏡', '_'), ('🎩', '_'), ('🎧', '_'), ('🎉', '_'), ('🍰', '_'), ('🍭', '_'), ('🍜', '_'),
                   ('🍒', '_'), ('🍃', '_'), ('🍂', '_'), ('🌺', '_'), ('🌹', '_'), ('🌸', '_'), ('🌷', '_'), ('🌡', '_'),
                   ('🌟', '_'), ('🌞', '_'), ('🌙', '_'), ('🌎', '_'), ('🌈', '_'), ('⭐', '_'), ('⧸', '_'),
                   ('➡', '_'),
                   ('❤', '_'), ('❗', '_'), ('❕', '_'), ('❓', '_'), ('❌', '_'), ('✿', '_'), ('✨', '_'), ('✧', '_'),
                   ('✦', '_'), ('✔', '_'), ('✅', '_'), ('🇹', '_'), ('🇷', '_'), ('🇰', '_'), ('🇮', '_'), ('⚡', '_'),
                   ('♬', '_'), ('♪', '_'), ('♩', '_'), ('♨', '_'), ('📝', '_'), ('🌱', '_'),
                   ('｜', '_'),
                   # 일본어 간자체 일부 맵핑 # 공부용 #아는 것만 추가 #같은문자 다른소리 처리 어떻게하지?
                   ("日", "日(nichi)"), ("人", "人(jin)"), ("本", "本(hon)"), ("大", "大(dai)"), ("中", "中(chuu)"),
                   ("小", "小(shou)"), ("山", "山(yama)"), ("川", "川(kawa)"), ("田", "田(ta)"), ("水", "水(sui)"),
                   ("火", "火(ka)"), ("木", "木(moku)"), ("金", "金(kin)"), ("土", "土(do)"),
                   ("空", "空(kuu)"),
                   ("天", "天(ten)"), ("海", "海(umi)"), ("心", "心(shin)"), ("愛", "愛(ai)"), ("学", "学(gaku)"),
                   ("生", "生(sei)"), ("車", "車(sha)"), ("電", "電(den)"), ("語", "語(go)"), ("書", "書(sho)"),
                   ("読", "読(doku)"), ("見", "見(ken)"), ("聞", "聞(bun)"), ("花", "花(hana)"), ("風", "風(kaze)"),
                   (']_[', ']['), ('_.. ', '_'), ('.._ ', '_'), ('._ ', '_'),
                   ('[$TIMESTAMP]', '_'),
                   (' e end hdtv once ', '_E_'),
                   ('.E.p_NEXT_', '_E_'),
                   (' e end hdtv once ', '_E_'),
                   ('hhd800.com@', '_'),
                   ('티비플', '[티비플]'), ('re제로', ' re zero '), ('리제로', ' re zero '), ('미스터 션샤인', ' 미스터션샤인'),
                   ('야나기나기', ' Nagi Yanagi'), ('피아노_음악', '[piano]'),
                   ('「', '['), ('】', ']'), ('」', ']'), ('【', '['), ('／', ' '), ('│', ' '),
                   ('이어폰 필수', '이어폰필수'),
                   ('우타이테', 'utaite'),
                   ('이어폰필수', '_'), ('편곡ver ', '_'), ('볼빨간 사춘기', '볼빨간사춘기'),
                   ('cover.鹿乃', '_'), ('#s #', '_'), ('[Leopard-Raws]', '_'),
                   ('메이플', '메이플스토리'), ('스토리스토리', '스토리'),
                   ('짐___캐리', '짐 캐리'), ('짐_캐리', '짐 캐리'),
                   ('케이tv', '_'), ('한글자막', '_'), ('1080P', '1080p'), ('1080p.H264-F1RST', '_'), ('[Moozzi2]', '_'),
                   # ('[[', '['),
                   # (']]', ']'),
                   # ('_)_)', '))'),
                   ('►', '_'), ('♫', '_'),
                   # '후회안합니다', '환영합니다', '합니다', '시작합니다', '소개합니다', '복잡합니다', '만들어야합니다', '공개합니다', '감사합니다',
                   # '[퓨전_음악]', '[ENG]', '[TM_sound]', '[치유정화]', '[울적해져요]', '[nightcore]', '[MV]', '[쇼! 음악중심]', '[쇼!_음악중심]', '[이어폰_소름]', '[이어폰_필수]', '[이어폰챙겻죠]', '[한국어 자막]', '[너무좋다]', '[소름 돋아요]', '[자작곡]', '[수정본]', '[TV]', '[CD]',
                   # 'Yang HeeEun', '판타스틱 듀오', '집중력 향상을 위한', '임금님랭킹2기오프닝', 'Fantastic Duo', '모던민요',
                   # "(ENG_SUB)"
                   # # 'playlist',
                   # # 'LIVE',
                   # '핫클립',
                   # '_., ', '_._ ',
                   # ' _ ', ' - ', '[_]', '___',
                   # '__', '  ',
                   # # "'",
                   # '|', '「️', '」️', '【', '】',
                   # # '+', '&',
               ] + stamp_title_list + duplicated_stamp_list * 2  # *2 를 해야 stamp 가 충분히 없어집니다.
    # for index, item in enumerate(keywords):
    #     pk_print(f'''keywords[{index}]={item}  {'%%%FOO%%%' if LTA else ''}''')

    # for index, item in enumerate(stamp_title_list):
    #     pk_print(f'''stamp_title_list[{index}]={item}  {'%%%FOO%%%' if LTA else ''}''')

    for index, item in enumerate(duplicated_stamp_list):
        pk_print(f'''duplicated_stamp_list[{index}]={item}  {'%%%FOO%%%' if LTA else ''}''')

    for keyword_removed in keywords_remove_pnxs_unnecessary:
        pnxs = [item for item in pnxs if
                keyword_removed not in item[0]]  # remove_element_to_have_"keywords_remove_dirs_unnecessary"
    # print_list_as_vertical(working_list=d_list, items_name="d_list")
    # print_list_as_vertical(working_list=f_list, items_name="f_list")
    pnxs_and_pnxs_new = []
    for item in pnxs:
        item_pnx = item[0]
        item_pnx_new = item_pnx  # item_pnx_로 초기화
        for keyword, keyword_new in keywords:
            item_p = get_p(pnx=item_pnx_new)
            item_nx = get_nx(pnx=item_pnx_new)
            item_nx_new = item_nx.replace(keyword, keyword_new)  # 누적하여 교체
            item_pnx_new = rf"{item_p}\{item_nx_new}"
        # pk_print(str_working=rf'''item_pnx="{item_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
        # pk_print(str_working=rf'''item_pnx_new="{item_pnx_new}"  {'%%%FOO%%%' if LTA else ''}''')
        if item_pnx != item_pnx_new:  # item_pnx_와 item_pnx_new가 다르면 추가
            pnxs_and_pnxs_new.append([item_pnx, item_pnx_new])

    # 확인
    pk_print(f'''pnxs_and_pnxs_new={pnxs_and_pnxs_new}  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''len(pnxs_and_pnxs_new)={len(pnxs_and_pnxs_new)} 바꿀 대상  {'%%%FOO%%%' if LTA else ''}''')

    # 적용
    rename_pnxs(pnx_list=pnxs_and_pnxs_new)
