package com.yonikim.aop_part4_chapter02.service

import retrofit2.Call
import retrofit2.http.GET

interface MusicService {

    @GET("/v3/ff912dde-2e71-411c-bfdb-28c443b6c519")
    fun listMusics(): Call<MusicDto>
}