def ensure_copied(str_working):
    import clipboard
    # Set-Clipboard -Value "텍스트"  # 클립보드에 텍스트 저장
    clipboard.copy(str_working)
    return str_working
