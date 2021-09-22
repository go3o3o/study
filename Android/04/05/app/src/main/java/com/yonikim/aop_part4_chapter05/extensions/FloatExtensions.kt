package com.yonikim.aop_part4_chapter05.extensions

import android.content.res.Resources

internal fun Float.fromDpToPx(): Int = (this * Resources.getSystem().displayMetrics.density).toInt()