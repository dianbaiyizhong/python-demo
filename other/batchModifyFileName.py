# _str = f'<?xml version="1.0" encoding="utf-8"?><animation-list xmlns:android="http://schemas.android.com/apk/res/android" android:oneshot="false">'
#
# for i in range(179):
#     _str = _str + f'    <item android:drawable="@drawable/warriors_{i:0>5}" android:duration="48" />'
#
# _str = _str + f'</animation-list>'
# print(_str)


_str = ''
for i in range(121):
    _str = _str + f'           <ImageView android:layout_width="match_parent" android:layout_height="wrap_content" android:src="@mipmap/simple_warriors_{i:0>3}" />'

print(_str)
