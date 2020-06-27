__VERSION__ = '0.0.1'

from imagerie_lite.imagerie import (order_4_coordinates_clockwise, remove_lonely_small_objects, biggest_contour,
                                    get_biggest_contour, closest_point, get_corners, warp_perspective,
                                    warp_homography, image_composite_with_mask, combine_two_images_with_mask,
                                    prepare_for_prediction_single, prepare_for_prediction, fill_holes,
                                    remove_smaller_objects)

from imagerie_lite.operations.img import img_as_uint, img_as_float, img_as_bool