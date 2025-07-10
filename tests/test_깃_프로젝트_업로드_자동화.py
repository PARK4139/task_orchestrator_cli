def test_깃_프로젝트_업로드_자동화():
    from pkg_py.pk_core_constants import D_PROJECT
    from pkg_py.pk_core import get_time_as_, assist_to_upload_pnx_to_git
    from colorama import init as pk_colorama_init  # import 하면 엄청 느려짐
    pk_colorama_init(autoreset=True)

