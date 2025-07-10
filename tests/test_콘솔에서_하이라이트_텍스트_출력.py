def test_콘솔에서_하이라이트_텍스트_출력():
    from pkg_py.pk_core import LTA, get_txt_highlighted
    from pkg_py.pk_colorful_cli_util import pk_print
    sample_text = (
        "Python is a powerful programming language. "
        "C++ is also powerful. I love both Python and C++!"
    )
    highlight_config = {
        "bright_red": ["Python"],
        "bright_blue": ["C++"],
        "bright_green": ["powerful", "love"]
    }
    print(get_txt_highlighted(sample_text, highlight_config))
    pk_print(working_str=rf'''LTA={LTA}''', print_color='red')
    pk_print(working_str=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')

