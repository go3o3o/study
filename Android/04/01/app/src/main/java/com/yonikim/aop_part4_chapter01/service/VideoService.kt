package com.yonikim.aop_part4_chapter01.service

import com.yonikim.aop_part4_chapter01.dto.VideoDto
import retrofit2.Call
import retrofit2.http.GET

interface VideoService {
    @GET("/v3/9dc401ea-e0b5-4313-ac19-01695a183ea7")
    fun listVideos(): Call<VideoDto>

}