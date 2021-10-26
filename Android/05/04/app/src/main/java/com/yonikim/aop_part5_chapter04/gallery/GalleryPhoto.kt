package com.yonikim.aop_part5_chapter04.gallery

import android.net.Uri

data class GalleryPhoto(
    val id: Long,
    val uri: Uri,
    val name: String,
    val date: String,
    val size: Int,
    val isSelected: Boolean = false
)
