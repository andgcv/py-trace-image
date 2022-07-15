from py_trace_image import load_write_image

def test_load_image():
    load_write_image.image_name = "image"
    load_write_image.image_extension = "jpg"
    output = load_write_image.load_image()
    assert output is not None