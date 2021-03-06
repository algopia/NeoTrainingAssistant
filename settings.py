# -*- coding: utf-8 -*-

# get cropped images
flag_save_crop = True

# report dump for unintended interruption
flag_report_dump = True
report_dump_interval = 3

# after create annotation, remove src images
flag_remove_src = False

# crop ratio (width / height)
# if you want make ratio free, set 0
# or you want square, set 1
aspect_ratio = 0

# image-size limit in main window
limit_upper_width  = 600
limit_upper_height = 450
limit_lower_width  = 400
limit_lower_height = 300

# button alert
alert_click_clear   = True      # when click 'Clear'
alert_click_overall = True      # when click 'Overall'
alert_click_dismiss = True      # when click 'Dismiss'
alert_click_skip    = False     # when click 'Skip'
alert_click_next    = False     # when click 'Next'
