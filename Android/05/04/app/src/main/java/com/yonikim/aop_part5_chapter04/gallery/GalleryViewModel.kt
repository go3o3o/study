package com.yonikim.aop_part5_chapter04.gallery

import androidx.lifecycle.ViewModel
import com.yonikim.aop_part5_chapter04.AopPart5Chapter04Application.Companion.appContext

class GalleryViewModel : ViewModel() {

    private val galleryPhotoRepository by lazy { GalleryPhotoRepository(appContext!!) }

    private lateinit var photoList: MutableList<GalleryPhoto9>

}