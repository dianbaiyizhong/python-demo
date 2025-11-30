from image.ImageUtil import crop_circle_from_image, add_hollow_cylinder

for i in range(121):


    crop_circle_from_image(
        f"/Users/huanghaoming/Documents/GitHub/watch-face-studio-project/warriors_res/upscayl_png_upscayl-standard-4x_2x/simple_circle_warriors_{i:0>3}.png",
        f"/Users/huanghaoming/Documents/GitHub/watch-face-studio-project/warriors_res/upscayl_png_upscayl-standard-4x_2x/output/simple_circle_warriors_{i:0>3}.png",
        504, 486.5, 450)

    path = f"/Users/huanghaoming/Documents/GitHub/watch-face-studio-project/warriors_res/upscayl_png_upscayl-standard-4x_2x/output/simple_circle_warriors_{i:0>3}.png"
    add_hollow_cylinder(path,
                        f"/Users/huanghaoming/Documents/GitHub/watch-face-studio-project/warriors_res/upscayl_png_upscayl-standard-4x_2x/output2/simple_circle_warriors_{i:0>3}.png"
                        , 450, 290
                        )
