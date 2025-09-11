def convert_img_to_img_cropped(img_pnx, abs_x: int, abs_y: int, width_px: int, height_px: int):
    import inspect
    from PIL import Image
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    img_converted = Image.open(img_pnx).crop((abs_x, abs_y, width_px, height_px))
    img_converted.show()
