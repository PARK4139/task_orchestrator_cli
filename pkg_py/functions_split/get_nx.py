

def get_nx(pnx):
    import os
    
    # 리스트인 경우 첫 번째 요소 사용
    if isinstance(pnx, list):
        if len(pnx) > 0:
            pnx = pnx[0]
        else:
            return ""
    
    # 문자열이 아닌 경우 문자열로 변환
    if not isinstance(pnx, str):
        pnx = str(pnx)
    
    return rf"{os.path.splitext(os.path.basename(pnx))[0]}{os.path.splitext(os.path.basename(pnx))[1]}"
