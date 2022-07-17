from py_trace_image import load_src_image


def test_load_image():
    load_src_image.image_name = "image2"
    load_src_image.image_extension = "jpg"
    load_src_image.image_orientation = "l"

    output = load_src_image.load_image()

    assert output is not None
